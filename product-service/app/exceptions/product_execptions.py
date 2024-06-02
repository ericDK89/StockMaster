"""File to create Product customer Exceptions"""


class ProductException(Exception):
    """Class to handle Product Exceptions

    Args:
        Exception (Exception): Main class Exception
    """

    def __init__(self, name: str, message: str) -> None:
        self.name: str = name
        self.message: str = message
        super().__init__(self.message)
