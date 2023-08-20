from models.raffle_game import RaffleGame
from modules.main.controller import MainScreenController

raffle_game = RaffleGame()

main_screen_controller = MainScreenController(raffle_game)
main_screen_controller.run()