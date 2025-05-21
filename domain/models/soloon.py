from dataclasses import dataclass

from domain.enums.astral_color_enum import AstralColorEnum
from domain.models.astral_object import AstralObject


@dataclass
class Soloon(AstralObject):
    color: AstralColorEnum

    def __repr__(self) -> str:
        return f'Soloon {self.row}x{self.column} ({self.color})'

    def to_dict(self) -> dict:
        data = super().to_dict()
        data.update({"color": self.color.value})
        return data
