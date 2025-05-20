from domain.enums.astral_color_enum import AstralColorEnum
from domain.models.astral_object import AstralObject


class Soloon(AstralObject):
    def __init__(self, color: AstralColorEnum, row: int, column: int):
        self.color: AstralColorEnum = color
        super().__init__(row=row, column=column)

    def __repr__(self):
        return f'Soloon {self.row}x{self.column} ({self.color})'

    def get_plural_name(self) -> str:
        return 'soloons'