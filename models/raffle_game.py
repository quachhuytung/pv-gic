from collections import defaultdict

from constants import (
    MAX_TICKETS_PER_USER,
    RAFFLE_GAME_INITIAL_POT,
    RAFFLE_STATUS_NOT_RUNNING,
    RAFFLE_STATUS_RUNNING,
    TICKET_PRICE,
    MIN_TICKETS_PER_USER
)
from models.ticket import Ticket


class RaffleGame:
    def __init__(self):
        self.__raffle_game_status = RAFFLE_STATUS_NOT_RUNNING
        self.__raffle_pot_value = 0

        self.__user_states = defaultdict(lambda: [])
        self.__wining_ticket = None

    def set_status(self, status):
        self.__raffle_game_status = status

    def set_raffle_value(self, value):
        self.__raffle_pot_value = value

    def get_status(self):
        return self.__raffle_game_status
    
    def get_raffle_value(self):
        return self.__raffle_pot_value
    
    def begin_raffle_game(self):
        self.__raffle_game_status = RAFFLE_STATUS_RUNNING
        self.__raffle_pot_value = RAFFLE_GAME_INITIAL_POT
    
    def add_user_buy_ticket_turn(self, username: str, n_tickets: int) -> (bool, list):
        """
        """
        if n_tickets < MIN_TICKETS_PER_USER or n_tickets > MAX_TICKETS_PER_USER:
            return False, []
                
        if not self.is_user_able_to_play(username, n_tickets):
            return False, []
        
        current_user_tickets = [Ticket() for _ in range(n_tickets)]
        self.__user_states[username].extend(current_user_tickets)

        self.set_raffle_value(self.get_raffle_value() + n_tickets * TICKET_PRICE)
        return True, current_user_tickets
    
    def clear_user_states(self):
        self.__user_states = defaultdict(lambda: [])
    
    def get_user_states(self):
        return self.__user_states
    
    def is_user_able_to_play(self, username, n_tickets=0):
        """
        Check whether user is able to play. User is able to play only when
          - he/she hasn't play yet
          - in current round, he/she hasn't buy for total 5 tickets
        ----
        Params:
          - username: string. Username to check
        ---
        Return:
          - is_able_to_play: boolean
        """
        return (
            (username not in self.__user_states.keys()) or \
            (len(self.__user_states[username]) + n_tickets <= MAX_TICKETS_PER_USER)
        )
    
    def get_winning_ticket(self) -> Ticket:
        return self.__wining_ticket
    
    def calculate_raffle(self):
        ## Generate a winning ticket
        self.__wining_ticket = Ticket()