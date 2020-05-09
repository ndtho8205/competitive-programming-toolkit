from pathlib import Path

from cptool.languages import BaseCodeFile


class CppFile(BaseCodeFile):
    SUFFIX = [".cpp"]

    def compile_instruction(self, code_file: Path, compiled_code_file: Path):
        return [
            "g++",
            "-Wall",
            "-Wextra",
            "-Werror",
            "-O2",
            "-pedantic",
            "-std=c++11",
            "-Wshadow",
            "-Wfloat-equal",
            "-Wconversion",
            "-Wlogical-op",
            "-Wduplicated-cond",
            "-fsanitize=address",
            "-fsanitize=undefined",
            "-fno-sanitize-recover",
            "-fstack-protector",
            code_file,
            "-o",
            compiled_code_file,
        ]
