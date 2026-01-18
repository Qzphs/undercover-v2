from game.game import Game

import sprout as s

from ui.constants import PLAYER_LIMIT, PLAYER_SPACING, PLAYER_X, PLAYER_Y
from ui.navigation import Navigation
from ui.spoiler import Spoiler


class WordsScreen(s.Screen):

    def __init__(self, parent: s.Application, game: Game):
        super().__init__(parent)
        self.game = game

        self.player_labels = [s.TextLabel(self, "") for _ in range(PLAYER_LIMIT)]
        self.word_spoilers = [Spoiler(self, "") for _ in range(PLAYER_LIMIT)]

        self.navigation = Navigation(self)
        self.navigation.words_button.font = s.Font("Sans Serif", 12, bold=True)
        self.navigation.place(910, 50, anchor=s.NE)

    def update(self):
        for i in range(PLAYER_LIMIT):
            label = self.player_labels[i]
            spoiler = self.word_spoilers[i]
            if i >= len(self.game.players):
                label.place(
                    x=s.OFFSCREEN,
                    y=PLAYER_Y + i * PLAYER_SPACING,
                )
                spoiler.place(
                    x=s.OFFSCREEN + 150,
                    y=PLAYER_Y + i * PLAYER_SPACING,
                )
                continue
            label.text = self.game.players[i]
            label.place(
                x=PLAYER_X,
                y=PLAYER_Y + i * PLAYER_SPACING,
            )
            spoiler.revealed = False
            spoiler.text = self.game.words[i]
            spoiler.place(
                x=PLAYER_X + 150,
                y=PLAYER_Y + i * PLAYER_SPACING,
            )
