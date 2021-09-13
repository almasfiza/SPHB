from altair.vegalite.v4.schema.channels import Tooltip
from altair.vegalite.v4.schema.core import TooltipContent
from seaborn.palettes import color_palette
import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from pywaffle import Waffle
import plotly.graph_objects as go
from plotly import tools
import plotly.offline as py
import plotly.express as px
import mpld3
import webbrowser


st.set_page_config(page_title = "Sleep patterns and human behaviour")







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
                colors = ["#FF3EA5FF","#EDFF00FF","#00A4CCFF"])
st.pyplot()
st.write("The majority of participants are between the age of 18-25 years old, or classified as Young Adults.")





st.write("***")
st.write("""## WHEN DO PEOPLE GO TO SLEEP? """)
st.set_option('deprecation.showPyplotGlobalUse', False)
sns.countplot(y = df["What time do you usually go to sleep?"], data = df, color="#EDFF00FF")
st.pyplot()
st.write(""" We can see that majority of the people in the study go to sleep around midnight. 

""")

st.write("***")
st.write("""## WHEN DO PEOPLE WAKE UP? """)
st.set_option('deprecation.showPyplotGlobalUse', False)
sns.countplot(y = df["What time do you usually wake up?"], data = df, color="#FF3EA5FF")
st.pyplot()

st.write("***")

#df.plot(kind='bar', stacked=True)
#plt.title("Age group and sleep time")
#plt.xlabel("What time do you usually go to sleep?")
#plt.ylabel("Do you wish you had more hours of sleep?")
#st.pyplot()

st.write("## GENERAL RESPONSES")


option = st.selectbox(
'See what majority of the people are doing',
(df.columns[1:]))


ax = sns.countplot(y = df[option], data = df, color="#00A4CCFF")
plt.show()
st.pyplot()




st.write("## GROUPED TRENDS")





option_group = st.selectbox(
'Select a question',
(df.columns[1:]))


group = (df.drop(option_group,axis=1)).columns[1:]
group_choose = st.radio("Group by ", group)





df_plot = df.groupby([group_choose, option_group]).size().reset_index().pivot(columns=group_choose,index=option_group, values=0)
df_plot.plot(kind='bar', stacked=True, color= ["#FF3EA5FF","#EDFF00FF","#00A4CCFF","#0C6291", "#EF476F"])
st.pyplot()




