from models.raffle_game import RaffleGame
from models.ticket import Ticket


class RunRaffleScreen:
    def render_text(self, winning_ticket: Ticket, current_round_rewards: dict):
        screen_txt = 'Running Raffle..\n'
        screen_txt += f'Winning Ticket is {winning_ticket}'

        for group, current_group_reward_detail in current_round_rewards.items():
            screen_txt += f'\n\nGroup {group} Winners:'
            
            if not current_group_reward_detail:
                screen_txt += '\nNil'
            else:
                for user, reward_detail in current_group_reward_detail.items():
                    n_tickets, reward_val = reward_detail
                    screen_txt += f'\n{user} with {n_tickets} winning ticket(s)- ${reward_val}'

        return screen_txt