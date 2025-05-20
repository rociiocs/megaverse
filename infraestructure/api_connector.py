import requests
from requests import Response


class ApiConnector:
    def post(self, url: str, data: dict = None, json: dict = None, headers: dict = None) -> Response:
        response = requests.post(url=url, data=data, json=json, headers=headers)
        response.raise_for_status()
        return response

    def get(self, url: str, params: dict = None, headers: dict = None) -> Response:
        response = requests.get(url=url, params=params, headers=headers)
        response.raise_for_status()
        return response
