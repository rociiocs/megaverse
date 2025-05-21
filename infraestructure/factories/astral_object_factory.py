from typing import Optional, Type

from domain.enums.astral_color_enum import AstralColorEnum
from domain.enums.cometh_direction_enum import DirectionEnum
from domain.models.astral_object import AstralObject
from domain.models.cometh import Cometh
from domain.models.polyanet import Polyanet
from domain.models.soloon import Soloon


class AstralObjectFactory:
    astral_object_class_mapper = {
        "polyanet": Polyanet,
        "soloon": Soloon,
        "cometh": Cometh,
    }

    PROPERTY_ENUM_MAPPER = {
        "polyanet": None,
        "soloon": AstralColorEnum,
        "cometh": DirectionEnum,
    }

    def create(self, object_type: str, property_value: Optional[str], *args, **kwargs) -> AstralObject:
        try:
            astral_object_class: Optional[Type[AstralObject]] = self.astral_object_class_mapper[object_type]

            if property_value is None:
                return astral_object_class(*args, **kwargs)

            astral_object_property = self.__get_astral_object_property(object_type, property_value)
            return astral_object_class(*args, astral_object_property, **kwargs)

        except KeyError:
            raise ValueError(f"There is not any astral object '{object_type}'.")
        except TypeError as e:
            raise ValueError(f"Error creating '{object_type}': {e}")

    def __get_astral_object_property(self, object_type: str, property_name: str) -> Optional[any]:
        astral_object_property_enum = self.PROPERTY_ENUM_MAPPER.get(object_type)
        if astral_object_property_enum is None:
            return None

        return astral_object_property_enum(property_name)
