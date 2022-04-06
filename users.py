from util import readFile
from constants import DELIM1, DELIM2


class Users:
    _users = list()

    @classmethod
    def addToUsers(cls, userId):
        cls._users.append(userId)

    @classmethod
    def __sortUsers(cls):
        print("Sorting users...")
        cls._users = list(set(cls._users))
        cls._users = [int(userId) for userId in cls._users]
        cls._users.sort()

    @classmethod
    def outputUsers(cls):
        cls.__sortUsers()
        print("Writing users...")
        with open("./out/users.txt", "w") as f:
            for user in cls._users:
                f.write(f"{user}\n")
