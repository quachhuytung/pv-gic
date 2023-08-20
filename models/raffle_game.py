from constants import (
    RAFFLE_GAME_INITIAL_POT,
    RAFFLE_STATUS_NOT_RUNNING,
    RAFFLE_STATUS_RUNNING,
    TICKET_PRICE
)
from models.ticket import Ticket


class RaffleGame:
    def __init__(self):
        self.raffle_game_status = RAFFLE_STATUS_NOT_RUNNING
        self.raffle_pot_value = 0

        self.user_states = {}

    def set_status(self, status):
        self.raffle_game_status = status

    def set_raffle_value(self, value):
        self.raffle_pot_value = value

    def get_status(self):
        return self.raffle_game_status
    
    def get_raffle_value(self):
        return self.raffle_pot_value
    
    def begin_raffle_game(self):
        self.raffle_game_status = RAFFLE_STATUS_RUNNING
        self.raffle_pot_value = RAFFLE_GAME_INITIAL_POT
    
    def add_user_buy_ticket_turn(self, username: str, n_tickets: int):
        """
        """
        current_user_tickets = [Ticket() for _ in range(n_tickets)]
        self.user_states[username] = current_user_tickets

        self.set_raffle_value(self.get_raffle_value() + n_tickets * TICKET_PRICE)
        return current_user_tickets
    
    def clear_user_states(self):
        self.user_states = {}
    
    def get_user_states(self):
        return self.user_states
    
    def did_user_played(self, username):
        return username in self.user_states.keys()