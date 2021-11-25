import pandas
from calculation.transaction_calculations.records_processing.getShareNamesFromCurrentFYSellRecords import get_share_names_from_current_FY_sell_records
from calculation.transaction_calculations.records_processing.getAllSpecifiedShareTransactions import get_share_transaction_from_buy_records, get_share_transaction_from_sell_records
from calculation.transaction_calculations.records_processing.createFeeDataframe import createShareFeeDateDataframe
from calculation.transaction_calculations.calculation_transaction_processing.matchBuySelltransactions import calculate


# Find all transactions of buy and sell records atrributing to a specific share
def calculateTaxableAmount(currFY, CurrentFinancialYearSellRecordsDataframe, buyRecordsDataframe, sellRecordsDataframe):
    currentFYShareNames = get_share_names_from_current_FY_sell_records(CurrentFinancialYearSellRecordsDataframe)
    totalTaxableComponents = {"CG > 1 Yr": 0,"CG < 1 Yr": 0, "CL": 0}

    for share in currentFYShareNames:
        buyShareTransactions = get_share_transaction_from_buy_records(share, buyRecordsDataframe)
        sellShareTransactions = get_share_transaction_from_sell_records(share, sellRecordsDataframe)

        buyShareTransactionsFeeDataframe = createShareFeeDateDataframe(buyShareTransactions)
        sellShareTransactionsFeeDataframe = createShareFeeDateDataframe(sellShareTransactions)

        taxableComponents = calculate(buyShareTransactionsFeeDataframe, sellShareTransactionsFeeDataframe, currFY)

        totalTaxableComponents["CG > 1 Yr"] += taxableComponents["CG > 1 Yr"]
        totalTaxableComponents["CG < 1 Yr"] += taxableComponents["CG < 1 Yr"]
        totalTaxableComponents["CL"] += taxableComponents["CL"]
    return totalTaxableComponents
