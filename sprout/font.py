import tkinter.font


class Font:
    """Same as tkinter.font.Font."""

    def __init__(
        self,
        family: str = "Sans Serif",
        size: int = 12,
        bold: bool = False,
        italic: bool = False,
        underline: bool = False,
        strikethrough: bool = False,
    ):
        self.family = family
        self.size = size
        self.bold = bold
        self.italic = italic
        self.underline = underline
        self.strikethrough = strikethrough

    @classmethod
    def default(cls):
        return Font()

    def copy(
        self,
        family: str | None = None,
        size: int | None = None,
        bold: bool | None = None,
        italic: bool | None = None,
        underline: bool | None = None,
        strikethrough: bool | None = None,
    ):
        """
        Create a copy of this font.

        Individual font properties can be changed using the
        corresponding parameter, or default to same as the original if
        left blank.
        """
        if family is None:
            family = self.family
        if size is None:
            size = self.size
        if bold is None:
            bold = self.bold
        if italic is None:
            italic = self.italic
        if underline is None:
            underline = self.underline
        if strikethrough is None:
            strikethrough = self.strikethrough
        return Font(family, size, bold, italic, underline, strikethrough)

    def _tkinter(self):
        return tkinter.font.Font(
            family=self.family,
            size=self.size,
            weight=tkinter.font.BOLD if self.bold else tkinter.font.NORMAL,
            slant=tkinter.font.ITALIC if self.italic else tkinter.font.ROMAN,
            underline=self.underline,
            overstrike=self.strikethrough,
        )
