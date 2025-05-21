from dataclasses import dataclass

from domain.enums.cometh_direction_enum import DirectionEnum
from domain.models.astral_object import AstralObject


@dataclass
class Cometh(AstralObject):
    direction: DirectionEnum

    def __repr__(self) -> str:
        return f'Cometh {self.row}x{self.column} ({self.direction})'

    def to_dict(self) -> dict:
        data = super().to_dict()
        data.update({"direction": self.direction.value})
        return data
