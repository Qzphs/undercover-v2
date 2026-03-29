import random

from game.files import FILES
from game.role import Role


class Setup:

    def __init__(self):
        self.players: list[str] = []
        self.file = FILES[0]
        self.undercovers = 1
        self.mr_whites = 0

    @property
    def can_start(self):
        return (
            len(self.players) >= 2
            and len(self.players) >= 1 + self.undercovers + self.mr_whites
            and self.file.n_pairs > 0
        )

    def random_roles(self):
        if not self.can_start:
            raise Exception("cannot start on current setup")
        roles: list[Role] = []
        for _ in range(self.undercovers):
            roles.append(Role.UNDERCOVER)
        for _ in range(self.mr_whites):
            roles.append(Role.MR_WHITE)
        while len(roles) < len(self.players):
            roles.append(Role.CIVILIAN)
        random.shuffle(roles)
        return roles
