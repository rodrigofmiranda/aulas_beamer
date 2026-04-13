#!/usr/bin/env python3
"""Mechanical preflight for lesson .tex files.

This script catches the repetitive issues that kept appearing in the
lesson workflow: placeholders that survived to the final PDF, glossary
anti-patterns, code blocks that are hard to copy, and compile/log
problems that can be verified automatically.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
MANIFEST_DIR = ROOT / "admin" / "class_manifests" / "classes"


@dataclass
class Finding:
    severity: str
    tag: str
    message: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run automatic checks for a generated lesson."
    )
    parser.add_argument(
        "--class",
        dest="class_number",
        type=int,
        help="Class number to resolve through the manifest.",
    )
    parser.add_argument(
        "--tex",
        type=Path,
        help="Direct path to the lesson .tex file.",
    )
    parser.add_argument(
        "--compile",
        action="store_true",
        help="Compile with latexmk and inspect log/PDF output.",
    )
    return parser.parse_args()


def read_text(path: Path) -> str:
    for encoding in ("utf-8", "utf-8-sig", "latin-1"):
        try:
            return path.read_text(encoding=encoding)
        except UnicodeDecodeError:
            continue
    raise UnicodeDecodeError("unknown", b"", 0, 1, f"Could not decode {path}")


def load_manifest(class_number: int) -> dict | None:
    manifest_path = MANIFEST_DIR / f"class_{class_number:02d}.json"
    if not manifest_path.exists():
        return None
    return json.loads(read_text(manifest_path))


def resolve_tex_path(args: argparse.Namespace) -> tuple[Path, dict | None]:
    manifest = None
    if args.tex:
        tex_path = args.tex
        if not tex_path.is_absolute():
            tex_path = (ROOT / tex_path).resolve()
        if args.class_number is not None:
            manifest = load_manifest(args.class_number)
        return tex_path, manifest

    if args.class_number is None:
        raise SystemExit("Use --class N or --tex PATH.")

    manifest = load_manifest(args.class_number)
    if manifest is None:
        raise SystemExit(f"Manifest not found for class {args.class_number:02d}.")

    pattern = manifest.get("expected_tex_glob")
    if not pattern:
        raise SystemExit(f"Manifest for class {args.class_number:02d} has no expected_tex_glob.")

    matches = sorted(ROOT.glob(pattern))
    if not matches:
        raise SystemExit(f"No lesson .tex found for class {args.class_number:02d} using {pattern}.")
    if len(matches) > 1:
        raise SystemExit(
            f"More than one lesson .tex matched class {args.class_number:02d}: "
            + ", ".join(str(path.relative_to(ROOT)) for path in matches)
        )
    return matches[0].resolve(), manifest


def extract_frames(tex: str) -> list[tuple[str, str]]:
    pattern = re.compile(
        r"\\begin\{frame\}(?:\[[^\]]*\])?\{(?P<title>[^}]*)\}(?P<body>.*?)\\end\{frame\}",
        re.DOTALL,
    )
    return [(match.group("title"), match.group("body")) for match in pattern.finditer(tex)]


def add(findings: list[Finding], severity: str, tag: str, message: str) -> None:
    findings.append(Finding(severity=severity, tag=tag, message=message))


def check_tex(tex_path: Path, manifest: dict | None) -> list[Finding]:
    findings: list[Finding] = []
    tex = read_text(tex_path)
    tex_lower = tex.lower()

    conditional_assets = re.findall(r"\\IfFileExists\s*\{([^}]+)\}", tex)
    for raw_asset in conditional_assets:
        asset_name = Path(raw_asset).name.lower()
        if asset_name.startswith("fig"):
            add(
                findings,
                "ERROR",
                "[FIGURA DO LIVRO AUSENTE]",
                r"Encontrado `\IfFileExists` envolvendo figura da aula; substituir por asset real na pasta da aula.",
            )
            break

    placeholder_patterns = (
        "figura del libro no disponible",
        "figura do livro não disponível",
        "figura do livro nao disponivel",
    )
    for phrase in placeholder_patterns:
        if phrase in tex_lower:
            add(
                findings,
                "ERROR",
                "[FIGURA DO LIVRO AUSENTE]",
                "O .tex ainda contém bloco de placeholder para figura do livro.",
            )
            break

    if re.search(r"numbers\s*=\s*(left|right)", tex):
        add(
            findings,
            "ERROR",
            "[CÓDIGO NÃO COPIÁVEL]",
            "Há numeração de linhas ativa em bloco/listing copiável.",
        )

    if r"\xrightarrow" in tex:
        add(
            findings,
            "ERROR",
            "[ATIVIDADE IRRESOLVÍVEL]",
            r"Encontrado `\xrightarrow{}`; usar notação textual plana nas respostas.",
        )

    aggressive_shrink = re.findall(r"\\begin\{frame\}\[shrink=(\d+)\]", tex)
    for raw_value in aggressive_shrink:
        if int(raw_value) > 10:
            add(
                findings,
                "ERROR",
                "[COMPOSIÇÃO VISUAL]",
                f"Frame com shrink={raw_value}; isso passa do limite aceitável do projeto.",
            )

    frames = extract_frames(tex)
    gloss_frames: list[tuple[str, str]] = []
    total_gloss_cards = 0

    for title, body in frames:
        if "glosario" in title.lower():
            gloss_frames.append((title, body))
            cards = len(re.findall(r"\\glosscard\s*\{", body))
            total_gloss_cards += cards
            if r"\begin{description}" in body:
                add(
                    findings,
                    "WARN",
                    "[GLOSSÁRIO]",
                    f"O frame de glossário '{title}' ainda usa `description` cru.",
                )
            if cards == 0:
                add(
                    findings,
                    "WARN",
                    "[GLOSSÁRIO]",
                    f"O frame de glossário '{title}' não usa `\\glosscard`.",
                )

    if gloss_frames:
        avg_cards = total_gloss_cards / len(gloss_frames)
        if len(gloss_frames) >= 3 and avg_cards < 4:
            add(
                findings,
                "WARN",
                "[GLOSSÁRIO]",
                "Glossário ficou espalhado demais para a quantidade de cartões atual; revisar densidade útil por frame.",
            )

    image_refs = re.findall(r"\\includegraphics(?:\[[^\]]*\])?\{([^}]+)\}", tex)
    for raw_ref in image_refs:
        ref = raw_ref.strip()
        asset_path = tex_path.parent / ref
        if not asset_path.suffix:
            candidates = [asset_path.with_suffix(ext) for ext in (".png", ".jpg", ".jpeg", ".pdf")]
        else:
            candidates = [asset_path]

        if Path(ref).name.lower() == "logo.jpg":
            continue

        if not any(candidate.exists() for candidate in candidates):
            tag = "[FIGURA DO LIVRO AUSENTE]" if Path(ref).name.startswith("fig") else "[TÉCNICO LATEX]"
            add(
                findings,
                "ERROR",
                tag,
                f"Asset referenciado por includegraphics não existe: {ref}",
            )

    lesson_type = ((manifest or {}).get("lesson_type") or {}).get("normalized")
    if lesson_type == "lab":
        code_like = any(token in tex for token in (r"\begin{lstlisting}", r"\lstinputlisting", ".py", ".sh"))
        if code_like and "shell.cloud.google.com" not in tex_lower:
            add(
                findings,
                "WARN",
                "[SEPARAÇÃO]",
                "Aula de lab com código, mas sem referência explícita a shell.cloud.google.com.",
            )

        heuristic_groups = {
            "previsão": ("predic", "hipótes", "antes de ejecutar", "antes de correr", "qué cre", "que cre"),
            "observação": ("observ", "anotá", "anota", "registr", "mirá", "mira", "qué pasó", "que paso"),
            "explicação": ("explic", "compar", "interpret"),
        }
        missing_groups = [
            label
            for label, stems in heuristic_groups.items()
            if not any(stem in tex_lower for stem in stems)
        ]
        if missing_groups:
            add(
                findings,
                "WARN",
                "[EXPERIMENTO MECÂNICO]",
                "O lab não mostra com clareza todos os verbos esperados do experimento guiado: "
                + ", ".join(missing_groups)
                + ".",
            )

    return findings


def run_command(command: list[str], workdir: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        command,
        cwd=workdir,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        check=False,
    )


def find_missing_assets(log_text: str) -> Iterable[str]:
    patterns = (
        r"File [`']([^`']+)['`] not found",
        r"LaTeX Warning: File `([^`]+)' not found",
    )
    for pattern in patterns:
        for match in re.finditer(pattern, log_text):
            yield match.group(1)


def analyze_pdf_text(pdf_path: Path, findings: list[Finding]) -> None:
    result = run_command(["pdftotext", "-layout", str(pdf_path), "-"], pdf_path.parent)
    if result.returncode != 0:
        add(
            findings,
            "WARN",
            "[CÓDIGO NÃO COPIÁVEL]",
            "Não foi possível extrair texto do PDF com pdftotext para a checagem automática.",
        )
        return

    extracted = result.stdout or ""
    numbered_code = re.findall(
        r"(?m)^\s{0,5}\d+\s+(?:def |for |if |while |import |from |class |echo |python |print\(|[A-Za-z_][A-Za-z0-9_]*\s*=)",
        extracted,
    )
    if numbered_code:
        add(
            findings,
            "WARN",
            "[CÓDIGO NÃO COPIÁVEL]",
            "A extração do PDF sugere que ainda há código com numeração ou prefixo nocivo ao copiar.",
        )


def compile_and_check(tex_path: Path) -> list[Finding]:
    findings: list[Finding] = []
    tex_dir = tex_path.parent
    command = [
        "latexmk",
        "-pdf",
        "-interaction=nonstopmode",
        "-halt-on-error",
        "-file-line-error",
        tex_path.name,
    ]
    result = run_command(command, tex_dir)
    if result.returncode != 0:
        add(
            findings,
            "ERROR",
            "[TÉCNICO LATEX]",
            "latexmk falhou na compilação. Verificar o log da aula.",
        )

    log_path = tex_path.with_suffix(".log")
    if not log_path.exists():
        add(
            findings,
            "ERROR",
            "[TÉCNICO LATEX]",
            "Compilação terminou sem gerar arquivo .log esperável.",
        )
        return findings

    log_text = read_text(log_path)

    missing_assets = sorted(set(find_missing_assets(log_text)))
    for missing in missing_assets:
        tag = "[FIGURA DO LIVRO AUSENTE]" if Path(missing).name.startswith("fig") else "[TÉCNICO LATEX]"
        add(
            findings,
            "ERROR",
            tag,
            f"Compilação reportou asset ausente: {missing}",
        )

    for match in re.finditer(r"Overfull \\hbox \(([\d.]+)pt too wide\)", log_text):
        amount = float(match.group(1))
        if amount > 5:
            add(
                findings,
                "WARN",
                "[COMPOSIÇÃO VISUAL]",
                f"Log ainda tem Overfull hbox real de {amount:.1f}pt.",
            )

    for match in re.finditer(r"Overfull \\vbox \(([\d.]+)pt too high\)", log_text):
        amount = float(match.group(1))
        if amount > 5:
            add(
                findings,
                "WARN",
                "[COMPOSIÇÃO VISUAL]",
                f"Log ainda tem Overfull vbox de {amount:.1f}pt; confirmar se não é falso positivo de imagem.",
            )

    pdf_path = tex_path.with_suffix(".pdf")
    if pdf_path.exists():
        analyze_pdf_text(pdf_path, findings)
    else:
        add(
            findings,
            "ERROR",
            "[TÉCNICO LATEX]",
            "Compilação não gerou PDF final.",
        )

    return findings


def print_report(tex_path: Path, manifest: dict | None, findings: list[Finding], compile_mode: bool) -> None:
    rel_path = tex_path.relative_to(ROOT) if tex_path.is_relative_to(ROOT) else tex_path
    print("== Lesson preflight ==")
    print(f"Arquivo: {rel_path}")
    if manifest:
        lesson_type = ((manifest.get('lesson_type') or {}).get('normalized')) or "unknown"
        print(f"Aula: {manifest.get('class_number')} ({lesson_type})")
    print(f"Modo compilação: {'sim' if compile_mode else 'não'}")

    if not findings:
        print("Status: limpo")
        return

    errors = [f for f in findings if f.severity == "ERROR"]
    warns = [f for f in findings if f.severity == "WARN"]
    print(f"Resumo: {len(errors)} erro(s), {len(warns)} aviso(s)")
    for finding in findings:
        print(f"{finding.severity:5} {finding.tag} {finding.message}")


def main() -> int:
    args = parse_args()
    tex_path, manifest = resolve_tex_path(args)
    if not tex_path.exists():
        raise SystemExit(f"Arquivo .tex não encontrado: {tex_path}")

    findings = check_tex(tex_path, manifest)
    if args.compile:
        findings.extend(compile_and_check(tex_path))

    print_report(tex_path, manifest, findings, args.compile)
    return 1 if any(f.severity == "ERROR" for f in findings) else 0


if __name__ == "__main__":
    sys.exit(main())
