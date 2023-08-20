from typing import List

from models.ticket import Ticket

class BuyTicketScreen:
    BUY_TICKET_PROMPT_TXT = "Enter your name, no of tickets to purchase: "
    
    def prompt_buy_ticket_message(self) -> str:
        return input(self.__class__.BUY_TICKET_PROMPT_TXT)
    
    def display_purchased_tickets(self, username: str, purchased_tickets: List[Ticket]):
        """
        """
        print(f'Hi {username}, you have purchased {len(purchased_tickets)} ticket(s)-')
        for i, ticket in enumerate(purchased_tickets):
            print(f'Ticket {i+1}: {ticket}')