from os import getcwd
from pathlib import Path
import json

BASE_PATH = Path(getcwd())
PASSWORDS_PATH = BASE_PATH / 'passwords.json'
if not PASSWORDS_PATH.exists():
    print("passwords.json not found!")
    exit(-1)

if not PASSWORDS_PATH.exists():
    print("passwords.json not found!")
    PASSWORDS = {}
else:
    PASSWORDS = json.load(open(PASSWORDS_PATH))
    if not isinstance(PASSWORDS, dict):
        print("Error reading passwords.json")
        exit(-1)

    for k, v in PASSWORDS.items():
        if not isinstance(k, str) or not isinstance(v, str):
            print("Error reading passwords.json")
            exit(-1)
