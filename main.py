import pandas
from calculation.calculation import calculate

def main():
        year = int(input("What is the financial year you want to calculate tax on?: "))
        soldInCurrentFinancialYearRecordsDataframe = calculate(year)
        print(soldInCurrentFinancialYearRecordsDataframe)

if __name__ == "__main__":
    main()
