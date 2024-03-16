# -*- coding: "utf-8" -*-
import frontend 



def janitor(stock_data):
    '''
    Cleans data.
    ----------
    Attributes
    nulls:
    ----------
    Parameters:
    dataframe: tabular
    '''
    
    stock_data = "Almost...there!!!"
    

    #nulls = dataframe.isnull().sum()


    return stock_data 

# Initialize.
st = frontend.st
csv_ex = frontend.csv_ex
data = csv_ex.data()

ohlc = ["date", "open", "high", "low", "close"]

# Stock dataframes.
amzn_df = data['amzn'][['Date', 'Open', 'High', 'Low', 'Close']]
amzn_df = amzn_df.round(2)
amzn_df.columns = ohlc

sox_df = data["sox"]
sox_df.columns = ohlc
sox_df = sox_df.iloc[0:235].copy()

stock_data = {'amzn':amzn_df, 'sox':sox_df}

if __name__ == "__main__":
    st.write("From janitor, run directly")
else:
    st.write("From janitor, run as import")
    
