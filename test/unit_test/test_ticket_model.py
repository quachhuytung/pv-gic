import pytest

from constants import TICKET_N_NUMS, TICKET_MAX_COMPONENT, TICKET_MIN_COMPONENT
from models.ticket import Ticket

@pytest.fixture
def sample_ticket():
    return Ticket()

@pytest.fixture()
def winning_ticket_sample():
    return Ticket((1, 2, 3, 4, 5))

def test_should_generate_ticket_with_valid_number_of_component(sample_ticket: Ticket):
    assert len(sample_ticket.get_ticket_nums()) == TICKET_N_NUMS

def test_should_generate_ticket_with_valid_component(sample_ticket: Ticket):
    is_valid = True
    for component in sample_ticket.get_ticket_nums():
        is_valid = is_valid and (TICKET_MIN_COMPONENT <= component <= TICKET_MAX_COMPONENT)
    assert is_valid

def test_should_generate_ticket_with_unique_numbers(sample_ticket: Ticket):
    ticket_nums = sample_ticket.get_ticket_nums()
    assert len(set(ticket_nums)) == TICKET_N_NUMS

@pytest.mark.parametrize("match_zero_component_ticket", [
    (7, 8, 9, 10, 11),
    (6, 8, 11, 12, 15),
    (8, 7, 15, 12, 10)
])
def test_should_match_zero_component(winning_ticket_sample: Ticket, match_zero_component_ticket):
    assert winning_ticket_sample.compare_ticket(Ticket(match_zero_component_ticket)) == 0

@pytest.mark.parametrize("match_one_component_ticket", [
    (1, 8, 9, 10, 11),
    (6, 2, 11, 12, 15),
    (8, 7, 15, 5, 10)
])
def test_should_match_one_component(winning_ticket_sample: Ticket, match_one_component_ticket):
    assert winning_ticket_sample.compare_ticket(Ticket(match_one_component_ticket)) == 1

@pytest.mark.parametrize("match_two_components_ticket", [
    (1, 8, 9, 10, 2),
    (6, 2, 11, 3, 15),
    (8, 3, 15, 5, 10)
])
def test_should_match_two_components(winning_ticket_sample: Ticket, match_two_components_ticket):
    assert winning_ticket_sample.compare_ticket(Ticket(match_two_components_ticket)) == 2


@pytest.mark.parametrize("match_three_components_ticket", [
    (1, 8, 4, 10, 2),
    (6, 2, 4, 3, 15),
    (8, 3, 1, 5, 10)
])
def test_should_match_three_components(winning_ticket_sample: Ticket, match_three_components_ticket):
    assert winning_ticket_sample.compare_ticket(Ticket(match_three_components_ticket)) == 3

@pytest.mark.parametrize("match_four_components_ticket", [
    (1, 5, 4, 10, 2),
    (5, 2, 4, 3, 15),
    (2, 3, 1, 5, 10)
])
def test_should_match_four_components(winning_ticket_sample: Ticket, match_four_components_ticket):
    assert winning_ticket_sample.compare_ticket(Ticket(match_four_components_ticket)) == 4

def test_should_match_jackpot(winning_ticket_sample: Ticket):
    assert winning_ticket_sample.compare_ticket(Ticket((1,2,3,4,5))) == 5