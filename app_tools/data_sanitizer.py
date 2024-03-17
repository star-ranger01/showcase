# -*- coding: "utf-8" -*-
import frontend 
#from app_tools.app

dust_list = []
dust = (dust_list)

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
    
    
    for k, v in stock_data.items():
        
        stock_df = stock_data[k]
        dust_list.append(k.upper())

        df_types = stock_df.dtypes
        dust_list.append(df_types)

        # TODO: if df_types = object
        # TODO: else:
        
        df_count = stock_df.count()
        dust_list.append(df_count)

        df_na = stock_df.isna().sum()
        dust_list.append(df_na)

        # TODO: if df_na > 0":
        # TODO: else:
        
        df_null = stock_df.isnull().sum()
        dust_list.append(df_null)

        # TODO: if df_null > 0":
        # TODO: else:
        
        df_dupli = stock_df.duplicated().sum()
        dust_list.append(df_dupli)
        
        # TODO: if df_dupli == True
        # TODO: else:

        df_shape = stock_df.shape
        dust_list.append(df_shape)
        #df_info = stock_df.info()

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

duster = janitor(stock_data)

if __name__ == "__main__":
    st.write("From janitor, run directly")
else:
    st.write("From janitor, run as import")
    
