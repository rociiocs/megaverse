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
            object_name, property_name = AstralObjectFactory.get_object_and_property_name(name)
            astral_object_class: Optional[Type[AstralObject]] = AstralObjectFactory[object_name.upper()].value
            if astral_object_class is None:
                return None
            if property_name is not None:
                return astral_object_class(*args, property_name, **kwargs)
            return astral_object_class(*args, **kwargs)
        except KeyError:
            raise ValueError(f"There is not any astral object '{name}'.")
        except TypeError as e:
            raise ValueError(f"Error creating '{name}': {e}")

    @staticmethod
    def get_object_and_property_name(name: str) -> tuple[str, Optional[str]]:
        try:
            splitted_name = name.split("_")
            if len(splitted_name) < 2:
                return splitted_name[0], None
            print(f"{splitted_name[1]} , {splitted_name[0]}")
            return splitted_name[1], splitted_name[0]
        except ValueError:
            raise ValueError(f"Error parsing '{name}'.")
