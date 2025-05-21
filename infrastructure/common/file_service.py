import json
import os


class FileService:
    def save_data_list(self, data_list: list[dict], file_path: str) -> None:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)

        print(f"Saving data list in {file_path}")
        with open(file_path, "w") as f:
            json.dump(data_list, f, indent=4)

    def get_data_list(self, file_path: str) -> list[dict]:
        try:
            with open(file_path, "r") as f:
                data_list = json.load(f)
        except FileNotFoundError:
            print("No data file found")
            data_list = []

        return data_list
