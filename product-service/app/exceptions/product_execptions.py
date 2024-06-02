class ProductException(Exception):
    def __init__(self, type: str, message: str):
        self.type = type
        self.message = message
        super().__init__(self.message)
