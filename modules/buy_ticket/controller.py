import re

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
            
            is_success, purchased_tickets = self.__raffle_game.add_user_buy_ticket_turn(username, n_tickets)
            if is_success:
                self.__screen.display_purchased_tickets(username, purchased_tickets)
                self.__main_screen_controller.run(is_rerun=True)
            else:
                self.run()

        else:
            self.run()

    def __validate_user_input(self, inp) -> (bool, dict):
        inp_list = inp.split(',')

        if len(inp_list) != 2:
            return False, {}
        
        try:
            name, n_tickets_inp = inp.split(',')
            n_tickets = int(n_tickets_inp)

            ## Validate number of tickets
            if not (1 <= n_tickets <= MAX_TICKETS_PER_USER):
                return False, {}
            
            # Validate name
            pattern = re.compile(r"^[a-zA-Z]+(([',. -][a-zA-Z ])?[a-zA-Z]*)*$")
            if not pattern.match(name):
                return False, {}
        except:
            return False, {}
        
        return True, {
            'username': name,
            'n_tickets': n_tickets
        }