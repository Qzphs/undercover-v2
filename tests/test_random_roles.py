import pytest

from game.role import Role
from game.setup import Setup


@pytest.fixture
def setup():
    setup = Setup()
    setup.players.extend(f"player {i}" for i in range(4))
    return setup


def test_random_roles_one_undercover(setup: Setup):
    setup.n_undercovers = 1
    setup.n_mr_whites = 0
    roles = setup.random_roles()
    assert len(roles) == 4
    assert roles.count(Role.CIVILIAN) == 3
    assert roles.count(Role.UNDERCOVER) == 1


def test_random_roles_one_mr_white(setup: Setup):
    setup.n_undercovers = 0
    setup.n_mr_whites = 1
    roles = setup.random_roles()
    assert len(roles) == 4
    assert roles.count(Role.CIVILIAN) == 3
    assert roles.count(Role.MR_WHITE) == 1


def test_random_roles_one_of_each(setup: Setup):
    setup.n_undercovers = 1
    setup.n_mr_whites = 1
    roles = setup.random_roles()
    assert len(roles) == 4
    assert roles.count(Role.CIVILIAN) == 2
    assert roles.count(Role.UNDERCOVER) == 1
    assert roles.count(Role.MR_WHITE) == 1


def test_random_roles_two_undercover(setup: Setup):
    setup.n_undercovers = 2
    setup.n_mr_whites = 0
    roles = setup.random_roles()
    assert len(roles) == 4
    assert roles.count(Role.CIVILIAN) == 2
    assert roles.count(Role.UNDERCOVER) == 2


def test_random_roles_two_mr_white(setup: Setup):
    setup.n_undercovers = 0
    setup.n_mr_whites = 2
    roles = setup.random_roles()
    assert len(roles) == 4
    assert roles.count(Role.CIVILIAN) == 2
    assert roles.count(Role.MR_WHITE) == 2
