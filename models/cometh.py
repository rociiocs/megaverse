from models.astral_object import AstralObject
from models.cometh_direction import ComethDirection


class Cometh(AstralObject):
    def __init__(self, direction: ComethDirection, row: int, column: int):
        self.direction: ComethDirection = direction
        super().__init__(row=row, column=column)
