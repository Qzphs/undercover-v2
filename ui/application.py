from game.files import FILES
from game.game import Game

import sprout as s

from ui.navigation import Navigation
from ui.questions_screen import QuestionsScreen
from ui.setup_screen import SetupScreen
from ui.voting_screen import VotingScreen
from ui.words_screen import WordsScreen


class Application(s.Application):

    def __init__(self):
        super().__init__("undercover v2", 960, 600)
        self.game = Game()

        self.setup_screen = SetupScreen(self)
        self.setup_screen.start_button.on_click = self._start_game
        self._init_navigation_commands(self.setup_screen.navigation)

        self.words_screen = WordsScreen(self, self.game)
        self._init_navigation_commands(self.words_screen.navigation)

        self.questions_screen = QuestionsScreen(self, self.game)
        self._init_navigation_commands(self.questions_screen.navigation)

        self.voting_screen = VotingScreen(self, self.game)
        self._init_navigation_commands(self.voting_screen.navigation)

        self.tk.createcommand("tk::mac::Quit", self._save_and_quit)
        self.tk.protocol("WM_DELETE_WINDOW", self._save_and_quit)

        self.change_screen(self.setup_screen)

    def _init_navigation_commands(self, navigation: Navigation):
        navigation.setup_button.on_click = self._go_to_setup
        navigation.words_button.on_click = self._go_to_words
        navigation.questions_button.on_click = self._go_to_questions
        navigation.voting_button.on_click = self._go_to_voting

    def _start_game(self, source: s.TextLabel):
        self.game.reset(self.setup_screen.setup)
        self.words_screen.update()
        self.questions_screen.update()
        self.voting_screen.update()
        self.change_screen(self.words_screen)

    def _go_to_setup(self, source: s.TextLabel):
        if not self.game.players:
            return
        self.setup_screen.update_n_words_label()
        self.change_screen(self.setup_screen)

    def _go_to_words(self, source: s.TextLabel):
        if not self.game.players:
            return
        self.change_screen(self.words_screen)

    def _go_to_questions(self, source: s.TextLabel):
        if not self.game.players:
            return
        self.change_screen(self.questions_screen)

    def _go_to_voting(self, source: s.TextLabel):
        if not self.game.players:
            return
        self.change_screen(self.voting_screen)

    def _save_and_quit(self):
        for file in FILES:
            file.save()
        self.tk.quit()
