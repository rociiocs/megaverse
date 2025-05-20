import os

from dotenv import load_dotenv

from domain.models.astral_object import AstralObject
from services.api_service import ApiService
from services.map_creator import MapCreator

load_dotenv()


class MegaverseMapCreator(MapCreator):
    MEGAVERSE_URL = os.getenv("MEGAVERSE_URL")
    CANDIDATE_ID = os.getenv("CANDIDATE_ID")
    GOAL_MAP_URL = "{url}map/{candidate_id}/goal"

    map: [str, str] = None
    astralObjects: list[AstralObject] = []

    def __init__(self):
        super().__init__()
        self.api_service = ApiService()

    def create_map(self):
        print("Creating Megaverse Map")
        self.get_goal_map()
        self.create_shape()

    def get_goal_map(self):
        url: str = self.GOAL_MAP_URL.format(url=self.MEGAVERSE_URL, candidate_id=self.CANDIDATE_ID)
        # self.map = [['SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE'], ['SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE'], ['SPACE', 'SPACE', 'POLYANET', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'POLYANET', 'SPACE', 'SPACE'], ['SPACE', 'SPACE', 'SPACE', 'POLYANET', 'SPACE', 'SPACE', 'SPACE', 'POLYANET', 'SPACE', 'SPACE', 'SPACE'], ['SPACE', 'SPACE', 'SPACE', 'SPACE', 'POLYANET', 'SPACE', 'POLYANET', 'SPACE', 'SPACE', 'SPACE', 'SPACE'], ['SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'POLYANET', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE'], ['SPACE', 'SPACE', 'SPACE', 'SPACE', 'POLYANET', 'SPACE', 'POLYANET', 'SPACE', 'SPACE', 'SPACE', 'SPACE'], ['SPACE', 'SPACE', 'SPACE', 'POLYANET', 'SPACE', 'SPACE', 'SPACE', 'POLYANET', 'SPACE', 'SPACE', 'SPACE'], ['SPACE', 'SPACE', 'POLYANET', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'POLYANET', 'SPACE', 'SPACE'], ['SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE'], ['SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE']]
        self.map = self.api_service.fetch_map(url)
        print(self.map)

    def create_shape(self):
        print("Creating shape")

    def set_shape(self):
        print("Setting shape")
