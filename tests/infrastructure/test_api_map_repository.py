from unittest import TestCase
from unittest.mock import Mock

from requests import Response

from domain.models.astral_object import AstralObject
from infrastructure.api_map_repository import ApiMapRepository
from infrastructure.astral_object_adapter import AstralObjectAdapter
from infrastructure.common.file_service import FileService
from infrastructure.common.http_client import HttpClient


class TestApiMapRepository(TestCase):
    def setUp(self):
        self.http_client = Mock(HttpClient)
        self.file_service = Mock(FileService)
        self.adapter = Mock(AstralObjectAdapter)
        self.candidate_id = "1234"
        self.goal_map_url = "http://example/{candidate_id}/map"
        self.cometh_url = "http://example/cometh.url"
        self.polyanet_url = "http://example/polyanet"
        self.soloon_url = "http://example/soloon"
        self.file_path = "resources/multiple_data.json"

        self.api_map_repository = ApiMapRepository(
            http_client=self.http_client,
            file_service=self.file_service,
            astral_object_adapter=self.adapter,
            candidate_id=self.candidate_id,
            goal_map_url=self.goal_map_url,
            cometh_url=self.cometh_url,
            polyanet_url=self.polyanet_url,
            soloon_url=self.soloon_url
        )

    def test_fetch_astral_objects_success(self):
        mock_response = Mock(spec=Response)
        mock_response.json.return_value = {
            "goal": [["COMETH", "SPACE", "POLYANET"], ["SPACE", "RED_SOLOON", "SPACE"]]
        }
        self.http_client.get.return_value = mock_response

        expected_astral_objects = [Mock(spec=AstralObject), Mock(spec=AstralObject)]
        self.adapter.get_list_astral_objects.return_value = expected_astral_objects

        result = self.api_map_repository.fetch_astral_objects()

        self.assertEqual(result, expected_astral_objects)
        self.http_client.get.assert_called_once()
        self.adapter.get_list_astral_objects.assert_called_once()

    def test_fetch_astral_objects_invalid_map(self):
        mock_response = Mock(spec=Response)
        mock_response.json.return_value = {"goal": "invalid_map"}
        self.http_client.get.return_value = mock_response

        with self.assertRaises(ValueError):
            self.api_map_repository.fetch_astral_objects()

    def test_create_astral_objects_success(self):
        astral_object = Mock(spec=AstralObject)
        astral_object.__class__.__name__ = "Polyanet"
        astral_object.to_dict.return_value = {"row": 1, "column": 1}

        self.api_map_repository.create_astral_objects([astral_object])

        self.http_client.post_retry.assert_called_once()
        expected_astral_objects_data = [
            {'url': 'http://example/polyanet', 'json': {'row': 1, 'column': 1, 'candidateId': '1234'}}]

        self.file_service.save_data_list.assert_called_once_with(
            data_list=expected_astral_objects_data,
            file_path=self.file_path
        )

    def test_delete_megaverse_map(self):
        self.file_service.get_data_list.return_value = [{"url": "url", "json": {"data": 123}}]

        self.api_map_repository.delete_megaverse_map()

        self.http_client.delete_retry.assert_called_once_with(url="url", json={"data": 123})
        self.file_service.get_data_list.assert_called_once_with(self.file_path)
