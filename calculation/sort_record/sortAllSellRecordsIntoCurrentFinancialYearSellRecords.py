import pandas

# Takes in the whole sell records and returns transactions that occured in the specified financial year
def take_current_financial_year_from_sellRecordsDataframe(CurrFY, sellRecordsDataframe):
    # Create empty dataframe for current financial year sell records
    Curr_FYSellRecordsDataframe = pandas.DataFrame(columns=["Date","Share", "Price","Units"])

    for i in range(len(sellRecordsDataframe)):
        [day, month, year] = list(map(int, sellRecordsDataframe.iloc[i]["Date"].split("/")))
        # Check for valid Financial year, before July of the year or after june of the previous year
        if year == CurrFY and month < 7 or year == (CurrFY - 1) and month > 6:
            Curr_FYSellRecordsDataframe = Curr_FYSellRecordsDataframe.append(sellRecordsDataframe.iloc[i], ignore_index=True)

    return Curr_FYSellRecordsDataframe
