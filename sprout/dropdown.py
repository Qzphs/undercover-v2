import tkinter
import tkinter.font
from typing import Callable

from sprout.font import Font
from sprout.widget import Container, Widget


class Dropdown(Widget):
    """Same as tkinter.OptionMenu."""

    def __init__(self, parent: Container, options: list[str]):
        super().__init__(parent)
        assert len(options) > 0
        self._variable = tkinter.StringVar(self._base)
        self._variable.set(options[0])
        self._variable.trace_add("write", self._on_write)
        self.options = options
        self._dropdown = tkinter.OptionMenu(self._base, self._variable, *options)
        self._dropdown.pack()
        self.font = Font.default()
        self.on_write: Callable[[Widget], None] | None = None

    def _on_write(self, *args):
        if self.on_write is None:
            return
        self.on_write(self)

    @property
    def value(self):
        """Same as tkinter's value."""
        return self._variable.get()

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
        self._dropdown.config(font=font._tkinter())
