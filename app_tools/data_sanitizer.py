# -*- coding: "utf-8" -*-
import app_tools

# Initialize.
st = app_tools.frontend.st

def janitor(dataframe):
    '''
    Cleans data.
    ----------
    Attributes
    nulls:
    ----------
    Parameters:
    dataframe: tabular
    '''
    dataframe[['Date', 'Open', 'High', 'Low', 'Close']]
    nulls = dataframe.isnull().sum()


    return nulls
    
if __name__ == "__main__":
    st.write("From janitor, run directly")
else:
    st.write("From janitor, run as import")
    
