# Megaverse
Megaverse Challenge for Crossmint. It consists:
- Gets a goal megaverse map from Crossmint API
- Process astral objects from the goal megaverse map
- Create astral objects sending data to Crossmint API
- Delete astral objects in case that you get some error in the creation process

This project uses Python 3.11 with a virtual environment to keep dependencies isolated.

## Requirements
 - Python 3.11 [https://www.python.org/downloads/release](https://www.python.org/downloads/release)
 - `pip` updated.

## Setup

1. Clone repository

```bash
git clone <repo>
cd megaverse
```

2. Create virtual environment

```bash
python3.11 -m venv venv
```

3. Activate virtual env
- macOS/Linux
```bash
source venv/bin/activate
```

- windows
```powershell
venv\Scripts\Activate.ps1
```

4. Install dependencies
```bash
pip install -r requirements.txt
```

5. Copy .env.example to .env
```bash
cp .env.example .env
```
IMPORTANT: Change variables with your correct data. (API must be changed for the correct one)

## Run code

### Create megaverse app
This command will get the goal map, process astral objects and create them to get your megaverse map.
In case of error, all the astral objects were saved in "/resources/multiple_data.json" file to delete it. 
(NOTE: To delete astral objects created you have to use "delete" command)

```bash
python megaverse.py create
```
### Delete megaverse app
This command deletes all the astral objects that were created before, and they were saved in "/resources/multiple_data.json" file.

```bash
python megaverse.py delete
```

## Run unit tests
```bash
python -m unittest
```