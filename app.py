#Importing the required library

import yfinance as yf
import streamlit as st
import datetime

st.header("Stock data for particular interval")
st.subheader("Please provide the dates to get stock data")

# Deviding frame into two columns
co1,col2=st.columns(2)

# Getting starting and ending dats for the columns
with co1:
    start_date=st.date_input('Please enter the start date',
                     datetime.date(year=2019,month=1,day=1))

with col2:
    end_date=st.date_input('Please enter the end date',
                     datetime.date(year=2020,month=12,day=31))

# Taking the stock name dynamically from user

x=st.text_input("Please enter the stock name ")
if st.button("Enter"):
    hist=yf.Ticker(x)
    data=hist.history(period="1d",start=f"{start_date}",end=f"{end_date}")
    st.dataframe(data)
    st.line_chart(data.Close)

else:
    st.write("Please enter the correct short form of stock")
