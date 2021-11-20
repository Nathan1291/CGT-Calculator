import pandas
from calculation.sort_record.sortRecords import sort_records

def calculate():
    buyRecordsDataframe, sellRecordsDataframe = sort_records()
    return buyRecordsDataframe, sellRecordsDataframe


if __name__ == "__main__":
    main()
