import sys


class Env:
    platform = None
    is_linux = False
    is_windows = False

    def __init__(self):
        self.platform = sys.platform
        if self.platform == "linux":
            self.is_linux = True
