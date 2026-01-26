import tkinter
import tkinter.font
from typing import Callable

from sprout.font import Font
from sprout.widget import Container, Widget


class TextLabel(Widget):
    """Same as tkinter.Label, but always has text."""

    def __init__(self, parent: Container, text: str):
        super().__init__(parent)
        self._label = tkinter.Label(self._base, text=text)
        self._label.bind("<Button-1>", self._on_click)
        self._label.pack()
        self.font = Font.default()
        self.on_click: Callable[[Widget], None] | None = None

    def _on_click(self, event: tkinter.Event):
        if self.on_click is None:
            return
        self.on_click(self)

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

    @property
    def text(self) -> str:
        """Same as tkinter's text."""
        return self._label.cget("text")

    @text.setter
    def text(self, text: str):
        self._label.config(text=text)

    @property
    def wraplength(self) -> int:
        """Same as tkinter's wraplength."""
        return self._label.cget("wraplength")

    @wraplength.setter
    def wraplength(self, wraplength: int):
        self._label.config(wraplength=wraplength)
