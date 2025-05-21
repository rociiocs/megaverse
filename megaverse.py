import argparse

from dotenv import load_dotenv

from application.create_megaverse_use_case import CreateMegaverseMapUseCase
from application.delete_megaverse_use_case import DeleteMegaverseMapUseCase
from infrastructure.container import Container

load_dotenv()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Megaverse Map CLI")
    parser.add_argument(
        "action",
        choices=["create", "delete"],
        help="Action to perform on the megaverse map"
    )

    args = parser.parse_args()

    container = Container()

    if args.action == "create":
        create_megaverse_use_case: CreateMegaverseMapUseCase = container.create_megaverse_use_case()
        create_megaverse_use_case.create_map()

    elif args.action == "delete":
        delete_megaverse_use_case: DeleteMegaverseMapUseCase = container.delete_megaverse_use_case()
        delete_megaverse_use_case.delete_map()
