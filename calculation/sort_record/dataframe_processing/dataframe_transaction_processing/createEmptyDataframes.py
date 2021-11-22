import pandas

# Initialise empty dataframes for buy and sell
def create_empty_buy_and_sell_dataframes():
    return pandas.DataFrame(columns=["Date","Share", "Price","Units"]), pandas.DataFrame(columns=["Date","Share", "Price","Units"])
