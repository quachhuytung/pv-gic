import pytest
from constants import RAFFLE_GAME_INITIAL_POT, TICKET_PRICE
from models.raffle_game import RaffleGame
from models.ticket import Ticket

@pytest.fixture
def sample_raffle_game():
    return RaffleGame()

def test_raffle_game_should_have_100_dollar_when_start(sample_raffle_game: RaffleGame):
    sample_raffle_game.begin_raffle_game()
    assert sample_raffle_game.get_raffle_value() == RAFFLE_GAME_INITIAL_POT


@pytest.mark.parametrize("n_ticket_less_than_1", [
    0,
    -2,
    -1000
])
def test_raffle_game_should_not_allow_user_purchase_n_tickets_less_than_one_test(
        sample_raffle_game: RaffleGame,
        n_ticket_less_than_1
    ):
    is_success, _ = sample_raffle_game.add_user_buy_ticket_turn('Joe', n_ticket_less_than_1)
    assert not is_success

@pytest.mark.parametrize("n_ticket_less_more_than_5", [
    6,
    10,
    100000
])
def test_raffle_game_should_not_allow_user_purchase_n_tickets_less_than_one_test(
        sample_raffle_game: RaffleGame,
        n_ticket_less_more_than_5
    ):
    is_success, _ = sample_raffle_game.add_user_buy_ticket_turn('Joe', n_ticket_less_more_than_5)
    assert not is_success


@pytest.mark.parametrize("n_tickets", [
    1,
    2,
    3,
    4,
    5
])
def test_raffle_game_should_increase_pot_when_user_purchases_ticket(sample_raffle_game: RaffleGame, n_tickets):
    sample_raffle_game.begin_raffle_game()
    sample_raffle_game.add_user_buy_ticket_turn('Joe', n_tickets)
    
    assert sample_raffle_game.get_raffle_value() == RAFFLE_GAME_INITIAL_POT + TICKET_PRICE * n_tickets

def test_raffle_game_should_increase_pot_when_users_purchase_ticket_sequence(sample_raffle_game: RaffleGame):
    sample_raffle_game.begin_raffle_game()
    
    n1 = 2
    sample_raffle_game.add_user_buy_ticket_turn('Joe', n1)

    n2 = 5
    sample_raffle_game.add_user_buy_ticket_turn('Joe One', n2)

    n3 = 4
    sample_raffle_game.add_user_buy_ticket_turn('Joe Two', n3)

    assert sample_raffle_game.get_raffle_value() == RAFFLE_GAME_INITIAL_POT + TICKET_PRICE * (n1 + n2 + n3)

def test_user_can_purchase_up_to_five_tickets_within_this_draw(sample_raffle_game: RaffleGame):
    is_success = True

    current_is_success, _ = sample_raffle_game.add_user_buy_ticket_turn('Joe', 2)
    is_success = is_success and current_is_success
    
    current_is_success, _ = sample_raffle_game.add_user_buy_ticket_turn('Joe', 1)
    is_success = is_success and current_is_success
    
    current_is_success, _ = sample_raffle_game.add_user_buy_ticket_turn('Joe', 2)
    is_success = is_success and current_is_success

    assert is_success

def test_same_user_cannot_purchase_more_than_five_tickets_within_this_draw(sample_raffle_game: RaffleGame):
    is_success = True

    current_is_success, _ = sample_raffle_game.add_user_buy_ticket_turn('Joe', 2)
    is_success = is_success and current_is_success
    
    current_is_success, _ = sample_raffle_game.add_user_buy_ticket_turn('Joe', 3)
    is_success = is_success and current_is_success
    
    current_is_success, _ = sample_raffle_game.add_user_buy_ticket_turn('Joe', 2)
    is_success = is_success and current_is_success

    assert not is_success

def test_same_user_can_purchase_upto_than_five_tickets_in_each_draw(sample_raffle_game: RaffleGame):
    is_success = True

    current_is_success, _ = sample_raffle_game.add_user_buy_ticket_turn('Joe', 2)
    is_success = is_success and current_is_success
    
    current_is_success, _ = sample_raffle_game.add_user_buy_ticket_turn('Joe', 3)
    is_success = is_success and current_is_success

    ## Simulate new draw
    sample_raffle_game.clear_user_states()

    is_success_round_2 = True

    current_is_success, _ = sample_raffle_game.add_user_buy_ticket_turn('Joe', 2)
    is_success_round_2 = is_success_round_2 and current_is_success
    
    current_is_success, _ = sample_raffle_game.add_user_buy_ticket_turn('Joe', 3)
    is_success_round_2 = is_success_round_2 and current_is_success

    assert is_success and is_success_round_2

