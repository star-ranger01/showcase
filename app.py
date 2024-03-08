# -*- coding: "utf-8" -*-

# Import dependencies.
import sys
import streamlit as st
from pathlib import Path
import pct_change as pct
import frontend


def read_csv():
    # Read csv into dataframe.
    for k, v in csv_dict.items():

        # Pandas dataframe.
        csv_df = pct.read_csv(csv_dict[k])
        df[k] = csv_df


frontend.user_interface()

st.title(':blue[Hellooo...Universe!!!] :sunglasses:')
st.divider()

tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10, tab11 = st.tabs(["Dataframes", "SQL", "Charts", "Technical Analysis","Time Series", "Machine Learning", "Deep Learning", "Algorithmic Trading", "Robo Advisor", "Cypto Currency", "dApps"])


amzn_csv = Path("./resources/amazon.csv")
sox_csv = Path("./resources/SOX_2015_2020.csv")

csv_dict = {
        "amzn": amzn_csv,
        "sox": sox_csv
        }

df = {}
option = st.sidebar.selectbox("Select data collection.", ("Pre-collected data in csv format", "Make an API request for data"))

if option == "Pre-collected data in csv format":
    st.sidebar.write("My man.")
    read_csv()


else:
    st.sidebar.write("Dude.")




if __name__ == "__main__":
    user_name = sys.argv[1]
else:
    print("Run as import")

