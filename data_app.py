# -*- coding: utf-8 -*-
"""
Created on Sat Jan 28 15:45:37 2023

@author: JEHANGIR
"""

# on anaconda command prompt: streamlit run data_app.py i.e. the filw name

import pandas as pd

import streamlit as st

file = r'C:\Users\JEHANGIR\OneDrive\Desktop\KHI AI All lectures\Lecture 2\Billionaire.csv'

st.header('Billionaire Bar Chart')

# reading the file
df = pd.read_csv('Billionaire.csv')

# for reading, single file, multiple sheets data
# df = read_excel(filename)
# names = df.sheet_names 
# all_data = []
# for name in names:
#   all_data.append(df[name])

# highest rank billionaire 
top_bill = df[df['Rank']==1]

# find count of billionaires by country 
# bill_count = df.groupby('Country')['Name'].count().sort_values(ascending=False).head(10)
# st.bar_chart(bill_count)

# find the most popular source of income 
# df.groupby('Source')['Name'].count().sort_values()

# get the cumulative wealth of billionaires belonging to US (Data Cleaning)
df['NetWorth'].apply(lambda x: float(x.replace('$', '').replace(' B', '')))

# interactivity
# all_countries = df['Country'].unique()
# selection = st.selectbox('Select Country', all_countries)
# subset = df[df['Country'] == selection]
# st.dataframe(subset)

# input and output seperating by columns 
all_countries = sorted(df['Country'].unique())

col1, col2 = st.columns(2)

#column 1
#display on streamlit
selected_country = col1.selectbox('Select Your Country', all_countries)
#subset on a selected country
subset_country = df[df['Country'] == selected_country]

#get unique sources from the selected country
sources = sorted(subset_country['Source'].unique())
#display multiselect option on source
selected_source = col1.multiselect('Selection Source of Income', sources)
#subset on selected source
subset_source = subset_country[subset_country['Source'].isin(selected_source)]


#column2
main_string = '{} - Billionaires'.format(selected_country)
# main_string = selected_country + ' - Billionaires'
col2.header(main_string)
col2.table(subset_country)
col2.header('Source wise Info')
col2.table(subset_source)






