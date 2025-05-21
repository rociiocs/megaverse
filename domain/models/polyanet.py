from dataclasses import dataclass

from domain.models.astral_object import AstralObject


@dataclass
class Polyanet(AstralObject):

    def __repr__(self) -> str:
        return f'Polyanet {self.row}x{self.column}'
