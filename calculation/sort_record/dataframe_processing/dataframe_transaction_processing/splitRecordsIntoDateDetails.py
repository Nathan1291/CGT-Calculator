import pandas

# Function taking in the whole Dataframe of Date, Reference, Details, Debit, Credit and Balance and Turning it into Date and Details
def split_records_into_date_details(recordsDataframe):
    return recordsDataframe[["Date", "Details"]]
