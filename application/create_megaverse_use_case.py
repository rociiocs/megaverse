from domain.models.astral_object import AstralObject
from infraestructure.api_map_repository import MapRepository, ApiMapRepository


class CreateMegaverseMapUseCase:
    def __init__(self):
        self.map_repository: MapRepository = ApiMapRepository()

    def create_map(self):
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
        for astral_object in astral_objects:
            self.map_repository.create_astral_object(astral_object=astral_object)
