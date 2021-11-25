import pandas
from calculation.transaction_calculations.calculation_transaction_processing.calculation_processing.transaction_processing import createBuyTransactionValueDataframe
from calculation.transaction_calculations.calculation_transaction_processing.calculation_processing.calculateTaxableComponents import calculateTaxableComponents



def calculate(buyShareTransactionsFeeDataframe, sellShareTransactionsFeeDataframe, currFY):
    taxableComponents = {"CG > 1 Yr": 0,"CG < 1 Yr": 0, "CL": 0}


    # Keep a tracker of the current buy transaction we are at (starting at the first transaction) (-1 due to index' starting at 0)
    buyRecordsLength = len(buyShareTransactionsFeeDataframe)
    buyRecordTracker = buyRecordsLength - 1


    # iterating through the sell records to link up appropriate buy records
    for i in range(len(sellShareTransactionsFeeDataframe)):
        buyTransactionRecords = pandas.DataFrame(columns=["Date", "Units", "Value"])
        # starting from the last sold share (i+1 due to i starting at 0)
        currentSellShareTransaction = sellShareTransactionsFeeDataframe.iloc[len(sellShareTransactionsFeeDataframe) - (i + 1)]

        sellTransactionDate = currentSellShareTransaction["Date"]
        sellTransactionUnits = currentSellShareTransaction["Units"]

        # keeping a tracker of how many units are left
        remainingUnits = sellTransactionUnits

        # find the execution date, month and year from current sell transaction
        [day, month, year] = list(map(int, currentSellShareTransaction["Date"].split("/")))

        # if sell date is inside of the current FY
        if year == currFY and month < 7 or year == (currFY - 1) and month > 6:
            # if there sell transaction has not been fully
            while remainingUnits > 0:
                # find the current buy record and its information
                buyTransaction = buyShareTransactionsFeeDataframe.iloc[buyRecordTracker]
                buyTransactionDate = buyTransaction["Date"]
                buyTransactionUnits = buyTransaction["Units"]

                # if the buy transaction is fully exhausted on the sell transaction, use all units and move to the next transaction,  then add to the transaction records
                if remainingUnits >= buyTransactionUnits:
                    remainingUnits -= buyTransactionUnits
                    buyRecordTracker -= 1
                    # add the transaction to the records with the related information, used up all buy units therefore no use in messing with fees
                    buyTransactionRecords = buyTransactionRecords.append(createBuyTransactionValueDataframe(buyTransaction, buyTransactionUnits))

                # if the buy transaction is not fully exhausted on the sell transaction, use up all units and deduct the appropriate fee, then add to the transaction records

                elif remainingUnits < buyTransactionUnits:
                    transactionsUsed = remainingUnits
                    unitDifference = buyTransactionUnits - remainingUnits
                    remainingUnits = 0
                    # add the transaction to the records with the related information, didnt used up all buy units therefore have to mess with fees
                    buyTransactionRecords = buyTransactionRecords.append(createBuyTransactionValueDataframe(buyTransaction, transactionsUsed))
                    # changing the values of the original dataframe to make the fees associated with transactions match up
                    buyShareTransactionsFeeDataframe.at[buyRecordTracker, "Fees"] = buyShareTransactionsFeeDataframe.iloc[buyRecordTracker]["Fees"] * (unitDifference / buyTransactionUnits)
                    buyShareTransactionsFeeDataframe.at[buyRecordTracker, "Units"] = unitDifference


            # calculate capital changes for the current sell transaction and add that to the total taxable components
            CG_after_1Yr, CG_Before_1Yr, CL = calculateTaxableComponents(buyTransactionRecords, currentSellShareTransaction)
            taxableComponents["CG > 1 Yr"] += CG_after_1Yr
            taxableComponents["CG < 1 Yr"] += CG_Before_1Yr
            taxableComponents["CL"] += CL


        # if sell date is outside of current FY, no need to calculate change in value, just need to find and remove associated buy transactions
        else:
            # if there sell transaction has not been fully
            while remainingUnits > 0:
                # find the current buy record and its information
                buyTransaction = buyShareTransactionsFeeDataframe.iloc[buyRecordTracker]
                buyTransactionDate = buyTransaction["Date"]
                buyTransactionUnits = buyTransaction["Units"]


                # if the buy transaction is fully exhausted on the sell transaction, use all units and move to the next transaction
                if remainingUnits >= buyTransactionUnits:
                    remainingUnits -= buyTransactionUnits
                    buyRecordTracker -= 1


                # if the buy transaction is not fully exhausted on the sell transaction, use up all units and deduct the appropriate fee
                elif remainingUnits < buyTransactionUnits:
                    unitDifference = buyTransactionUnits - remainingUnits
                    remainingUnits = 0
                    # changing the values of the original dataframe to make the fees associated with transactions match up
                    buyShareTransactionsFeeDataframe.at[buyRecordTracker, "Fees"] = buyShareTransactionsFeeDataframe.iloc[buyRecordTracker]["Fees"] * (unitDifference / buyTransactionUnits)
                    buyShareTransactionsFeeDataframe.at[buyRecordTracker, "Units"] = unitDifference

    return taxableComponents
