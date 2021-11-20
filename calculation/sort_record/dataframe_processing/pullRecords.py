import pandas

def get_records_from_csv():
    recordsDataframe = pandas.read_csv(r"C:\Users\natha\desktop\Coding\Net Capital Gains or Loss Calculator\record\Transactions.csv")
    return recordsDataframe

def main():
    recordsDataframe = get_records_from_csv()
    print(recordsDataframe)

if __name__ == "__main__":
    main()
