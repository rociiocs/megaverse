from models.astral_object import AstralObject


class Polyanet(AstralObject):
    def __init__(self, row: int, column: int):
        super().__init__(row=row, column=column)
