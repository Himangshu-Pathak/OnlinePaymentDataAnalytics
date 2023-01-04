import pandas as pd
import streamlit as st
from PIL import Image
import plotly.express as px
import plotly.graph_objects as go
import csv


data = pd.read_csv("PaymentData.csv", delimiter = ",")
st.title("The Online Payments Data Analytics Web App")

st.write("")
st.write("")
st.write("")

st.header("Online Payments Fraud Detection Dataset")
st.write("")
st.dataframe(data)

data_filtered = data[["Type", "Amount", "isFraud", "isFlaggedFraud"]]

st.write("")
st.write("")
st.write("")

st.header("Dataset filtered on Type, Amount, isFraud, isFlaggedFraud")
st.dataframe(data_filtered)

columns = {"Type", "Amount", "isFraud", "isFlaggedFraud"}
columnsForPie = {"Type", "isFraud", "isFlaggedFraud"}


st.write("")
st.write("")
st.write("")


data_filtered["Count"] = 0

st.write("")
st.write("")
st.write("")

st.header("Dataset correlation between columns multi-selection")
multi_select_column2 = st.multiselect("Multi-select columns grouped by", list(columns), default = ["Type"])
multi_select_groupby = data_filtered[multi_select_column2].groupby(multi_select_column2).size().reset_index(name = "Count")
multi_select_groupby["Percentage"] = (multi_select_groupby.Count/multi_select_groupby.Count.sum()) * 100
st.dataframe(multi_select_groupby)

st.write("")
st.write("")
st.write("")


st.header("Dataset Aggregated by Count Pie Chart")
pick_columns_visualized = st.selectbox("Visualize by Column", list(columnsForPie))
data_filtered_count_visual = data_filtered.groupby(pick_columns_visualized).count()
data_filtered_count_visual["x-axis"] = data_filtered_count_visual.index
fig = go.Figure([go.Pie(labels = data_filtered_count_visual["x-axis"], values = data_filtered_count_visual["Count"])])
st.plotly_chart(fig)

st.video("https://www.youtube.com/watch?v=15MQtpdzcDg")
