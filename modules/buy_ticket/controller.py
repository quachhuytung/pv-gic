from constants import MAX_TICKETS_PER_USER
from helpers import clear_screen
from models.raffle_game import RaffleGame

from .screen import BuyTicketScreen

class BuyTicketController:
    def __init__(self, raffle_game: RaffleGame, main_screen_controller):
        self.__raffle_game = raffle_game
        self.__main_screen_controller = main_screen_controller
        self.__screen = BuyTicketScreen()

    def run(self):
        clear_screen()

        inp = self.__screen.prompt_buy_ticket_message()
        is_valid, inp_result = self.__validate_user_input(inp)

        if is_valid:
            username = inp_result['username']
            n_tickets = inp_result['n_tickets']
            
            if not self.__raffle_game.did_user_played(username):
                purchased_tickets = self.__raffle_game.add_user_buy_ticket_turn(username, n_tickets)

                self.__screen.display_purchased_tickets(username, purchased_tickets)

                self.__main_screen_controller.run(is_rerun=True)
            else:
                self.run()

        else:
            self.run()

    def __validate_user_input(self, inp) -> (bool, dict):
        try:
            name, n_tickets_inp = inp.split(',')
            n_tickets = int(n_tickets_inp)

            if not (1 <= n_tickets <= MAX_TICKETS_PER_USER):
                return False, {}
        except:
            return False, {}
        
        ## TODO: VALIDATE NAME
        return True, {
            'username': name,
            'n_tickets': n_tickets
        }