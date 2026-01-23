import sprout as s

from ui.constants import DEFAULT_FONT


class Spoiler(s.Frame):

    def __init__(self, parent, text, centered: bool = False):
        super().__init__(parent, 200, 25)
        self.text = text
        self._revealed = False

        self.on_click = self._toggle_revealed

        self._text_label = s.TextLabel(self, "(click to reveal)")
        self._text_label.font = DEFAULT_FONT
        self._text_label.on_click = self._toggle_revealed
        if centered:
            self._text_label.place(100, 0, anchor=s.N)
        else:
            self._text_label.place(0, 0)

    @property
    def revealed(self):
        return self._revealed

    @revealed.setter
    def revealed(self, revealed: bool):
        self._revealed = revealed
        if self._revealed:
            self._text_label.text = self.text
        else:
            self._text_label.text = "(click to reveal)"

    def _toggle_revealed(self, source: "Spoiler | s.TextLabel"):
        self.revealed = not self.revealed
