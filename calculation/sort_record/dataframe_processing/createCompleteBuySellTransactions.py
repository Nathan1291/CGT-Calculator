import pandas

from calculation.sort_record.dataframe_processing.dataframe_transaction_processing.createEmptyDataframes import create_empty_buy_and_sell_dataframes
from calculation.sort_record.dataframe_processing.dataframe_transaction_processing.getDataframeInformation import get_records_dataframe_information
from calculation.sort_record.dataframe_processing.dataframe_transaction_processing.splitRecordsIntoDateDetails import split_records_into_date_details




# Processing the whole date and detail Dataframe into Buy and sell Dataframes
def clean_records_into_buy_and_sell_transactions(recordsDataframe):
     recordsDataframe = split_records_into_date_details(recordsDataframe)
     buyRecordsDataframe, sellRecordsDataframe = create_empty_buy_and_sell_dataframes()

     for i in range(len(recordsDataframe)):
         # Check to reduce time complexity, only runs if it is a buy or sell transaction
         if recordsDataframe.iloc[i]["Details"][0] != "B" and recordsDataframe.iloc[i]["Details"][1] == " " or recordsDataframe.iloc[i]["Details"][0] != "S " and recordsDataframe.iloc[i]["Details"][1] == " ":

             transactionType, recordsDataframeInformation = get_records_dataframe_information(recordsDataframe.iloc[i])

             if transactionType == "B":
                 buyRecordsDataframe = buyRecordsDataframe.append(recordsDataframeInformation, ignore_index=True)
             elif transactionType== "S":
                 sellRecordsDataframe = sellRecordsDataframe.append(recordsDataframeInformation, ignore_index=True)

     return buyRecordsDataframe, sellRecordsDataframe
