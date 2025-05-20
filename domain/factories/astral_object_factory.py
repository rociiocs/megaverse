from enum import Enum
from typing import Optional, Type

from domain.models.astral_object import AstralObject
from domain.models.cometh import Cometh
from domain.models.polyanet import Polyanet
from domain.models.soloon import Soloon


class AstralObjectFactory(Enum):
    POLYANET = Polyanet
    SOLOON = Soloon
    COMETH = Cometh
    SPACE = None

    @staticmethod
    def create_astral_object(name: str, *args, **kwargs):
        try:
            astral_object_class: Optional[Type[AstralObject]] = AstralObjectFactory[name.upper()].value
            if astral_object_class is None:
                return None
            return astral_object_class(*args, **kwargs)
        except KeyError:
            raise ValueError(f"There is not any astral object '{name}'.")
        except TypeError as e:
            raise ValueError(f"Error creating '{name}': {e}")
