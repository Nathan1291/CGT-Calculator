import pandas


# Get a pandas dataframe from the given csv file
def get_records_from_csv():
    recordsDataframe = pandas.read_csv(r"C:\Users\natha\desktop\Coding\Net Capital Gains or Loss Calculator\record\Transactions.csv")
    return recordsDataframe
