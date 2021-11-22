import pandas
import calculation.sort_record.dataframe_processing.pullRecords as pullRecords
from calculation.sort_record.dataframe_processing.createCompleteBuySellTransactions import clean_records_into_buy_and_sell_transactions



# Complete Function to sort records into buy and sell records in the form of
# [Date, Share, Price and Unit] from raw pandas dataframe of transactions.csv
def sort_records():
    recordsDataframe = pullRecords.get_records_from_csv()
    buyRecordsDataframe, sellRecordsDataframe = clean_records_into_buy_and_sell_transactions(recordsDataframe)
    return buyRecordsDataframe, sellRecordsDataframe
