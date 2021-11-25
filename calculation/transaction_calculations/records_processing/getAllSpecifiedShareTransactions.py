import pandas



# Get transactions with a specific share from the buy records
def get_share_transaction_from_buy_records(shareName, buyRecordsDataframe):

    buyShareTransactions = pandas.DataFrame(columns=["Date","Share", "Price","Units"])

    for i in range(len(buyRecordsDataframe)):
        if buyRecordsDataframe.iloc[i]["Share"] == shareName:
            buyShareTransactions = buyShareTransactions.append(buyRecordsDataframe.iloc[i])

    buyShareTransactions = buyShareTransactions.reset_index(drop=True)
    return buyShareTransactions



# Get transactions with a specific share from the sell records
def get_share_transaction_from_sell_records(shareName, sellRecordsDataframe):
    sellShareTransactions = pandas.DataFrame(columns=["Date","Share", "Price","Units"])

    for i in range(len(sellRecordsDataframe)):
        if sellRecordsDataframe.iloc[i]["Share"] == shareName:
            sellShareTransactions = sellShareTransactions.append(sellRecordsDataframe.iloc[i])

    sellShareTransactions = sellShareTransactions.reset_index(drop=True)

    return sellShareTransactions
