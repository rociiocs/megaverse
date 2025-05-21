from domain.repositories.map_repository import MapRepository
from infraestructure.api_map_repository import ApiMapRepository


class DeleteMegaverseMapUseCase:
    def __init__(self) -> None:
        self.map_repository: MapRepository = ApiMapRepository()

    def delete_map(self) -> None:
        print("Deleting Megaverse Map")
        self.map_repository.delete_megaverse_map()
