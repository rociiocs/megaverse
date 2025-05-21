from dotenv import load_dotenv

from application.create_megaverse_use_case import CreateMegaverseMapUseCase

load_dotenv()

if __name__ == "__main__":
    CreateMegaverseMapUseCase().create_map()
