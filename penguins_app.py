import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import seaborn as sns
import random

st.title('Penguins Rock 🐧')
#load data
df=sns.load_dataset('penguins')
df=df.dropna()

#show the data
st.dataframe(df)

#show the barplot 
penguin_count = df['island'].value_counts().reset_index()
fig = px.bar(penguin_count,x='island',y='count',color='island')
st.plotly_chart(fig)

#show the boxplot 
fig = px.box(df,x='island', y= 'body_mass_g')
st.plotly_chart(fig)

#show scatterplot 
fig_scatter = px.scatter(df, y='bill_length_mm', x='body_mass_g',color ='species')
st.plotly_chart(fig_scatter)
