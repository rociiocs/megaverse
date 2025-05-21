from abc import abstractmethod, ABC

from domain.models.astral_object import AstralObject


class MapRepository(ABC):
    @abstractmethod
    def fetch_astral_objects(self) -> list[AstralObject]:
        pass

    @abstractmethod
    def create_astral_object(self, astral_object: AstralObject) -> None:
        pass
