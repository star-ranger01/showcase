# -*- coding: "utf-8" -*-

# Import dependencies
import sys
import pandas as pd
import streamlit as st

''' Percent Change Formula
Increase = Current Price - Original Price
Percent Increase = (Increase / Original Price) x 100
'''
def read_csv(path):
    df = pd.read_csv(path)
    #st.dataframe(df)

def main():
    original_price = 198.87
    current_price = 254.32
    increase = current_price - original_price
    percent_increase = increase / original_price * 100

    st.text(
            f"The original price is ${original_price}\n"
            f"The current price is ${current_price}\n"
            f"The increase is ${increase}\n"
            f"The increase as percentage of the original price is {percent_increase}%\n"
            )
#amzn_csv = Path(
#        "./resources/amazon.csv"
#        )
#sox_csv = Path(
#        "./resources/SOX_2015_2020"
#        )
csv_path = ()

if __name__ == "__main__":
    user_name = sys.argv[1]
    main()
else:
    print("pct_change.py is run as import.")
