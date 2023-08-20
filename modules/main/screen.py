from constants import RAFFLE_STATUS_NOT_RUNNING, RAFFLE_STATUS_RUNNING
from helpers import clear_screen
from models.raffle_game import RaffleGame

class MainScreen:
    WELCOME_TEXT = "Welcome to My Raffle App\n"

    STATUS_TEXT_NOT_STARTED = "\rStatus: Draw has not started"
    STATUS_TEXT_ONGOING = "\rDraw is ongoing. Raffle pot size is {raffle_pot_value}"

    OPTIONS_TEXT = """
    \r[1] Start a New Draw
    \r[2] Buy Tickets
    \r[3] Run Raffle
    """.rstrip()

    def __init__(self, raffle_game: RaffleGame):
        self.raffle_game = raffle_game

    def render_text(self):
        clear_screen()

        screen_txt = self.__class__.WELCOME_TEXT        
        current_raffle_status = self.raffle_game.get_status()

        if current_raffle_status == RAFFLE_STATUS_NOT_RUNNING:
            screen_txt += self.__class__.STATUS_TEXT_NOT_STARTED
        # Status running
        else:
            screen_txt += self.__class__.STATUS_TEXT_ONGOING \
                .format(raffle_pot_value=self.raffle_game.raffle_pot_value)
        
        screen_txt += self.__class__.OPTIONS_TEXT
        return screen_txt
