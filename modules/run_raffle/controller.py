from constants import RAFFLE_STATUS_ENDED
from models.raffle_game import RaffleGame
from modules.run_raffle.screen import RunRaffleScreen


class RunRaffleController:
    def __init__(self, raffle_game: RaffleGame, main_screen):
        self.__raffle_game = raffle_game
        self.__run_raffle_screen = RunRaffleScreen()
        self.__main_screen = main_screen

    def run(self):
        winning_ticket, _, current_round_rewards = self.__raffle_game.calculate_raffle()
        self.__raffle_game.clear_states()
        
        print(self.__run_raffle_screen.render_text(winning_ticket, current_round_rewards))
        self.__main_screen.run(is_rerun=True)