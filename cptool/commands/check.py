class CheckCommand:
    """Check the validity of the `project.toml` file."""

    def __call__(self, args):
        self.handle()

    def register_arguments(self, parser):
        pass

    def handle(self):
        # yaml_file = XXX.locate(Path.cwd())
        # results = ProblemYaml.validate(yaml_file)
        # raise errors.CptoolError("{}".format(results))
        raise NotImplementedError("command `check` has not been implemented yet")
