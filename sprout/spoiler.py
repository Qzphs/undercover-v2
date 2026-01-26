import tkinter
import tkinter.font

from sprout.constants import N
from sprout.font import Font
from sprout.widget import Container, Widget


class Spoiler(Widget):
    """Custom sprout widget based on tkinter.Label."""

    def __init__(self, parent: Container, text: str, width: int, height: int):
        super().__init__(parent)
        self._back_text = text
        self._front_text = "(click to reveal)"
        self._revealed = False

        self._base.config(width=width, height=height)
        self._base.bind("<Button-1>", self._toggle_revealed)

        self._label = tkinter.Label(self._base)
        self._label.config(text=self._front_text)
        self._label.config(wraplength=width)
        self._label.bind("<Button-1>", self._toggle_revealed)
        self._label.place(x=width // 2, y=0, anchor=N)

        self.font = Font.default()

    def _toggle_revealed(self, source: "Spoiler"):
        self.revealed = not self.revealed

    def _update(self):
        if self._revealed:
            self._label.config(text=self._back_text)
        else:
            self._label.config(text=self._front_text)

    @property
    def back_text(self):
        """The text displayed when this spoiler is revealed."""
        return self._back_text

    @back_text.setter
    def back_text(self, back_text: str):
        self._back_text = back_text
        self._update()

    @property
    def front_text(self):
        """The text displayed when this spoiler is unrevealed."""
        return self._front_text

    @front_text.setter
    def front_text(self, front_text: str):
        self._front_text = front_text
        self._update()

    @property
    def revealed(self):
        """Whether this spoiler is revealed."""
        return self._revealed

    @revealed.setter
    def revealed(self, revealed: bool):
        self._revealed = revealed
        self._update()

    @property
    def background_colour(self):
        """Same as tkinter's bg."""
        if self._base.cget("bg") == self.parent._base.cget("bg"):
            return None
        return self._base.cget("bg")

    @background_colour.setter
    def background_colour(self, background_colour: str | None):
        if background_colour is None:
            background_colour = self.parent._base.cget("bg")
        self._base.config(bg=background_colour)
        self._label.config(bg=background_colour)

    @property
    def colour(self):
        """Same as tkinter's fg."""
        return self._label.cget("fg")

    @colour.setter
    def colour(self, colour: str):
        self._label.config(fg=colour)

    @property
    def font(self):
        """
        Similar to tkinter's font.

        This property is a sprout.Font object, not a tkinter font name.
        """
        return self._font

    @font.setter
    def font(self, font: Font):
        self._font = font
        self._label.config(font=font._tkinter())
