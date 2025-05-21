from domain.models.astral_object import AstralObject
from domain.repositories.map_repository import MapRepository
from infraestructure.api_map_repository import ApiMapRepository


class CreateMegaverseMapUseCase:
    def __init__(self) -> None:
        self.map_repository: MapRepository = ApiMapRepository()


def create_map(self) -> None:
    print("Creating Megaverse Map")

    astral_objects: list[AstralObject] = self.__get_astral_objects()
    self.__create_astral_objects(astral_objects)

    print("Megaverse Map created")


def __get_astral_objects(self) -> list[AstralObject]:
    print("Getting Astral Objects from Goal Map")

    astral_objects: list[AstralObject] = self.map_repository.fetch_astral_objects()
    print(astral_objects)

    return astral_objects


def __create_astral_objects(self, astral_objects: list[AstralObject]):
    print("Creating astral objects")
    self.map_repository.create_astral_objects(astral_objects=astral_objects)
