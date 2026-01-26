import tkinter

from sprout.constants import LEFT, NW, OFFSCREEN
from sprout.widget import Container, Widget


class Application:
    """Main class for GUIs using Sprout."""

    def __init__(self, title: str, width: int, height: int):
        self._tk = tkinter.Tk()
        self._tk.title(title)
        self._tk.geometry(f"{width}x{height}+{0}+{0}")
        self._tk.createcommand("tk::mac::Quit", self._on_quit)
        self._tk.protocol("WM_DELETE_WINDOW", self._on_quit)
        self.width = width
        self.height = height
        self._screen = Screen(self)
        self._screen._base.place(x=0, y=0)

    @property
    def screen(self):
        """The screen currently being displayed."""
        return self._screen

    @screen.setter
    def screen(self, screen: "Screen"):
        self._screen._base.place(x=OFFSCREEN, y=0)
        self._screen = screen
        self._screen._base.place(x=0, y=0)

    def start(self):
        self._tk.mainloop()

    def _on_quit(self):
        if self.on_quit is not None:
            self.on_quit()
        self._tk.quit()

    def on_quit(self):
        pass


class Screen(Container):
    """Similar to tkinter.Frame, but occupies the entire window."""

    def __init__(self, parent: Application):
        self._application = parent
        self._base = tkinter.Frame(
            parent._tk,
            width=parent.width,
            height=parent.height,
        )
        self._contents = self._base
        self.children: list[Widget] = []

    def pack(self, side=LEFT):
        raise NotImplementedError("cannot pack screen")

    def place(self, x, y, anchor=NW):
        raise NotImplementedError("cannot place screen")

    @property
    def background_colour(self):
        """Same as tkinter's bg."""
        return self._base.cget("bg")

    @background_colour.setter
    def background_colour(self, background_colour: str | None):
        if background_colour is None:
            self._base.config(bg=self._application._tk.cget("bg"))
        else:
            self._base.config(bg=background_colour)
