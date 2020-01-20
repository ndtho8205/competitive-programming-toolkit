LANGS = {
    {"ext": ["cpp"], "command": "g++", "flags": []},
    {"ext": ["py"], "command": "python3", "flags": []},
}


def compile(code_path, flags):
    pass


def execute(code_path, input_path, output_path):
    print(f"g++ {code_path} {input_path} {output_path}")
