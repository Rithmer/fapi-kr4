class CustomExceptionA(Exception):
    def __init__(self, message: str = "Business rule A violated") -> None:
        self.message = message


class CustomExceptionB(Exception):
    def __init__(self, message: str = "Requested resource does not exist") -> None:
        self.message = message
