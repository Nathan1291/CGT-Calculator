import pandas


# Pull all unique shares using sets
def get_share_names_from_current_FY_sell_records(CurrentFinancialYearSellRecordsDataframe):
    share_names = set()
    for name in CurrentFinancialYearSellRecordsDataframe["Share"]:
        share_names.add(name)
    return share_names
