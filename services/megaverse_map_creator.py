import os

from dotenv import load_dotenv

from domain.factories.astral_object_factory import AstralObjectFactory
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
        self.set_shape()
        print("Megaverse Map created")

    def get_goal_map(self):
        print("Getting Goal Map")

        url: str = self.GOAL_MAP_URL.format(url=self.MEGAVERSE_URL, candidate_id=self.CANDIDATE_ID)
        # self.map = [['SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE'], ['SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE'], ['SPACE', 'SPACE', 'POLYANET', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'POLYANET', 'SPACE', 'SPACE'], ['SPACE', 'SPACE', 'SPACE', 'POLYANET', 'SPACE', 'SPACE', 'SPACE', 'POLYANET', 'SPACE', 'SPACE', 'SPACE'], ['SPACE', 'SPACE', 'SPACE', 'SPACE', 'POLYANET', 'SPACE', 'POLYANET', 'SPACE', 'SPACE', 'SPACE', 'SPACE'], ['SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'POLYANET', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE'], ['SPACE', 'SPACE', 'SPACE', 'SPACE', 'POLYANET', 'SPACE', 'POLYANET', 'SPACE', 'SPACE', 'SPACE', 'SPACE'], ['SPACE', 'SPACE', 'SPACE', 'POLYANET', 'SPACE', 'SPACE', 'SPACE', 'POLYANET', 'SPACE', 'SPACE', 'SPACE'], ['SPACE', 'SPACE', 'POLYANET', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'POLYANET', 'SPACE', 'SPACE'], ['SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE'], ['SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE', 'SPACE']]
        self.map = self.api_service.fetch_map(url)
        print(self.map)

    def create_shape(self):
        print("Creating shape")
        for row_index, row in enumerate(self.map):
            for col_index, cell in enumerate(row):
                astral_object = AstralObjectFactory.create_astral_object(cell, row_index, col_index)
                if astral_object is not None:
                    self.astralObjects.append(astral_object)

        print(self.astralObjects)

    def set_shape(self):
        print("Setting shape")
        for astral_object in self.astralObjects:
            url = self.MEGAVERSE_URL + astral_object.get_plural_name()
            self.api_service.post_astral_object(url=url, astral_object=astral_object, candidate_id=self.CANDIDATE_ID)

