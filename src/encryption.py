import json
import base64

class Encyption:
    def __init__(self, key: bytes = b"HangmanPython2025"):
        self.key = key

    def encode(self, data: dict) -> bytes:
        raw = json.dumps(data).encode("utf-8")
        xored = bytes(
            raw[i] ^ self.key[i % len(self.key)] for i in range(len(raw))
        )
        return base64.b64encode(xored)

    def decode(self, blob: bytes) -> dict:
        xored = base64.b64decode(blob)
        raw = bytes(
            xored[i] ^ self.key[i % len(self.key)] for i in range(len(xored))
        )

        return json.loads(raw.decode("utf-8"))