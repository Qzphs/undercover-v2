import random

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


class QuestionsScreen(s.Screen):

    def __init__(self, parent: s.Application, game: Game):
        super().__init__(parent)
        self.game = game
        self.question_order: list[str] = []

        self.player_labels = [s.TextLabel(self, "") for _ in range(PLAYER_LIMIT)]
        for label in self.player_labels:
            label.font = DEFAULT_FONT

        self.reroll_button = s.TextLabel(self, "(reroll question order)")
        self.reroll_button.font = DEFAULT_FONT
        self.reroll_button.on_click = self._reroll_question_order
        self.reroll_button.place(50, 550, anchor=s.SW)

        self.notepad = s.TextArea(self, 70, 30)
        self.notepad.place(PLAYER_X + 175, PLAYER_Y)

        self.navigation = Navigation(self)
        self.navigation.questions_button.emphasise()
        self.navigation.place(910, 50, anchor=s.NE)

    def _reroll_question_order(self, source: s.TextLabel):
        self.update()

    def update(self):
        self.question_order.clear()
        self.question_order.extend(self.game.players)
        random.shuffle(self.question_order)
        for i in range(PLAYER_LIMIT):
            label = self.player_labels[i]
            if i >= len(self.game.players):
                label.place(
                    x=s.OFFSCREEN,
                    y=PLAYER_Y + i * PLAYER_SPACING,
                )
                continue
            label.text = f"{i+1}. {self.question_order[i]}"
            label.place(
                x=PLAYER_X,
                y=PLAYER_Y + i * PLAYER_SPACING,
            )
