import matplotlib.pyplot as plt 
import pandas as pd
import streamlit as st
import numpy as np
import seaborn as sns 
st.title("ASSIGNMENT4")
st.header("ML Batch Icfoss")
st.set_option('deprecation.showPyplotGlobalUse', False)
st.subheader("Titanic Dataset")
df = pd.read_csv('titanic.csv')
tit = df.head(25)
st.table(tit)
st.subheader("Analaysis")
data1=df.loc[df.Sex == 'male'].shape[0]
st.write("Total number of male members",data1)
st.subheader("Survivors of titanic")
arr = np.array(df.loc[df.Survived == 1,'Name'])
st.table(arr)
st.subheader("Pairplot")
sns.pairplot(tit,hue='Sex',palette='rainbow')
st.pyplot()
st.subheader("Bar Plot")
tit.plot(kind='bar')
st.pyplot()
st.markdown("url_link of the taken dataset")
st.markdown("[Google](https://github.com/awesomedata/awesome-public-datasets)")
url_link = "https://github.com/awesomedata/awesome-public-datasets"

