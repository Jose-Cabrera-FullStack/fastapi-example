import re
import random
import string


class DebtDomain:

    @staticmethod
    def generate_operation_identifier(length=16):
        characters = string.ascii_letters + string.digits + "-"
        return ''.join(random.choice(characters) for _ in range(length))

    @staticmethod
    def validate_operation_identifier(identifier):
        pattern = r'^[A-Za-z0-9-]{16}$'
        return bool(re.match(pattern, identifier))
