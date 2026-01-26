from game.game import Game

import sprout as s

from ui.constants import (
    DEFAULT_FONT,
    PLAYER_LIMIT,
    PLAYER_SPACING,
    PLAYER_X,
    PLAYER_Y,
)
from ui.navigation import Navigation


WORDS_X = 580
SPOILER_WIDTH = 200
SPOILER_HEIGHT = 25


class VotingScreen(s.Screen):

    def __init__(self, parent: s.Application, game: Game):
        super().__init__(parent)
        self.game = game

        self.player_labels = [s.TextLabel(self, "") for _ in range(PLAYER_LIMIT)]
        for label in self.player_labels:
            label.font = DEFAULT_FONT

        self.role_spoilers = [
            s.Spoiler(self, "", SPOILER_WIDTH, SPOILER_HEIGHT)
            for _ in range(PLAYER_LIMIT)
        ]
        for spoiler in self.role_spoilers:
            spoiler.font = DEFAULT_FONT

        self.c_word_label = s.TextLabel(self, "civilian word")
        self.c_word_label.font = DEFAULT_FONT
        self.c_word_label.place(WORDS_X, 75, anchor=s.N)
        self.c_word_spoiler = s.Spoiler(self, "", SPOILER_WIDTH, SPOILER_HEIGHT)
        self.c_word_spoiler.font = DEFAULT_FONT
        self.c_word_spoiler.place(WORDS_X, 125, anchor=s.N)

        self.u_word_label = s.TextLabel(self, "undercover word")
        self.u_word_label.font = DEFAULT_FONT
        self.u_word_label.place(WORDS_X, 275, anchor=s.N)
        self.u_word_spoiler = s.Spoiler(self, "", SPOILER_WIDTH, SPOILER_HEIGHT)
        self.u_word_spoiler.font = DEFAULT_FONT
        self.u_word_spoiler.place(WORDS_X, 325, anchor=s.N)

        self.navigation = Navigation(self)
        self.navigation.voting_button.emphasise()
        self.navigation.place(910, 50, anchor=s.NE)

    def update(self):
        for i in range(PLAYER_LIMIT):
            label = self.player_labels[i]
            spoiler = self.role_spoilers[i]
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
            spoiler.back_text = self.game.roles[i].value
            spoiler.place(
                x=PLAYER_X + 150,
                y=PLAYER_Y + i * PLAYER_SPACING,
            )
        self.c_word_spoiler.back_text = self.game.c_word
        self.u_word_spoiler.back_text = self.game.u_word
