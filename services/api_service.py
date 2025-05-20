from requests import Response

from domain.models.astral_object import AstralObject
from infraestructure.api_connector import ApiConnector


class ApiService:
    def __init__(self):
        self.api_connector = ApiConnector()

    def fetch_map(self, url: str) -> list[list[str]]:
        response: Response = self.api_connector.get(url)
        map_json = response.json().get('goal')
        if map_json is None or self.__is_valid_map_format(map_json) is False:
            raise ValueError(f"Invalid map format: {map_json}")
        return map_json

    def post_astral_object(self, url: str, astral_object: AstralObject, candidate_id: str):
        json = {
            'row': astral_object.row,
            'column': astral_object.column,
            'candidateId': candidate_id,
        }
        self.api_connector.post(url, json=json)

    def __is_valid_map_format(self, map_json: dict) -> bool:
        if not isinstance(map_json, list):
            return False
        for inner in map_json:
            if not isinstance(inner, list):
                return False
            for item in inner:
                if not isinstance(item, str):
                    return False
        return True
