# Megaverse
Megaverse Challenge for Crossmint.
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
Change variables with your data.

## Run code

```bash
python megaverse.py
```
