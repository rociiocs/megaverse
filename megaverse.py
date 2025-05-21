import argparse

from dotenv import load_dotenv

from application.create_megaverse_use_case import CreateMegaverseMapUseCase
from application.delete_megaverse_use_case import DeleteMegaverseMapUseCase

load_dotenv()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Megaverse Map CLI")
    parser.add_argument(
        "action",
        choices=["create", "delete"],
        help="Action to perform on the megaverse map"
    )

    args = parser.parse_args()

    if args.action == "create":
        CreateMegaverseMapUseCase().create_map()
    elif args.action == "delete":
        DeleteMegaverseMapUseCase().delete_map()
