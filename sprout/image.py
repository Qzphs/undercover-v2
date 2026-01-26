import tkinter


class Image:
    """Same as tkinter.PhotoImage."""

    def __init__(self, base: tkinter.PhotoImage):
        self._base = base

    @classmethod
    def from_file(cls, filename: str):
        return Image(tkinter.PhotoImage(file=filename))

    def subsample(self, x: int, y: int | None = None):
        """Same as tkinter.PhotoImage's subsample()."""
        if y is None:
            y = x
        return Image(self._base.subsample(x=x, y=y))

    def zoom(self, x: int, y: int | None = None):
        """Same as tkinter.PhotoImage's zoom()."""
        if y is None:
            y = x
        return Image(self._base.zoom(x=x, y=y))
