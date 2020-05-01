from yaml import safe_load, dump


class YamlFile:
    def __init__(self):
        self._content = None

    @property
    def content(self):
        return self._content

    def load(self, data):
        self._content = safe_load(data)

    def dump(self, stream):
        kargs = dict(
            default_flow_style=False,
            indent=2,
            width=80,
            allow_unicode=True,
            line_break=None,
            encoding="utf-8",
            sort_keys=False,
        )

        if not hasattr(stream, "write") and hasattr(stream, "open"):
            # pathlib.Path() instance
            with stream.open("w") as file:
                return dump(self._content, stream=file, **kargs)
        return dump(self._content, stream=stream, **kargs)

    def export(self):
        pass
