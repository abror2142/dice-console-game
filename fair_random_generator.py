import hmac, hashlib, secrets

from random_number import RandomNumberGenerator


class FairRandomGenerator:
    key = None
    hmac_value = None
    random_number = None

    def __init__(self, limit):
        self.limit = limit
        self.key = secrets.token_hex(32)
        # Assign random number to instance
        random_number_generator = RandomNumberGenerator(self.limit)
        self.random_number = random_number_generator.generate()

    def sign_number(self):
        self.hmac_value = hmac.digest(
            self.key.encode('utf-8'),
            str(self.random_number).encode('utf-8'),
            hashlib.sha3_256
        ).hex()

    def generate(self):
        self.sign_number()

        # Print info about hmac address
        print(f"I selected a random value in the range 0...{self.limit-1}")
        print(f"(HMAC={self.hmac_value}).")

        credentials = {
            "hmac": self.hmac_value,
            "key": self.key,
            "value": self.random_number
        }
        return credentials