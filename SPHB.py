import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from pywaffle import Waffle



st.title('SLEEP PATTERNS AND HUMAN BEHAVIOUR')
st.write('Author: [Almasfiza Shaikh] (https://www.linkedin.com/in/almasfiza-shaikh-004048185/)')
st.write("""This is a survey analysis of 54 responses survey, which comprises of questions ranging from sleeping pattern and habits to general behavioural inclinations.
***""")

df = pd.read_csv("https://raw.githubusercontent.com/almasfiza/SPHB/main/SPHB_data_modified.csv?token=AO24MASJJKXNH4HZVMDQJTDBI4PDQ") 
st.write("""## DATASET
This is the dataset represented as a dataframe in pandas. Know more about [dataframe] (https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html) and [pandas.] (https://pandas.pydata.org/docs/index.html)""")
st.write(df)
st.write("""***""")
st.write("""## QUESTIONS 
These are the list of questions which were invovled in the survey. Additional questions relating to the identity of responders have been removed. """)
st.table(df.columns)
st.write("""***""")
st.write("""## FAMILIARISING WITH THE DATA """)
st.write(df.describe())
st.write(df.describe(include="object"))
st.write("***")

st.write("## AGE GROUPS IN OUR DATA ")


wafflefig = plt.figure(FigureClass = Waffle, 
                rows = 5,
                columns = 11,
                values = pd.array(df["Your age group:"].value_counts()),
                labels = ['18-25', '<17', '>25'],
                colors = ["#C0C0C0","#DCDCDC","#000000"])
st.pyplot()





st.write("***")
st.write("""## WHEN DO PEOPLE GO TO SLEEP? """)
st.set_option('deprecation.showPyplotGlobalUse', False)
sns.countplot(y = df["What time do you usually go to sleep?"], data = df, color="#808495")
st.pyplot()
st.write(""" We can see that majority of the people in the study go to sleep around midnight. 

""")
st.write(df["What time do you usually go to sleep?"].groupby(df["Your age group:"]))
st.write("***")
st.write("""## WHEN DO PEOPLE WAKE UP? """)
st.set_option('deprecation.showPyplotGlobalUse', False)
sns.countplot(y = df["What time do you usually wake up?"], data = df, color="#808495")
st.pyplot()



