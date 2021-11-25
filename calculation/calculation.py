import pandas
from calculation.sort_record.sortRecords import sort_records
from calculation.sort_record.sortAllSellRecordsIntoCurrentFinancialYearSellRecords import take_current_financial_year_from_sellRecordsDataframe
from calculation.transaction_calculations.calculateTaxableAmount import calculateTaxableAmount


# calculate all components and final net capital change
def calculate(year):
    # get the total taxable components
    buyRecordsDataframe, sellRecordsDataframe = sort_records()
    CurrentFinancialYearSellRecordsDataframe = take_current_financial_year_from_sellRecordsDataframe(year, sellRecordsDataframe)
    totalTaxableComponents = calculateTaxableAmount(year, CurrentFinancialYearSellRecordsDataframe, buyRecordsDataframe, sellRecordsDataframe)

    CG_after_1Yr = totalTaxableComponents["CG > 1 Yr"]
    CG_before_1Yr = totalTaxableComponents["CG < 1 Yr"]
    CL = totalTaxableComponents["CL"]

    # calculate the final change in capital
    netCapitalChange = 0
    capitalLossTracker = CL

    # if the capital loss is fully exhausted on capital gains before 1 year
    if CG_before_1Yr > capitalLossTracker:
        netCapitalChange = round(CG_before_1Yr + CL + CG_after_1Yr * 0.5, 2)
    else:
        capitalLossTracker += CG_before_1Yr

        # if the capital loss is fully exhausted on capital gains after 1 year
        if CG_after_1Yr > capitalLossTracker:
            netCapitalChange = round((CG_after_1Yr + capitalLossTracker) * 0.5, 2)

        # if there is a net capital loss
        else:
            netCapitalChange = round(capitalLossTracker + CG_after_1Yr, 2)

    return netCapitalChange, totalTaxableComponents
