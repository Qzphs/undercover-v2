import sprout as s

from ui.constants import DEFAULT_FONT


class Navigation(s.Frame):

    def __init__(self, parent: s.Screen):
        super().__init__(parent, 150, 200)

        self.setup_button = NavigationButton(self, "(setup)")
        self.setup_button.place(150, 0, anchor=s.NE)

        self.words_button = NavigationButton(self, "(words)")
        self.words_button.place(150, 50, anchor=s.NE)

        self.questions_button = NavigationButton(self, "(questions)")
        self.questions_button.place(150, 100, anchor=s.NE)

        self.voting_button = NavigationButton(self, "(voting)")
        self.voting_button.place(150, 150, anchor=s.NE)


class NavigationButton(s.TextLabel):

    def __init__(self, parent, text):
        super().__init__(parent, text)
        self.font = DEFAULT_FONT

    def emphasise(self):
        self.font = self.font.copy(bold=True)
