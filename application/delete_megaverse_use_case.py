from domain.repositories.map_repository import MapRepository


class DeleteMegaverseMapUseCase:
    def __init__(self, map_repository: MapRepository) -> None:
        self.map_repository: MapRepository = map_repository

    def delete_map(self) -> None:
        print("Deleting Megaverse Map")
        self.map_repository.delete_megaverse_map()
