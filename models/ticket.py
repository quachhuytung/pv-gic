from typing import Tuple
import random

from constants import (
    TICKET_N_NUMS,
    TICKET_VALID_NUM
)

class Ticket:
    def __init__(self):
        self.__ticket_nums = self.__generate_ticket_value()

    def __repr__(self):
        return ' '.join([str(x) for x in self.__ticket_nums])
    
    def __generate_ticket_value(self) -> Tuple[int]:
        return tuple(random.sample(TICKET_VALID_NUM, k=TICKET_N_NUMS))
    
    def get_ticket_nums(self):
        return self.__ticket_nums
    
    def compare_ticket(self, other_ticket: 'Ticket') -> int:
        """
        Return the number of match components between 2 tickets
        ---
        Params:
          - other ticket: Ticket to compare
        ---
        Output:
          - n: number of match components between 2 tickets (0 - 5)
        """
        match_components = set(self.__ticket_nums).intersection(other_ticket.get_ticket_nums())
        return len(match_components)       
