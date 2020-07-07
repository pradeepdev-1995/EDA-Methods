import matplotlib
matplotlib.use("Agg")
import seaborn as sns 
import streamlit as st_object 
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 


activities = ["EDA"]	
choice = st_object.sidebar.selectbox("Select Activities",activities)

if choice == 'EDA':
	st_object.subheader("Exploratory Data Analysis")

	data = st_object.file_uploader("Upload a Dataset", type=["csv", "txt"])
	if data is not None:
		df = pd.read_csv(data)
		st_object.dataframe(df.head())
		
		if st_object.checkbox("Show Value Counts"):
			st_object.write(df.iloc[:,-1].value_counts())

		if st_object.checkbox("Correlation Plot(Matplotlib)"):
			plt.matshow(df.corr())
			st_object.pyplot()

		if st_object.checkbox("Correlation Plot(Seaborn)"):
			st_object.write(sns.heatmap(df.corr(),annot=True))
			st_object.pyplot()

		if st_object.checkbox("Show Shape"):
			st_object.write(df.shape)

		if st_object.checkbox("Show Columns"):
			all_columns = df.columns.to_list()
			st_object.write(all_columns)

		if st_object.checkbox("Summary"):
			st_object.write(df.describe())


		if st_object.checkbox("Pie Plot"):
			all_columns = df.columns.to_list()
			column_to_plot = st_object.selectbox("Select 1 Column",all_columns)
			pie_plot = df[column_to_plot].value_counts().plot.pie(autopct="%1.1f%%")
			st_object.write(pie_plot)
			st_object.pyplot()



