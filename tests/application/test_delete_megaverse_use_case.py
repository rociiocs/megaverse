from unittest import TestCase
from unittest.mock import Mock

from application.delete_megaverse_use_case import DeleteMegaverseMapUseCase
from domain.repositories.map_repository import MapRepository


class TestDeleteMegaverseMapUseCase(TestCase):
    def setUp(self):
        self.map_repository_mock = Mock(spec=MapRepository)
        self.use_case = DeleteMegaverseMapUseCase(map_repository=self.map_repository_mock)

    def test_delete_map(self):
        self.use_case.delete_map()

        self.map_repository_mock.delete_megaverse_map.assert_called_once()
