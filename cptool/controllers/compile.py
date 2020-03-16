import subprocess
from pathlib import Path

_LANGS = {
    ".rs": {"compile": "rustc '{input}' -o '{output}'", "execute": "./{} < {} > {}"},
    ".cpp": {"compile": "g++ '{input}' -o '{output}'", "execute": "./{} < {} > {}"},
    ".py": {"execute": "python3 {input} < {} > {}"},
}


def compile(code_path: Path, compiled_output_dir: Path):
    compiled_output_dir.mkdir(parents=True, exist_ok=True)

    lang = _LANGS[code_path.suffix]
    compiled_output_path = compiled_output_dir / code_path.stem
    if "compile" in lang:
        subprocess.check_call(
            lang["compile"].format(input=code_path, output=compiled_output_path),
            shell=True,
        )
        print(f"Successfully compiled file {code_path} in {compiled_output_path}")

    return lang, compiled_output_path


def execute(lang, compiled_code_path, input_path, output_path):
    subprocess.check_call(
        lang["execute"].format(compiled_code_path, input_path, output_path), shell=True
    )
