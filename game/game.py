from game.role import Role
from game.setup import Setup


class Game:

    def __init__(self):
        self.players: list[str] = []
        self.roles: list[Role] = []
        self.words: list[str] = []
        self.c_word: str = ""
        self.u_word: str = ""

    def reset(self, setup: Setup):
        if setup.file.n_pairs == 0:
            raise Exception("cannot start game using empty file")
        self.players.clear()
        self.players.extend(setup.players)
        self.roles.clear()
        self.roles.extend(setup.random_roles())
        self.c_word, self.u_word = setup.file.get()
        self.words.clear()
        for role in self.roles:
            if role == Role.CIVILIAN:
                self.words.append(self.c_word)
            elif role == Role.UNDERCOVER:
                self.words.append(self.u_word)
            elif role == Role.MR_WHITE:
                self.words.append("(you are mr. white)")
