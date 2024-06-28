import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import altair as alt
import plotly.express as px
#$import plotly_figure_factory as ff
from plotly.tools import FigureFactory as ff
import scipy


st.header('1. Altair scatter plot')
#chart_data = pd.DataFrame(np.random.randn(500,5), columns = ['a ,b ,c , d ,e ']) 
chart_data = pd.DataFrame(np.random.randn(500,5), columns = ['a','b','c','d','e'])
chart = alt.Chart(chart_data).mark_circle().encode(x = 'a' , y = 'b', size = 'c',
        tooltip = ['a','b','c','d','e'])
#chart = alt.Chart(chart_data).mark_circle().encode(x = 'a' , y = 'b', size = 'c',
       # tooltip = ['a','b','c','d','e'])
st.altair_chart(chart)

st.header('2. Interactive line charts')
st.subheader('2.1 Line chart')
df = pd.read_csv('C:\\Users\\aska5\\pythonworks,\\lang_data.csv')
lang_list = df.columns.to_list() # convert the language into colusmns
lang_choices = st.multiselect('Choose your language', lang_list)
new_df = df[lang_choices] #dicitonary 
st.line_chart(new_df)

st.subheader('2.2 Area chart')
st.area_chart(new_df)

st.header('3. Data visualization with plotly')
st.subheader('3.1 display dataset')
df = pd.read_csv('\\Users\\aska5\\pythonworks,\\tips.csv')
st.dataframe(df.head())

st.subheader('3.2 pie chart')
fig = px.pie(df, values = 'total_bill', names = 'time', opacity = .7)
st.plotly_chart(fig)

st.subheader('3.3 pie chart with multiple parameters')
fig = px.pie(df, values = 'total_bill', names = 'day', opacity = .7,
            color_discrete_sequence = px.colors.sequential.RdBu) # from documentation
st.plotly_chart(fig)

#st.header('3.4 Histogram')
#x1= np.random.randn(200)
#x2= np.random.randn(200)
#x3= np.random.randn(200)

#hist_data = [x1,x2,x3]
#group_labels = ['group - 1','group - 2','group - 3']
#fig = ff.create_distplot(hist_data,group_labels, bin_size = [.1,.25,.5])
#st.plotly_chart(fig)

st.subheader('3.4 Histogram')
x1 = np.random.randn(200) - 2
x2 = np.random.randn(200)
x3 = np.random.randn(200) + 2

hist_data = [x1,x2,x3]
group_labels = ['Group - 1', 'Group - 2', 'Group - 3']
fig = ff.create_distplot(hist_data, group_labels, bin_size = [.1,.25,.5])

#keep having scipy errors