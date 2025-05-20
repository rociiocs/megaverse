from services.megaverse_map_creator import MegaverseMapCreator
from dotenv import load_dotenv

load_dotenv()

if __name__ == "__main__":
    MegaverseMapCreator().create_map()
