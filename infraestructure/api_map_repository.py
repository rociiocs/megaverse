import os

from dotenv import load_dotenv
from requests import Response

from domain.models.astral_object import AstralObject
from domain.repositories.map_repository import MapRepository
from infraestructure.astral_object_adapter import AstralObjectAdapter
from infraestructure.common.api_connector import ApiConnector

load_dotenv()


class ApiMapRepository(MapRepository):
    MEGAVERSE_URL = os.getenv("MEGAVERSE_URL")
    CANDIDATE_ID = os.getenv("CANDIDATE_ID")
    GOAL_MAP_URL = "{url}map/{candidate_id}/goal"

    ASTRAL_OBJECTS_URL = {
        "Cometh": "{url}comeths",
        "Polyanet": "{url}polyanets",
        "Soloon": "{url}soloons"
    }

    def __init__(self):
        self.api_connector = ApiConnector()
        self.astral_object_adapter = AstralObjectAdapter()

    def fetch_astral_objects(self) -> list[AstralObject]:
        url: str = self.GOAL_MAP_URL.format(url=self.MEGAVERSE_URL, candidate_id=self.CANDIDATE_ID)

        response: Response = self.api_connector.get(url)

        map_json = response.json().get('goal')
        # map_json = [
        #     ['RED_SOLOON', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE',
        #      'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE',
        #      'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE'],
        #     ['SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'RIGHT_COMETH', 'SPACE', 'SPACE', 'SPACE',
        #      'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE',
        #      'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE'],
        #     ['SPACE', 'SPACE', 'POLYANET', 'POLYANET', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE',
        #      'SPACE', 'SPACE', 'UP_COMETH', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE',
        #      'SPACE', 'POLYANET', 'POLYANET', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE'],
        #     ['SPACE', 'SPACE', 'POLYANET', 'SPACE', 'POLYANET', 'POLYANET', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE',
        #      'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'WHITE_SOLOON',
        #      'POLYANET', 'POLYANET', 'SPACE', 'POLYANET', 'SPACE', 'SPACE', 'LEFT_COMETH', 'SPACE', 'SPACE'],
        #     ['SPACE', 'SPACE', 'SPACE', 'POLYANET', 'SPACE', 'BLUE_SOLOON', 'POLYANET', 'POLYANET', 'PURPLE_SOLOON',
        #      'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'LEFT_COMETH', 'SPACE', 'SPACE', 'POLYANET',
        #      'POLYANET', 'SPACE', 'SPACE', 'POLYANET', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'RIGHT_COMETH'],
        #     ['SPACE', 'SPACE', 'SPACE', 'POLYANET', 'SPACE', 'SPACE', 'WHITE_SOLOON', 'SPACE', 'POLYANET', 'POLYANET',
        #      'SPACE', 'SPACE', 'DOWN_COMETH', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'POLYANET', 'POLYANET', 'BLUE_SOLOON',
        #      'SPACE', 'SPACE', 'SPACE', 'POLYANET', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE'],
        #     ['SPACE', 'SPACE', 'SPACE', 'SPACE', 'POLYANET', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'POLYANET',
        #      'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'POLYANET', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE',
        #      'POLYANET', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE'],
        #     ['SPACE', 'SPACE', 'SPACE', 'SPACE', 'POLYANET', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'POLYANET',
        #      'SPACE', 'SPACE', 'SPACE', 'SPACE', 'RED_SOLOON', 'POLYANET', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE',
        #      'POLYANET', 'PURPLE_SOLOON', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE'],
        #     ['SPACE', 'SPACE', 'SPACE', 'SPACE', 'WHITE_SOLOON', 'POLYANET', 'SPACE', 'SPACE', 'SPACE', 'SPACE',
        #      'BLUE_SOLOON', 'POLYANET', 'SPACE', 'SPACE', 'SPACE', 'POLYANET', 'SPACE', 'SPACE', 'SPACE', 'SPACE',
        #      'SPACE', 'POLYANET', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE'],
        #     ['SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'POLYANET', 'PURPLE_SOLOON', 'SPACE', 'SPACE', 'SPACE',
        #      'SPACE', 'POLYANET', 'RED_SOLOON', 'SPACE', 'SPACE', 'POLYANET', 'SPACE', 'SPACE', 'SPACE', 'SPACE',
        #      'SPACE', 'POLYANET', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'UP_COMETH', 'SPACE', 'SPACE'],
        #     ['SPACE', 'SPACE', 'UP_COMETH', 'SPACE', 'SPACE', 'SPACE', 'POLYANET', 'POLYANET', 'SPACE', 'SPACE',
        #      'SPACE', 'SPACE', 'POLYANET', 'SPACE', 'POLYANET', 'SPACE', 'SPACE', 'SPACE', 'PURPLE_SOLOON', 'POLYANET',
        #      'POLYANET', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE'],
        #     ['SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'BLUE_SOLOON', 'POLYANET', 'POLYANET',
        #      'SPACE', 'SPACE', 'POLYANET', 'SPACE', 'POLYANET', 'SPACE', 'SPACE', 'POLYANET', 'POLYANET', 'SPACE',
        #      'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE'],
        #     ['SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'POLYANET',
        #      'POLYANET', 'SPACE', 'POLYANET', 'SPACE', 'POLYANET', 'POLYANET', 'SPACE', 'SPACE', 'SPACE', 'SPACE',
        #      'SPACE', 'SPACE', 'SPACE', 'SPACE', 'LEFT_COMETH', 'SPACE', 'SPACE', 'DOWN_COMETH', 'SPACE'],
        #     ['SPACE', 'SPACE', 'SPACE', 'SPACE', 'RIGHT_COMETH', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE',
        #      'SPACE', 'POLYANET', 'POLYANET', 'POLYANET', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE',
        #      'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE'],
        #     ['SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'WHITE_SOLOON',
        #      'POLYANET', 'POLYANET', 'SPACE', 'POLYANET', 'SPACE', 'POLYANET', 'POLYANET', 'BLUE_SOLOON', 'SPACE',
        #      'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE'],
        #     ['SPACE', 'LEFT_COMETH', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'POLYANET', 'POLYANET',
        #      'SPACE', 'SPACE', 'POLYANET', 'SPACE', 'POLYANET', 'SPACE', 'SPACE', 'POLYANET', 'POLYANET',
        #      'WHITE_SOLOON', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'RIGHT_COMETH', 'SPACE', 'SPACE',
        #      'SPACE'],
        #     ['SPACE', 'SPACE', 'SPACE', 'DOWN_COMETH', 'SPACE', 'SPACE', 'POLYANET', 'POLYANET', 'BLUE_SOLOON', 'SPACE',
        #      'SPACE', 'SPACE', 'POLYANET', 'SPACE', 'POLYANET', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'POLYANET',
        #      'POLYANET', 'BLUE_SOLOON', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE'],
        #     ['SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'POLYANET', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE',
        #      'POLYANET', 'SPACE', 'SPACE', 'PURPLE_SOLOON', 'POLYANET', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE',
        #      'POLYANET', 'SPACE', 'SPACE', 'UP_COMETH', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE'],
        #     ['SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'POLYANET', 'PURPLE_SOLOON', 'SPACE', 'SPACE', 'SPACE',
        #      'SPACE', 'POLYANET', 'SPACE', 'SPACE', 'SPACE', 'POLYANET', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE',
        #      'POLYANET', 'RED_SOLOON', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE'],
        #     ['SPACE', 'SPACE', 'SPACE', 'SPACE', 'POLYANET', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'POLYANET',
        #      'WHITE_SOLOON', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'POLYANET', 'SPACE', 'SPACE', 'SPACE', 'SPACE',
        #      'SPACE', 'POLYANET', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE'],
        #     ['RIGHT_COMETH', 'SPACE', 'SPACE', 'SPACE', 'POLYANET', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE',
        #      'POLYANET', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'POLYANET', 'SPACE', 'SPACE', 'SPACE', 'SPACE',
        #      'SPACE', 'POLYANET', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE'],
        #     ['SPACE', 'SPACE', 'SPACE', 'POLYANET', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'POLYANET', 'POLYANET',
        #      'RED_SOLOON', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'WHITE_SOLOON', 'POLYANET', 'POLYANET',
        #      'PURPLE_SOLOON', 'SPACE', 'SPACE', 'SPACE', 'POLYANET', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE',
        #      'SPACE'],
        #     ['SPACE', 'SPACE', 'SPACE', 'POLYANET', 'SPACE', 'RED_SOLOON', 'POLYANET', 'POLYANET', 'BLUE_SOLOON',
        #      'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'LEFT_COMETH', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'POLYANET',
        #      'POLYANET', 'SPACE', 'SPACE', 'POLYANET', 'RED_SOLOON', 'SPACE', 'SPACE', 'DOWN_COMETH', 'SPACE', 'SPACE'],
        #     ['SPACE', 'SPACE', 'POLYANET', 'SPACE', 'POLYANET', 'POLYANET', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE',
        #      'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'POLYANET',
        #      'POLYANET', 'SPACE', 'POLYANET', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE'],
        #     ['SPACE', 'SPACE', 'POLYANET', 'POLYANET', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE',
        #      'SPACE', 'UP_COMETH', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE',
        #      'SPACE', 'POLYANET', 'POLYANET', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE'],
        #     ['SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE',
        #      'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE',
        #      'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE'],
        #     ['SPACE', 'SPACE', 'SPACE', 'DOWN_COMETH', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE',
        #      'SPACE', 'SPACE', 'SPACE', 'SPACE', 'DOWN_COMETH', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE',
        #      'SPACE', 'SPACE', 'SPACE', 'SPACE', 'UP_COMETH', 'SPACE', 'SPACE', 'SPACE'],
        #     ['SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'LEFT_COMETH', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE',
        #      'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE',
        #      'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE'],
        #     ['SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'RIGHT_COMETH',
        #      'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'LEFT_COMETH', 'SPACE',
        #      'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE'],
        #     ['SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE',
        #      'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE',
        #      'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE']]

        if map_json is None or self.__is_valid_map_format(map_json) is False:
            raise ValueError(f"Invalid map format: {map_json}")

        astral_objects: list[AstralObject] = self.astral_object_adapter.get_list_astral_objects(map_json)

        return astral_objects

    def create_astral_object(self, astral_object: AstralObject):
        url = self.ASTRAL_OBJECTS_URL.get(astral_object.__class__.__name__).format(url=self.MEGAVERSE_URL)

        json = astral_object.to_dict()
        json['candidateId'] = self.CANDIDATE_ID

        print(f"{url} {json}")

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
