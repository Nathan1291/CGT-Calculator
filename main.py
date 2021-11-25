import pandas
from calculation.calculation import calculate

def main():
        year = int(input("What is the financial year you want to calculate tax on?: "))
        netCapitalChange, totalTaxableComponents = calculate(year)
        print("Net Capital Change is: ", netCapitalChange, "\n")
        print("Components are: ", totalTaxableComponents, "\n")
        
if __name__ == "__main__":
    main()
