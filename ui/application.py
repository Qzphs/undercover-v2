from game.files import FILES
from game.game import Game

import sprout as s

from ui.questions_screen import QuestionsScreen
from ui.setup_screen import SetupScreen
from ui.voting_screen import VotingScreen
from ui.words_screen import WordsScreen


class Application(s.Application):

    def __init__(self):
        super().__init__("undercover v2", 960, 600)
        self.game = Game()

        self.setup_screen = SetupScreen(self)
        self.words_screen = WordsScreen(self, self.game)
        self.questions_screen = QuestionsScreen(self, self.game)
        self.voting_screen = VotingScreen(self, self.game)

        self.setup_screen.start_button.on_click = self.start_game
        self.setup_screen.navigation.setup_button.on_click = self.go_to_setup
        self.setup_screen.navigation.words_button.on_click = self.go_to_words
        self.setup_screen.navigation.questions_button.on_click = self.go_to_questions
        self.setup_screen.navigation.voting_button.on_click = self.go_to_voting

        self.words_screen.navigation.setup_button.on_click = self.go_to_setup
        self.words_screen.navigation.words_button.on_click = self.go_to_words
        self.words_screen.navigation.questions_button.on_click = self.go_to_questions
        self.words_screen.navigation.voting_button.on_click = self.go_to_voting

        self.questions_screen.navigation.setup_button.on_click = self.go_to_setup
        self.questions_screen.navigation.words_button.on_click = self.go_to_words
        self.questions_screen.navigation.questions_button.on_click = self.go_to_questions
        self.questions_screen.navigation.voting_button.on_click = self.go_to_voting

        self.voting_screen.navigation.setup_button.on_click = self.go_to_setup
        self.voting_screen.navigation.words_button.on_click = self.go_to_words
        self.voting_screen.navigation.questions_button.on_click = self.go_to_questions
        self.voting_screen.navigation.voting_button.on_click = self.go_to_voting

        self.tk.createcommand("tk::mac::Quit", self.save_and_quit)
        self.tk.protocol("WM_DELETE_WINDOW", self.save_and_quit)

        self.change_screen(self.setup_screen)

    def start_game(self, source: s.TextLabel):
        self.game.reset(self.setup_screen.setup)
        self.words_screen.update()
        self.questions_screen.update()
        self.voting_screen.update()
        self.change_screen(self.words_screen)

    def go_to_setup(self, source: s.TextLabel):
        if not self.game.players:
            return
        self.change_screen(self.setup_screen)

    def go_to_words(self, source: s.TextLabel):
        if not self.game.players:
            return
        self.change_screen(self.words_screen)

    def go_to_questions(self, source: s.TextLabel):
        if not self.game.players:
            return
        self.change_screen(self.questions_screen)

    def go_to_voting(self, source: s.TextLabel):
        if not self.game.players:
            return
        self.change_screen(self.voting_screen)

    def save_and_quit(self):
        for file in FILES:
            file.save()
        self.tk.quit()
