from constants import RAFFLE_STATUS_ENDED
from models.raffle_game import RaffleGame
from modules.run_raffle.screen import RunRaffleScreen
from modules.run_raffle.service import RunRaffleService


class RunRaffleController:
    def __init__(self, raffle_game: RaffleGame, main_screen):
        self.__raffle_game = raffle_game
        self.__raffle_calculation_service = RunRaffleService(raffle_game)
        self.__run_raffle_screen = RunRaffleScreen()
        self.__main_screen = main_screen

    def run(self):
        winning_ticket, remaining_rewards, current_round_rewards = self.__raffle_calculation_service.calculate_raffle()

        self.__raffle_game.set_raffle_value(remaining_rewards)
        self.__raffle_game.set_status(RAFFLE_STATUS_ENDED)
        
        self.__raffle_game.clear_user_states()
        self.__raffle_calculation_service.clear_status()

        print(self.__run_raffle_screen.render_text(winning_ticket, current_round_rewards))

        self.__main_screen.run(is_rerun=True)