import InterviewCake.stocks as stocks


def test_1():
    prices = [10, 7, 5, 8, 11, 9]
    assert stocks.get_max_profit(stock_prices_yesterday=prices) == 6


def test_min_at_end():
    prices = [10, 7, 5, 4, 11, 2]
    assert stocks.get_max_profit(stock_prices_yesterday=prices) == 7


def test_max_at_start():
    prices = [12, 7, 5, 8, 11, 9]
    assert stocks.get_max_profit(stock_prices_yesterday=prices) == 6


def test_falling_prices():
    prices = [10, 9, 8, 7, 6, 5]
    assert stocks.get_max_profit(stock_prices_yesterday=prices) == -1


def test_falling_prices2():
    prices = [10, 8, 5, 1]
    assert stocks.get_max_profit(stock_prices_yesterday=prices) == -2
