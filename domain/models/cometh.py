from domain.enums.cometh_direction_enum import ComethDirectionEnum
from domain.models.astral_object import AstralObject


class Cometh(AstralObject):
    def __init__(self, row: int, column: int, direction: ComethDirectionEnum):
        self.direction: ComethDirectionEnum = direction
        super().__init__(row=row, column=column)

    def __repr__(self):
        return f'Cometh {self.row}x{self.column} ({self.direction})'

    def get_plural_name(self) -> str:
        return 'comeths'
