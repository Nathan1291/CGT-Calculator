import pandas

# accounts for partial transactions along with full
def createBuyTransactionValueDataframe(buyTransaction, unitsUsed):
    # pull info
    buyTransactionDate = buyTransaction["Date"]
    buyTransactionUnits = buyTransaction["Units"]
    buyTransactionPrice = buyTransaction["Price"]
    buyTransactionFee = buyTransaction["Fees"]

    # calculate value
    totalValue = float((buyTransactionUnits * buyTransactionPrice + buyTransactionFee) * (unitsUsed/buyTransactionUnits))

    # return the dataframe back in the form ["date", "Units", "Value"]
    transactionData = {"Date": [buyTransactionDate],
                       "Units": [unitsUsed],
                       "Value": [totalValue]
                       }

    transactionDataframe = pandas.DataFrame(transactionData)

    return transactionDataframe.iloc[0]
