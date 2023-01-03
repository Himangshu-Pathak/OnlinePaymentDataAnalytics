import pandas as pd
import streamlit as st
from PIL import Image
import plotly.express as px
import plotly.graph_objects as go
import csv


fraud_data = pd.read_csv("C:\\Users\\Padmaja\\Downloads\\Career\\Placements\\Projects\\Python\\Payments Data\\ProjectCode\\PaymentData.csv", delimiter = ",")
st.title("The Online Payments Data Analytics Web App")

st.write("")
st.write("")
st.write("")

st.header("Online Payments Fraud Detection Dataset")
st.write("")
st.dataframe(fraud_data)

fraud_data_filtered = fraud_data[["Type", "Amount", "isFraud", "isFlaggedFraud"]]

st.write("")
st.write("")
st.write("")

st.header("Dataset filtered on Type, Amount, isFraud, isFlaggedFraud")
st.dataframe(fraud_data_filtered)

columns = {"Type", "Amount", "isFraud", "isFlaggedFraud"}
columnsForPie = {"Type", "isFraud", "isFlaggedFraud"}
st.write("")
st.write("")
st.write("")

st.header("Dataset aggregated by count")
pick_columns = st.selectbox("Count by column: ", list(columns))

fraud_data_filtered["Count"] = 0
fraud_data_filtered_count = fraud_data_filtered.groupby(pick_columns).count()
fraud_data_filtered_count = fraud_data_filtered_count[["Count"]]
fraud_data_filtered_count['Percentages'] = (fraud_data_filtered_count.Count/fraud_data_filtered_count.Count.sum()) * 100

st.dataframe(fraud_data_filtered_count)

#st.write("")
#st.write("")
#st.write("")

#st.header("Dataset correlation between columns")
#multi_select_column = st.multiselect("Multi-select columns for correlation", list(columns), default = ["Type"])

#multi_select_fraud_data_filtered = fraud_data_filtered[multi_select_column]

#st.dataframe(multi_select_fraud_data_filtered)

st.write("")
st.write("")
st.write("")

st.header("Dataset correlation between columns multi-selection")
multi_select_column2 = st.multiselect("Multi-select columns grouped by", list(columns), default = ["Type"])

multi_select_groupby = fraud_data_filtered[multi_select_column2].groupby(multi_select_column2).size().reset_index(name = "Count")

multi_select_groupby["Percentages"] = (multi_select_groupby.Count/multi_select_groupby.Count.sum()) * 100

st.dataframe(multi_select_groupby)

st.write("")
st.write("")
st.write("")

st.header("Dataset Aggregated by Count Pie Chart")
pick_columns_visualized = st.selectbox("Visualize by Column", list(columnsForPie))

fraud_data_filtered_count_visual = fraud_data_filtered.groupby(pick_columns_visualized).count()

fraud_data_filtered_count_visual['x-axis'] = fraud_data_filtered_count_visual.index

fig = go.Figure(data = [go.Pie(labels = fraud_data_filtered_count_visual["x-axis"], values = fraud_data_filtered_count_visual["Count"])])

st.plotly_chart(fig)

