# -*- coding: "utf-8" -*-

# Import libraries.
import streamlit as st

st.title(':blue[Hellooo...Universe!!!] :sunglasses:')
st.divider()

tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10, tab11 = st.tabs(["Dataframes", "SQL", "Charts", "Technical Analysis","Time Series", "Machine Learning", "Deep Learning", "Algorithmic Trading", "Robo Advisor", "Cypto Currency", "dApps"])

with tab1:
    st.header("This dataframe is the raw dataframe.")
    st.dataframe(df, width=700, height=250)

#with tab2:
#    df_pctChange = df.iloc[:,0:].pct_change().dropna()
#    st.header("This dataframe is the percent changes.")
#    st.dataframe(df_pctChange, width=700, height=250)
#
#with tab3:
#    chart_picks = st.selectbox("Choose the chart to view the trading: open, high, low, close", (
#        "candle",
#        "line open",
#        "line high",
#        "line low",
#        "line close",
#        "line ohlc",
#        )
#        )
#    candle_chart = candles(df_pctChange)
#    _open, high, low, close = line(df_pctChange)
#    chart_dict = {
#            "candle": candle_chart,
#            "line open": _open,
#            "line high": high,
#            "line low": low,
#            "line close": close,
#            "line ohlc": _open + high + low + close,
#            }
#
#    for chart in chart_dict:
#        if chart == chart_picks:
#            c = chart_dict[chart_picks]
#            #st.write(c)
#            st.altair_chart(c, use_container_width=True)
#with tab4:
#    tech_analysis = st.selectbox("Choose the TA to view.", ("Sharpe Ratio", "Price-to-Earnings Ratio"))
#
#    ta = {"Sharpe Ratio": "Sharpe Ratio is under construction...stay tuned!", "Price-to-Earnings Ratio": "Price-to-Earnings Ratio is under construction...stay tuned!"}
#    for i in ta:
#        if i == tech_analysis:
#            wip = ta[i]
#            st.write(wip)
#
#with tab5:
#    st.write("Time Series: under construction...stay tuned!")
#
#with tab6:
#    st.write("Machine Learning: under construction...stay tuned!")
#
#with tab7:
#    st.write("Deep Learning: under construction...stay tuned!")
#
#with tab8:
#    st.write("Algorithmic Trading: under construction...stay tuned!")
#
#with tab9:
#    st.write("Robo Advisor: under construction...stay tuned!")
#
#with tab10:
#    st.write("Cypto Currency: under construction...stay tuned!")
#
#with tab11:
#    st.write("dApps: under construction...stay tuned!")
#
#
##container = st.container(border=True)
##container.write("This is inside the container")
##st.write("This is outside")
##container.write("This is inside too")
#
#st.write("Howdeee...almost there!")
