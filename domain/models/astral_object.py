from abc import ABC


class AstralObject(ABC):
    def __init__(self, row: int, column: int):
        self.row: int = row
        self.column: int = column

    def get_plural_name(self) -> str:
        pass
