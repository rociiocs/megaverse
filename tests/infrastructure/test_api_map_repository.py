import os
from unittest import TestCase
from unittest.mock import patch, mock_open, Mock

from requests import Response

from domain.models.astral_object import AstralObject
from infrastructure.api_map_repository import ApiMapRepository
from infrastructure.astral_object_adapter import AstralObjectAdapter
from infrastructure.common.http_client import HttpClient


class TestApiMapRepository(TestCase):
    def setUp(self):
        self.http_client = Mock(HttpClient)
        self.adapter = Mock(AstralObjectAdapter)
        self.candidate_id = "1234"
        self.goal_map_url = "http://example/{candidate_id}/map"
        self.cometh_url = "http://example/cometh.url"
        self.polyanet_url = "http://example/polyanet"
        self.soloon_url = "http://example/soloon"

        self.api_map_repository = ApiMapRepository(
            http_client=self.http_client,
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
        self.assertTrue(os.path.exists("resources/multiple_data.json"))

    @patch("builtins.open", new_callable=mock_open, read_data='[{"url": "test", "json": {"a": 1}}]')
    def test_get_data_list_success(self, mock_file):
        data = self.api_map_repository._ApiMapRepository__get_data_list()
        self.assertEqual(data, [{"url": "test", "json": {"a": 1}}])

    @patch("builtins.open", side_effect=FileNotFoundError)
    def test_get_data_list_file_not_found(self, mock_file):
        data = self.api_map_repository._ApiMapRepository__get_data_list()
        self.assertEqual(data, [])

    @patch("builtins.open", new_callable=mock_open)
    @patch("os.makedirs")
    def test_save_data_list(self, mock_makedirs, mock_file):
        self.api_map_repository._ApiMapRepository__save_data_list([{"test": "value"}])
        mock_makedirs.assert_called_once_with("resources", exist_ok=True)
        mock_file.assert_called_once_with("resources/multiple_data.json", "w")

    @patch("infrastructure.api_map_repository.ApiMapRepository._ApiMapRepository__get_data_list")
    def test_delete_megaverse_map(self, mock_get_data_list):
        mock_get_data_list.return_value = [{"url": "url", "json": {"data": 123}}]

        self.api_map_repository.delete_megaverse_map()

        self.http_client.delete_retry.assert_called_once_with(url="url", json={"data": 123})
