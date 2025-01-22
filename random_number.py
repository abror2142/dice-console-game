import secrets


class RandomNumberGenerator:
    def __init__(self, limit):
        self.limit = limit

    def generate(self):
        s = secrets.randbelow(self.limit)
        return s