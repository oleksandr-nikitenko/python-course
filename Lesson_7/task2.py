"""
Create a function which takes as input two dicts with structure mentioned above, then computes and returns the total
price of stock.
"""
stock, prices = {"banana": 6, "apple": 0, "orange": 32, "pear": 15}, {"banana": 4, "apple": 2, "orange": 1.5, "pear": 3}


def calculate_price(stock_dict: dict, prices_dict: dict) -> float:
    total_price = float()
    for key in stock_dict:
        total_price += stock_dict[key] * prices_dict[key]
    return total_price


print(calculate_price(stock, prices))
