import pandas
from datetime import date


# Calculate all taxable components
def calculateTaxableComponents(buyTransactionRecords, currentSellShareTransaction):
    # setting up components
    CG_after_1Yr = 0
    CG_Before_1Yr = 0
    CL = 0

    # pulling sell unit info and calculating value of the transaction
    sellUnits = currentSellShareTransaction["Units"]
    sellPrice = currentSellShareTransaction["Price"]
    sellFees = currentSellShareTransaction["Fees"]
    sellValue = sellUnits * sellPrice - sellFees

    [sellDay, sellMonth, sellYear] = list(map(int, currentSellShareTransaction["Date"].split("/")))

    # going through the buy transactions associated with the sell transaction and calculating the capital gain/loss on each one
    for i in range(len(buyTransactionRecords)):
        buyUnits = buyTransactionRecords.iloc[i]["Units"]
        buyDate = buyTransactionRecords.iloc[i]["Date"]
        buyValue = buyTransactionRecords.iloc[i]["Value"]

        # calculting the change in capital value associated with the buy transaction
        capital_Change = round(sellValue * (buyUnits/sellUnits) - buyValue, 2)


        # sorting the transaction into the 3 categories based on its characteristics
        if capital_Change < 0:
            CL += capital_Change
        else:
            [buyDay, buyMonth, buyYear] = list(map(int, buyTransactionRecords.iloc[i]["Date"].split("/")))
            if (date(sellYear, sellMonth, sellDay)-date(buyYear, buyMonth, buyDay)).days > 365:
                CG_after_1Yr += capital_Change
            else:
                CG_Before_1Yr += capital_Change

    # return the values associated with the current sell transaction
    return CG_after_1Yr, CG_Before_1Yr, CL
