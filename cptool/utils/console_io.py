def line(data: str = ""):
    print(data)


def ask(question: str, default: str = ""):
    print(question, end="")
    return input() or default


def confirm(question: str, default: bool = True):
    print(question, end="")
    answer = input()

    if not answer:
        return default
    if answer.lower() in ["y", "yes"]:
        return True
    return False


class Codes:
    FOREGROUND_COLORS = {
        "black": 30,
        "red": 31,
        "green": 32,
        "yellow": 33,
        "blue": 34,
        "white": 97,
    }

    BACKGROUND_COLORS = {
        "black": 40,
        "red": 41,
        "green": 42,
        "yellow": 43,
        "blue": 44,
        "white": 107,
    }

    FORMATS = {
        "bold": 1,
        "dim": 2,
        "underline": 4,
        "blink": 5,
        "reverse": 7,
        "hidden": 8,
    }


class Style:
    ESCAPE = "\033["
    RESET = ""

    def __init__(self, fg=None, bg=None, formats=None):
        self.codes = []

        if fg in Codes.FOREGROUND_COLORS.keys():
            self.codes.append(Codes.FOREGROUND_COLORS[fg])
        else:
            pass

        self.fg = fg
        self.bg = bg
        self.formats = formats

    def render_code(self):
        return "\033[{}m".format(self.fg, self.bg, self.formats)


class Colorize:
    INFO = Style(fg="", bg="", formats=[""])
    WARNING = Style(fg="", bg="", formats=[""])
    ERROR = Style(fg="", bg="", formats=[""])

    def __init__():
        pass

    def colorize(self, text, style):
        return "{}{}{}".format(style, text, Codes.RESET)

    def info(self, text):
        return self.colorize(text, self.INFO)

    def warning(self, text):
        return self.colorize(text, self.WARNING)

    def error(self, text):
        return self.colorize(text, self.ERROR)
