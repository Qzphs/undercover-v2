import sprout as s


class Navigation(s.Frame):

    def __init__(self, parent: s.Screen):
        super().__init__(parent, 150, 200)

        self.setup_button = s.TextLabel(self, "(setup screen)")
        self.setup_button.place(150, 0, anchor=s.NE)

        self.words_button = s.TextLabel(self, "(words screen)")
        self.words_button.place(150, 50, anchor=s.NE)

        self.questions_button = s.TextLabel(self, "(questions screen)")
        self.questions_button.place(150, 100, anchor=s.NE)

        self.voting_button = s.TextLabel(self, "(voting screen)")
        self.voting_button.place(150, 150, anchor=s.NE)
