import json
import os

from requests import Response

from domain.models.astral_object import AstralObject
from domain.repositories.map_repository import MapRepository
from infrastructure.astral_object_adapter import AstralObjectAdapter
from infrastructure.common.http_client import HttpClient


class ApiMapRepository(MapRepository):
    ASTRAL_OBJECTS_MAPPER_URL: dict = {}

    def __init__(
            self,
            http_client: HttpClient,
            astral_object_adapter: AstralObjectAdapter,
            candidate_id: str,
            goal_map_url: str,
            cometh_url: str,
            polyanet_url: str,
            soloon_url: str
    ) -> None:
        self.http_client = http_client
        self.astral_object_adapter = astral_object_adapter
        self.candidate_id = candidate_id
        self.goal_map_url = goal_map_url
        self.cometh_url = cometh_url
        self.polyanet_url = polyanet_url
        self.soloon_url = soloon_url

        self.ASTRAL_OBJECTS_MAPPER_URL = {
            "Cometh": self.cometh_url,
            "Polyanet": self.polyanet_url,
            "Soloon": self.soloon_url,
        }

    def fetch_astral_objects(self) -> list[AstralObject]:
        url: str = self.goal_map_url.format(candidate_id=self.candidate_id)

        response: Response = self.http_client.get(url)

        map_json = response.json().get('goal')

        if map_json is None or self.__is_valid_map_format(map_json) is False:
            raise ValueError(f"Invalid map format: {map_json}")

        astral_objects: list[AstralObject] = self.astral_object_adapter.get_list_astral_objects(map_json)

        return astral_objects

    def create_astral_objects(self, astral_objects: list[AstralObject]) -> None:
        astral_objects_created: list[dict] = []
        for astral_object in astral_objects:
            url = self.ASTRAL_OBJECTS_MAPPER_URL.get(astral_object.__class__.__name__)
            print(url)
            data_json: dict = astral_object.to_dict()
            data_json['candidateId'] = self.candidate_id

            request_data = {"url": url, "json": data_json}
            print(f"Creating {request_data}")

            try:
                self.http_client.post_retry(url=url, json=data_json)
            except Exception as e:
                print(astral_objects_created)
                self.__save_data_list(astral_objects_created)
                raise e

            astral_objects_created.append(request_data)
        self.__save_data_list(astral_objects_created)

    def delete_megaverse_map(self) -> None:
        data_list = self.__get_data_list()
        for data in data_list:
            print(f"Deleting {data}")
            self.http_client.delete_retry(url=data["url"], json=data["json"])

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

    def __save_data_list(self, data_list: list[dict]) -> None:
        dir_path = "resources"
        file_path = os.path.join(dir_path, "multiple_data.json")

        os.makedirs(dir_path, exist_ok=True)

        print(f"Saving data list in {file_path}")
        with open(file_path, "w") as f:
            json.dump(data_list, f, indent=4)

    def __get_data_list(self) -> list[dict]:
        try:
            with open("resources/multiple_data.json", "r") as f:
                data_list = json.load(f)
        except FileNotFoundError:
            print("No data file found")
            data_list = []

        return data_list
