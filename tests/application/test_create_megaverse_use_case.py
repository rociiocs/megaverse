from unittest import TestCase
from unittest.mock import Mock

from application.create_megaverse_use_case import CreateMegaverseMapUseCase
from domain.models.astral_object import AstralObject
from domain.repositories.map_repository import MapRepository


class TestCreateMegaverseMapUseCase(TestCase):
    def setUp(self):
        self.map_repository_mock = Mock(spec=MapRepository)
        self.use_case = CreateMegaverseMapUseCase(map_repository=self.map_repository_mock)

    def test_create_map(self):
        mock_astral_objects = [Mock(spec=AstralObject) for _ in range(3)]
        self.map_repository_mock.fetch_astral_objects.return_value = mock_astral_objects

        self.use_case.create_map()

        self.map_repository_mock.fetch_astral_objects.assert_called_once()
        self.map_repository_mock.create_astral_objects.assert_called_once_with(astral_objects=mock_astral_objects)
