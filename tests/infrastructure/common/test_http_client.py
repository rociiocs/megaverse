import unittest
from unittest.mock import patch, Mock

import requests

from infrastructure.common.http_client import HttpClient


class TestHttpClient(unittest.TestCase):
    def setUp(self):
        self.client = HttpClient()
        self.url = "https://example.com"

    @patch("requests.post")
    def test_post_success(self, mock_post):
        mock_response = Mock(status_code=200)
        mock_post.return_value = mock_response

        response = self.client.post(url=self.url, json={"foo": "bar"})

        mock_post.assert_called_once()
        self.assertEqual(response, mock_response)

    @patch("requests.post")
    @patch("time.sleep", return_value=None)
    def test_post_retry_success_after_429(self, mock_sleep, mock_post):
        mock_429 = Mock(status_code=429, headers={"Retry-After": "1"})
        mock_success = Mock(status_code=200)
        mock_post.side_effect = [mock_429, mock_success]

        response = self.client.post_retry(url=self.url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(mock_post.call_count, 2)
        mock_sleep.assert_called_once_with(1)

    @patch("requests.post")
    @patch("time.sleep", return_value=None)
    def test_post_retry_exceeds_max_retries(self, mock_sleep, mock_post):
        mock_429 = Mock(status_code=429, headers={"Retry-After": "2"})
        mock_429.raise_for_status.side_effect = requests.exceptions.HTTPError("429 Too Many Requests")
        mock_post.return_value = mock_429

        with self.assertRaises(Exception):
            self.client.post_retry(url=self.url, max_retries=3)

        self.assertEqual(mock_post.call_count, 3)
        self.assertEqual(mock_sleep.call_count, 3)

    @patch("requests.get")
    def test_get_success(self, mock_get):
        mock_response = Mock(status_code=200)
        mock_get.return_value = mock_response

        response = self.client.get(url=self.url)

        mock_get.assert_called_once()
        self.assertEqual(response, mock_response)

    @patch("requests.delete")
    def test_delete_success(self, mock_delete):
        mock_response = Mock(status_code=200)
        mock_delete.return_value = mock_response

        response = self.client.delete(url=self.url)

        mock_delete.assert_called_once()
        self.assertEqual(response, mock_response)

    @patch("requests.delete")
    @patch("time.sleep", return_value=None)
    def test_delete_retry_success_after_429(self, mock_sleep, mock_delete):
        mock_429 = Mock(status_code=429, headers={"Retry-After": "3"})
        mock_success = Mock(status_code=204)
        mock_delete.side_effect = [mock_429, mock_success]

        response = self.client.delete_retry(url=self.url)

        self.assertEqual(response.status_code, 204)
        self.assertEqual(mock_delete.call_count, 2)
        mock_sleep.assert_called_once_with(3)

    @patch("requests.delete")
    @patch("time.sleep", return_value=None)
    def test_delete_retry_exceeds_max_retries(self, mock_sleep, mock_delete):
        mock_429 = Mock(status_code=429, headers={"Retry-After": "2"})
        mock_429.raise_for_status.side_effect = requests.exceptions.HTTPError("429 Too Many Requests")
        mock_delete.return_value = mock_429

        with self.assertRaises(Exception):
            self.client.delete_retry(url=self.url, max_retries=3)

        self.assertEqual(mock_delete.call_count, 3)
        self.assertEqual(mock_sleep.call_count, 3)
