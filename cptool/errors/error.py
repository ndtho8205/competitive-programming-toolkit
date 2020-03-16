class Error(BaseException):
    message = "Generic Error"

    def get_message(self):
        return self.message
