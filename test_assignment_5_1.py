import pytest

from assignment_5_1 import return_coins


@pytest.mark.parametrize(
    ("money", "denominations", "expected_coins"),
    [
        (0, [1, 2, 5], []),
        (-5, [1, 2, 5], []),
        ("a", [1, 2, 5], []),
        ("10", [1, 2, 5], []),
        (1, [1, 2, 5, 10, 20, 50], [1]),
        (25, [1, 2, 5, 10, 20, 50], [20, 5]),
        (233, [1, 2, 5, 10, 20, 50], [50, 50, 50, 50, 20, 10, 2, 1]),
        (9, [2, 5, 10, 20], [5, 2, 2]),
        (5, [1], [1, 1, 1, 1, 1]),
        (13, [9, 8, 5, 1], [9, 1, 1, 1, 1]),
        (40, [25, 20, 10, 5, 1], [25, 10, 5]),
    ]
)
def test_return_coins(money, denominations, expected_coins):
    assert return_coins(money, denominations) == expected_coins
