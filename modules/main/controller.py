from constants import RAFFLE_STATUS_RUNNING
from models.raffle_game import RaffleGame
from modules.run_raffle.controller import RunRaffleController
from modules.buy_ticket.controller import BuyTicketController
from .screen import MainScreen

class MainScreenController:
    OPTIONS = {
        'EXIT': '0',
        'NEW_DRAW': '1',
        'BUY_TICKET': '2',
        'RUN': '3'
    }

    def __init__(self, raffle_game: RaffleGame):
        self.__raffle_game = raffle_game
        self.__screen = MainScreen(self.__raffle_game)

    def run(self, is_rerun=False):
        if is_rerun:
            input('\nPress any key to return to main menu')

        print(self.__screen.render_text())

        user_inp = self.__get_user_input()

        if user_inp == self.__class__.OPTIONS['NEW_DRAW']:
            self.__raffle_game.begin_raffle_game(is_rerun)
            print(self.__screen.render_text())
            self.run()
        elif user_inp == self.__class__.OPTIONS['BUY_TICKET']:
            if self.__raffle_game.get_status() != RAFFLE_STATUS_RUNNING:
                self.run()
            else:
                BuyTicketController(self.__raffle_game, self).run()
        elif user_inp == self.__class__.OPTIONS['RUN']:
            if self.__raffle_game.get_status() != RAFFLE_STATUS_RUNNING:
                self.run()
            else:
                RunRaffleController(self.__raffle_game, self).run()
        elif user_inp == self.__class__.OPTIONS['EXIT']:
            exit(0)
        else:
            self.run()

    def __get_user_input(self) -> str:
        user_inp = input()

        if not (user_inp in self.__class__.OPTIONS.keys()):
            print(self.__screen.render_text())
        
        return user_inp