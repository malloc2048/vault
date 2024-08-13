import json


class Users:
    def __init__(self):
        self._users = [
            "available",
            "jim",
            "josh",
            "ryan",
            "james",
            "tyrel",
            "andrew",
            "walter"
        ]

    @property
    def users(self):
        return self._users
