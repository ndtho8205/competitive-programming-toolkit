from cptool.helpers import errors


class TestCommand:
    """Test your codes on test cases."""

    def __call__(self, env, args):
        raise errors.CommandNotImplemented("test")

    def register_arguments(self, parser):
        pass
