from unittest import TestCase
from unittest.mock import patch, mock_open

from infrastructure.common.file_service import FileService


class TestFileService(TestCase):
    def setUp(self):
        self.file_service = FileService()
        self.file_path = "resources/multiple_data.json"

    @patch("builtins.open", new_callable=mock_open, read_data='[{"url": "test", "json": {"a": 1}}]')
    def test_get_data_list_success(self, _):
        data = self.file_service.get_data_list(self.file_path)
        self.assertEqual(data, [{"url": "test", "json": {"a": 1}}])

    @patch("builtins.open", side_effect=FileNotFoundError)
    def test_get_data_list_file_not_found(self, _):
        data = self.file_service.get_data_list(self.file_path)
        self.assertEqual(data, [])

    @patch("builtins.open", new_callable=mock_open)
    @patch("os.makedirs")
    def test_save_data_list(self, mock_makedirs, mock_file):
        self.file_service.save_data_list([{"test": "value"}], self.file_path)
        mock_makedirs.assert_called_once_with("resources", exist_ok=True)
        mock_file.assert_called_once_with(self.file_path, "w")
