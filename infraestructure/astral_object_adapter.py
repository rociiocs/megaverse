from typing import Optional

from domain.models.astral_object import AstralObject
from infraestructure.factories.astral_object_factory import AstralObjectFactory


class AstralObjectAdapter:
    SPACE = "SPACE"

    def __init__(self) -> None:
        self.astral_objects_factory = AstralObjectFactory()

    def get_list_astral_objects(self, megaverse_map_json: dict) -> list[AstralObject]:
        astral_objects: list[AstralObject] = []

        for row_index, row in enumerate(megaverse_map_json):
            for col_index, cell in enumerate(row):
                if cell == self.SPACE:
                    continue

                object_type, property_value = self.__get_object_type_and_property_value(cell)

                astral_object = self.astral_objects_factory.create(
                    object_type,
                    property_value,
                    row_index,
                    col_index)

                astral_objects.append(astral_object)

        return astral_objects

    def __get_object_type_and_property_value(self, name: str) -> tuple[str, Optional[str]]:
        try:
            split_name = name.lower().split("_")

            if len(split_name) < 2:
                return split_name[0], None

            return split_name[1], split_name[0]
        except ValueError:
            raise ValueError(f"Error parsing '{name}'.")
