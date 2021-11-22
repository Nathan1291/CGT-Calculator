import pandas
from calculation.transaction_calculations.calculation_transaction_processing.getShareNamesFromCurrentFYSellRecords import get_share_names_from_current_FY_sell_records
from calculation.transaction_calculations.calculation_transaction_processing.getAllSpecifiedShareTransactions import get_share_transaction_from_buy_records, get_share_transaction_from_sell_records



# Find all transactions of buy and sell records atrributing to a specific share
def match_transactions(CurrentFinancialYearSellRecordsDataframe, buyRecordsDataframe, sellRecordsDataframe):
    currentFYShareNames = get_share_names_from_current_FY_sell_records(CurrentFinancialYearSellRecordsDataframe)

    for share in currentFYShareNames:
        buyShareTransactions = get_share_transaction_from_buy_records(share, buyRecordsDataframe)
        sellShareTransactions = get_share_transaction_from_sell_records(share, sellRecordsDataframe)


# to code: match up starting from the last of the sell - link up to appropriate buy transactions using FIFO, once fully exhausted then check date, if valid then put in a dataframe and pass down
# need to make another function to check the validity of the date (can be crosschecked with existing database ?)
# may want to add in the value of the entire transaction so the process is a little bit easier to link up once an appropriate grouping has been made
