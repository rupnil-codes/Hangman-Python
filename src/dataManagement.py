import os
from src import config as cog
from src.encryption import Encyption

encryption = Encyption(
    key = cog.SECRET_KEY_BYTES
)

appdata = os.environ.get("APPDATA")
base_dir = os.path.join(appdata, "HangmanPython", "data")
user_file = os.path.join(base_dir, "user.json")

def read(file: str) -> dict:
    with open(file, "rb") as file:
        raw = file.read()
        return encryption.decode(raw)

def write(file: str, data: dict):
    os.makedirs(base_dir, exist_ok=True)
    with open(file, "wb") as file:
        file.write(encryption.encode(data))

def load_data_safe(
    path: str,
    default_data: dict
) -> dict:
    try:
        with open(path, "rb") as f:
            raw = f.read()
            if not raw:
                raise ValueError("Empty file")

            data_ = encryption.decode(raw)

            # Check if data is intact (not manipulated/corrupted)
            if not isinstance(data_, dict):
                raise ValueError("Decoded data is not a dict")

            return data_

    except Exception:
        # scorch earth
        try:
            os.remove(path)
        except FileNotFoundError:
            pass

        data_ = default_data.copy()
        write(path, data_)

        return data_
