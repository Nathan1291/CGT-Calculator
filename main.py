import pandas
from calculation.calculation import calculate

def main():
        buyRecordsDataframe, sellRecordsDataframe = calculate()
        print(buyRecordsDataframe)
        print(sellRecordsDataframe)

if __name__ == "__main__":
    main()
