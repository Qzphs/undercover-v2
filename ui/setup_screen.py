from typing import Callable

from game.files import FILES
from game.setup import Setup

import sprout as s

from ui.constants import (
    DEFAULT_FONT,
    PLAYER_LIMIT,
    PLAYER_SPACING,
    PLAYER_X,
    PLAYER_Y,
)
from ui.navigation import Navigation


OPTIONS_X = 400


class SetupScreen(s.Screen):

    def __init__(self, parent: s.Application):
        super().__init__(parent)
        self.setup = Setup()

        self.player_entries = [s.Entry(self) for _ in range(PLAYER_LIMIT)]
        for entry in self.player_entries:
            entry.font = DEFAULT_FONT
            entry.width = 12
            entry.on_write = self._on_entry_write

        self.delete_buttons = [s.TextLabel(self, "(-)") for _ in range(PLAYER_LIMIT)]
        for button in self.delete_buttons:
            button.font = DEFAULT_FONT
            button.on_click = self._remove_player

        self.add_button = s.TextLabel(self, "(add player)")
        self.add_button.font = DEFAULT_FONT
        self.add_button.on_click = self._add_player
        self.add_button.place(x=50, y=550, anchor=s.SW)

        self.file_label = s.TextLabel(self, "use file:")
        self.file_label.font = DEFAULT_FONT
        self.file_label.place(OPTIONS_X, 50)
        self.file_dropdown = s.Dropdown(self, [file.name for file in FILES])
        self.file_dropdown.font = DEFAULT_FONT
        self.file_dropdown.on_write = self._on_dropdown_write
        self.file_dropdown.place(OPTIONS_X, 80)

        self.n_words_label = s.TextLabel(self, f"{self.setup.file.n_pairs} set(s) left")
        self.n_words_label.font = s.Font("Sans Serif", 10, italic=True)
        self.n_words_label.place(OPTIONS_X, 110)

        self.undercover_selector = NumberSelector(self, "undercovers:")
        self.undercover_selector.value = self.setup.undercovers
        self.undercover_selector.on_decrease = self._decrease_undercovers
        self.undercover_selector.on_increase = self._increase_undercovers
        self.undercover_selector.place(OPTIONS_X, 200)

        self.mr_white_selector = NumberSelector(self, "mr. whites:")
        self.mr_white_selector.value = self.setup.mr_whites
        self.mr_white_selector.on_decrease = self._decrease_mr_whites
        self.mr_white_selector.on_increase = self._increase_mr_whites
        self.mr_white_selector.place(OPTIONS_X, 300)

        self.start_button = s.TextLabel(self, "(start)")
        self.start_button.font = DEFAULT_FONT

        self.navigation = Navigation(self)
        self.navigation.setup_button.emphasise()
        self.navigation.place(910, 50, anchor=s.NE)

        self._update_player_widgets()

    def _add_player(self, source: s.TextLabel):
        self.setup.players.append("")
        self._update_player_widgets()
        self._update_start_button()

    def _remove_player(self, source: s.TextLabel):
        index = self.delete_buttons.index(source)
        self.setup.players.pop(index)
        self._update_player_widgets()
        self._update_start_button()

    def _decrease_undercovers(self, source: s.Widget):
        if self.setup.undercovers <= 0:
            return
        self.setup.undercovers -= 1
        self.undercover_selector.value = str(self.setup.undercovers)
        self._update_start_button()

    def _increase_undercovers(self, source: s.Widget):
        self.setup.undercovers += 1
        self.undercover_selector.value = str(self.setup.undercovers)
        self._update_start_button()

    def _decrease_mr_whites(self, source: s.Widget):
        if self.setup.mr_whites <= 0:
            return
        self.setup.mr_whites -= 1
        self.mr_white_selector.value = str(self.setup.mr_whites)
        self._update_start_button()

    def _increase_mr_whites(self, source: s.Widget):
        self.setup.mr_whites += 1
        self.mr_white_selector.value = str(self.setup.mr_whites)
        self._update_start_button()

    def _on_dropdown_write(self, source: s.Dropdown):
        file = next(file for file in FILES if file.name == source.value)
        self.setup.file = file
        self.update_n_words_label()
        self._update_start_button()

    def _on_entry_write(self, source: s.Entry):
        index = self.player_entries.index(source)
        if index >= len(self.setup.players):
            return
        self.setup.players[index] = source.value

    def _update_player_widgets(self):
        for i in range(PLAYER_LIMIT):
            entry = self.player_entries[i]
            button = self.delete_buttons[i]
            if i >= len(self.setup.players):
                entry.place(
                    x=s.OFFSCREEN,
                    y=PLAYER_Y + i * PLAYER_SPACING,
                )
                button.place(
                    x=s.OFFSCREEN,
                    y=PLAYER_Y + i * PLAYER_SPACING,
                )
                continue
            entry.value = self.setup.players[i]
            entry.place(
                x=PLAYER_X,
                y=PLAYER_Y + i * PLAYER_SPACING,
            )
            button.place(
                x=PLAYER_X + 150,
                y=PLAYER_Y + i * PLAYER_SPACING,
            )

    def _update_start_button(self):
        if self.setup.can_start:
            self.start_button.place(OPTIONS_X, 550, anchor=s.SW)
        else:
            self.start_button.place(s.OFFSCREEN, 550)

    def update_n_words_label(self):
        self.n_words_label.text = f"{self.setup.file.n_pairs} set(s) left"


class NumberSelector(s.Frame):

    def __init__(self, parent: s.Container, name: str):
        super().__init__(parent, 100, 60)

        self.name_label = s.TextLabel(self, text=name)
        self.name_label.font = DEFAULT_FONT
        self.name_label.place(50, 0, anchor=s.N)

        self.decrease_button = s.TextLabel(self, "(-)")
        self.decrease_button.font = DEFAULT_FONT
        self.decrease_button.on_click = self._decrease
        self.decrease_button.place(0, 30, anchor=s.NW)

        self.value_label = s.TextLabel(self, "0")
        self.value_label.font = DEFAULT_FONT
        self.value_label.place(50, 30, anchor=s.N)

        self.increase_button = s.TextLabel(self, "(+)")
        self.increase_button.font = DEFAULT_FONT
        self.increase_button.on_click = self._increase
        self.increase_button.place(100, 30, anchor=s.NE)

        self.on_decrease: Callable[[s.Widget], None] | None = None
        self.on_increase: Callable[[s.Widget], None] | None = None

    @property
    def value(self):
        return int(self.value_label.text)

    @value.setter
    def value(self, value: int):
        self.value_label.text = str(value)

    def _decrease(self, source: s.TextLabel):
        if self.on_decrease is None:
            return
        self.on_decrease(self)

    def _increase(self, source: s.TextLabel):
        if self.on_increase is None:
            return
        self.on_increase(self)
