import tkinter
import tkinter.font
from typing import Callable

from sprout.font import Font
from sprout.widget import Widget


class Entry(Widget):
    """Same as tkinter.Entry."""

    def __init__(self, parent):
        super().__init__(parent)
        self._variable = tkinter.StringVar(self._base)
        self._variable.trace_add("write", self._on_write)
        self._entry = tkinter.Entry(self._base, textvariable=self._variable)
        self._entry.pack()
        self.font = Font.default()
        self.on_write: Callable[[Widget], None] | None = None

    def _on_write(self, *args):
        if self.on_write is None:
            return
        self.on_write(self)

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
        self._entry.config(font=font._tkinter())

    @property
    def value(self):
        """Same as tkinter's value."""
        return self._entry.get()

    @value.setter
    def value(self, value: str):
        self._variable.set(value)

    @property
    def width(self):
        """Same as tkinter's width."""
        return self._entry.cget("width")

    @width.setter
    def width(self, width: int):
        self._entry.config(width=width)
