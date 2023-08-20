from collections import defaultdict

from models.raffle_game import RaffleGame
from models.ticket import Ticket


class RunRaffleService:
    def __init__(self, raffle_game: RaffleGame):
        self.__raffle_game = raffle_game

        # Generate wining ticket:
        self.__wining_ticket = Ticket()
    
    def clear_status(self):
        self.__wining_ticket = None

    def calculate_raffle(self):
        user_states = self.__raffle_game.get_user_states()

        ## Calculate winning group
        """
        winning group := {
            2: { # group match 2 number
                'Ben': 2 # Ben has 2 tickets of this group
            }
        }
        """
        winning_group = defaultdict(lambda: defaultdict(lambda: 0))
        current_raffle_value = remaining_rewards = self.__raffle_game.get_raffle_value()

        for user, current_user_tickets in user_states.items():
            for current_ticket in current_user_tickets:
                n_match_with_winning_ticket =  self.__wining_ticket.compare_ticket(current_ticket)

                if n_match_with_winning_ticket >= 2:
                    winning_group[n_match_with_winning_ticket][user] += 1
        
        result = defaultdict(lambda: defaultdict(lambda: {}))

        group_rewards_ratio = [0, 0, 0.1, 0.15, 0.25, 0.5]
        group_rewards_value = [x * current_raffle_value for x in group_rewards_ratio]

        for group in range(2, 6):
            user_winning_per_group = winning_group[group]

            if not user_winning_per_group:
                result[group] = {}
            else:
                # calculate remaining_rewards for next round
                remaining_rewards -= group_rewards_value[group]

                n_share_current_group = sum(user_winning_per_group.values())
                for user, n_ticket_winning_this_group in user_winning_per_group.items():
                    result[group][user] = (
                        n_ticket_winning_this_group,
                        round((n_ticket_winning_this_group / n_share_current_group) * group_rewards_value[group], 2)
                    )
        
        return self.__wining_ticket, remaining_rewards, result