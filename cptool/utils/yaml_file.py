from io import StringIO

from ruamel.yaml import YAML


class YamlFile(YAML):
    def __init__(self):
        super().__init__()
        self.indent(mapping=2, sequence=4, offset=2)
        self.default_flow_style = False
        self.width = 90

    def load(self, stream):
        return super().load(stream)

    def dump(self, data, stream=None):
        get_value = False
        if stream is None:
            stream = StringIO()
            get_value = True

        super().dump(data, stream)

        return stream.getvalue() if get_value else None
