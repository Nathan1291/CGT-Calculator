import pandas

# Takes in a singular date and detail dataframe and processes it ready to append to the buy and sell Dataframes
def get_records_dataframe_information(recordData):
    detailsList = str(recordData["Details"]).split()

    date = recordData["Date"]
    transactionType = detailsList[0]
    shareName = detailsList[2]
    noOfUnits = int(detailsList[1])
    price = float(detailsList[4])

    recordsDataframeInformation = { "Date": date,
                                    "Share": shareName,
                                    "Price": price,
                                    "Units": noOfUnits
                                  }

    return transactionType, recordsDataframeInformation
