# -*- coding: "utf-8" -*-

# Import libraries.
from frontend import st, Path, pct

# Define the paths to the csv files.
amzn_csv = Path(r"resources/amazon.csv")
sox_csv = Path(r"resources\SOX_2015_2020.csv")

# Create dictionary for paths.
csv_dict = {
        "amzn": amzn_csv,
        "sox": sox_csv
        }

# Create function to make dataframes.
def data():
    '''
    Reads csv file containing stock daily trading information into dataframe.
    '''
    # Read csv into dataframe.
    df = {} 

    #ohlc = ["date", "open", "high", "low", "close"]

    ## Stock dataframes.
    #amzn_df = data['amzn'][['Date', 'Open', 'High', 'Low', 'Close']]
    #amzn_df.columns = ohlc

    #sox_df = data["sox"]
    #sox_df.columns = ohlc
    #sox_df = sox_df.iloc[0:235].copy()

    #stock_data = (amzn_df, sox_df)

    for k, v in csv_dict.items():
   

        # Pandas dataframe.
        csv_df = pct.read_csv(csv_dict[k])

        # Updates df dict.
        df[k] = csv_df

    return df
