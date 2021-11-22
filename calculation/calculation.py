import pandas
from calculation.sort_record.sortRecords import sort_records
from calculation.sort_record.sortAllSellRecordsIntoCurrentFinancialYearSellRecords import take_current_financial_year_from_sellRecordsDataframe
from calculation.transaction_calculations.matchingTransactions import match_transactions



def calculate(year):
    buyRecordsDataframe, sellRecordsDataframe = sort_records()
    CurrentFinancialYearSellRecordsDataframe = take_current_financial_year_from_sellRecordsDataframe(year, sellRecordsDataframe)
    return CurrentFinancialYearSellRecordsDataframe
