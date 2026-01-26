import tkinter
import tkinter.font

from sprout.font import Font
from sprout.widget import Widget


class TextArea(Widget):

    def __init__(self, parent, width: int, height: int):
        super().__init__(parent)
        self._text = tkinter.Text(
            self._base,
            width=width,
            height=height,
            highlightthickness=0,
        )
        self._text.pack()

    @property
    def background_colour(self):
        """Same as tkinter's bg."""
        if self._text.cget("bg") == self.parent._base.cget("bg"):
            return None
        return self._text.cget("bg")

    @background_colour.setter
    def background_colour(self, background_colour: str | None):
        if background_colour is None:
            self._text.config(bg=self.parent._base.cget("bg"))
        else:
            self._text.config(bg=background_colour)

    @property
    def colour(self):
        """Same as tkinter's fg."""
        return self._text.cget("fg")

    @colour.setter
    def colour(self, colour: str):
        self._text.config(fg=colour)

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
        self._text.config(font=font._tkinter())
