class StockException(Exception):
    def __init__(self, name: str, message: str) -> None:
        self.name: str = name
        self.message: str = message
        super().__init__(self.message)
