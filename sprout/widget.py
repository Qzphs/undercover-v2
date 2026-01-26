import tkinter

from sprout.constants import LEFT, NW


class Widget:
    """Base class for Sprout widgets."""

    def __init__(self, parent: "Container"):
        self.parent = parent
        self._base = tkinter.Frame(parent._contents)
        self.parent.children.append(self)

    def pack(self, side: str = LEFT):
        """Same as tkinter's pack()."""
        self._base.pack(side=side)

    def place(self, x: int, y: int, anchor: str = NW):
        """Same as tkinter's place()."""
        self._base.place(x=x, y=y, anchor=anchor)

    def destroy(self):
        """Same as tkinter's destroy()."""
        self.parent.children.remove(self)
        self._base.destroy()


class Container(Widget):
    """Base class for Sprout widgets that contain other widgets."""

    def __init__(self, parent: "Container"):
        super().__init__(parent)
        self._contents = self._base
        self.children: list[Widget] = []
