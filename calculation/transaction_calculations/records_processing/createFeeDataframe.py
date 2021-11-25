import pandas

# finds the value of the total trade and calculates the appropriate brokerage fee
def createShareFeeDateDataframe(specificShareTransactions):

    shareTransactionFeeDataframe = pandas.DataFrame(columns=["Date","Share", "Price","Units", "Fees"])

    for i in range(len(specificShareTransactions)):
        # find total trade value
        transactionUnits = specificShareTransactions.iloc[i]["Units"]
        transactionPrice = specificShareTransactions.iloc[i]["Price"]

        tradeValue = transactionUnits * transactionPrice

        # calculate brokerage fee off trade values, fee values taken from normal commsec trading fees
        if tradeValue <= 1000:
            brokerageFee = 10
        elif tradeValue <= 10000:
            brokerageFee = 10
        elif tradeValue <= 25000:
            brokerageFee = 19.95
        else:
            brokerageFee = 0.0012

        # organise data to return back to the main dataframe
        transactionData = {"Date": specificShareTransactions.iloc[i]["Date"],
                           "Share": specificShareTransactions.iloc[i]["Share"],
                           "Units": int(transactionUnits),
                           "Price": float(transactionPrice),
                           "Fees": float(brokerageFee)
                           }

        shareTransactionFeeDataframe = shareTransactionFeeDataframe.append(transactionData, ignore_index=True)

    return shareTransactionFeeDataframe
