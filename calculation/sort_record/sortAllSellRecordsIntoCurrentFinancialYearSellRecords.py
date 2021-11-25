import pandas

# Takes in the whole sell records and returns transactions that occured in the specified financial year
def take_current_financial_year_from_sellRecordsDataframe(currFY, sellRecordsDataframe):
    # Create empty dataframe for current financial year sell records
    curr_FYSellRecordsDataframe = pandas.DataFrame(columns=["Date","Share", "Price","Units"])

    for i in range(len(sellRecordsDataframe)):
        [day, month, year] = list(map(int, sellRecordsDataframe.iloc[i]["Date"].split("/")))
        # Check for valid Financial year, before July of the year or after june of the previous year
        if year == currFY and month < 7 or year == (currFY - 1) and month > 6:
            curr_FYSellRecordsDataframe = curr_FYSellRecordsDataframe.append(sellRecordsDataframe.iloc[i], ignore_index=True)

    return curr_FYSellRecordsDataframe
