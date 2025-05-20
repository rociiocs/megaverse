from models.astral_color import AstralColor
from models.astral_object import AstralObject


class Soloon(AstralObject):
    def __init__(self, color: AstralColor, row: int, column: int):
        self.color: AstralColor = color
        super().__init__(row=row, column=column)
