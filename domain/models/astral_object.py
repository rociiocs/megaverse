from abc import ABC
from dataclasses import dataclass


@dataclass
class AstralObject(ABC):
    row: int
    column: int

    def to_dict(self) -> dict:
        return {
            'row': self.row,
            'column': self.column,
        }
