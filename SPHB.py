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
import scipy.stats as stats

#Title
st.set_page_config(page_title = "Sleep patterns and human behaviour")

#Sidebar
st.sidebar.title("Sleep Patterns and Human Behaviour")
st.sidebar.write("### This is a survey analysis to help find patterns between sleeping habits and human behaviour.")
st.sidebar.write("### You can find the original report on the survey [here](https://drive.google.com/file/d/1oL6C1wbQ2Q_bOralSikrsqv_GxESpUDK/view?usp=sharing).")
st.sidebar.write("***")
st.sidebar.write("Libraries used:")
st.sidebar.write("""numpy==1.18.1
matplotlib==3.1.3
scipy==1.4.1
altair==4.1.0
streamlit==0.72.0
mpld3==0.5.5
seaborn==0.10.0
pywaffle==0.6.3
plotly==5.3.1
pandas==1.0.1
""")


#Intro
st.title('SLEEP PATTERNS AND HUMAN BEHAVIOUR')
st.write('Author: [Almasfiza Shaikh] (https://www.linkedin.com/in/almasfiza-shaikh-004048185/)')
st.write("""This is a survey analysis of 54 responses survey, which comprises of questions ranging from sleeping pattern and habits to general behavioural inclinations.
***""")

#Data
df = pd.read_csv("https://raw.githubusercontent.com/almasfiza/SPHB/main/SPHB_data_modified.csv?token=AO24MASJJKXNH4HZVMDQJTDBI4PDQ") 
st.write("""## DATASET
This is the dataset represented as a dataframe in pandas. Know more about [dataframe] (https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html) and [pandas] (https://pandas.pydata.org/docs/index.html).""")
st.write(df)
st.write("""***""")

#Questions
st.write("""## QUESTIONS 
These are the list of questions which were invovled in the survey. Additional questions relating to the identity of responders have been removed. """)
st.table(df.columns)
st.write("""***""")
st.write("""## FAMILIARISING WITH THE DATA """)
st.write(df.describe())
st.write(df.describe(include="object"))
st.write("***")


#Waffle chart
st.write("## AGE GROUPS IN OUR DATA ")
wafflefig = plt.figure(FigureClass = Waffle, 
                rows = 5,
                columns = 11,
                values = pd.array(df["Your age group:"].value_counts()),
                labels = ['18-25', '>25', '<17'],
                colors = ["#FF3EA5FF","#EDFF00FF","#00A4CCFF"])
st.pyplot()
st.write("The majority of participants are between the age of 18-25 years old, or classified as Young Adults.")




#General one
st.write("***")
st.write("""## WHEN DO PEOPLE GO TO SLEEP? """)
st.set_option('deprecation.showPyplotGlobalUse', False)
sns.countplot(y = df["What time do you usually go to sleep?"], data = df, color="#EDFF00FF")
st.pyplot()
st.write(""" We can see that majority of the people in the study go to sleep around midnight. 

""")

st.write("***")

#General two
st.write("""## WHEN DO PEOPLE WAKE UP? """)
st.set_option('deprecation.showPyplotGlobalUse', False)
sns.countplot(y = df["What time do you usually wake up?"], data = df, color="#FF3EA5FF")
st.pyplot()
st.write("People usually prefer waking up between 7:00 a.m. to 9:00 a.m. Since the data largely represents university students, this could be attributed to early classes students have.")

st.write("***")





st.write("## GENERAL RESPONSES")
option = st.selectbox(
'See what majority of the people are doing',
(df.columns[1:]))
ax = sns.countplot(y = df[option], data = df, color="#00A4CCFF")
plt.show()
st.pyplot()



st.write("## GROUPED TRENDS")
st.write("Choose a main question and then select the data to group by to see the stacked bar graph.")
option_group = st.selectbox(
'Select a question',
(df.columns[1:]))
group = (df.drop(option_group,axis=1)).columns[1:]
group_choose = st.radio("Group by ", group)
df_plot = df.groupby([group_choose, option_group]).size().reset_index().pivot(columns=group_choose,index=option_group, values=0)
df_plot.plot(kind='bar', stacked=True, color= ["#FF3EA5FF","#EDFF00FF","#00A4CCFF","#0C6291", "#EF476F"])
st.pyplot()
st.write("***")


st.write("## CORRELATION")
st.write("""Since all of our values are categorical, we will perform the [chi-square] (https://towardsdatascience.com/chi-square-test-with-python-d8ba98117626)
test to measure the dependency between the parameters.
Learn more about [corrleation](https://www.khanacademy.org/math/statistics-probability/describing-relationships-quantitative-data/scatterplots-and-correlation/a/correlation-coefficient-review).
""")

st.write("### Correlation between morning larks or night owls and introvertness and extrovertness.")




# create contingency table
data_crosstab = pd.crosstab(df['Do you categorise yourself as a morning lark or a night owl? '],
                            df['Do you categorise yourself more as an introvert or an extrovert ?'],
                            margins=True, margins_name="Total")
st.write(data_crosstab)

# significance level
alpha = 0.05

# Calcualtion of Chisquare test statistics
chi_square = 0
rows = df['Do you categorise yourself as a morning lark or a night owl? '].unique()
columns = df['Do you categorise yourself more as an introvert or an extrovert ?'].unique()
for i in columns:
    for j in rows:
        O = data_crosstab[i][j]
        E = data_crosstab[i]['Total'] * data_crosstab['Total'][j] / data_crosstab['Total']['Total']
        chi_square += (O-E)**2/E

# The p-value approach
print("Approach 1: The p-value approach to hypothesis testing in the decision rule")
p_value = 1 - stats.norm.cdf(chi_square, (len(rows)-1)*(len(columns)-1))
conclusion = "Failed to reject the null hypothesis."
if p_value <= alpha:
    conclusion = "Null Hypothesis is rejected."
        
st.write("chisquare-score is:", chi_square, " and p value is:", p_value)
st.write(conclusion)
    


st.write("This shows that there is no correlation between the preference of being a morning lark or a night owl, with the introvertness or extrovertness of character.")

st.write("### Correlation between if people wished to have more hours of sleep and introvertness and extrovertness.")


# create contingency table
data_crosstab = pd.crosstab(df['Do you wish you had more hours of sleep?'],
                            df['Do you categorise yourself more as an introvert or an extrovert ?'],
                            margins=True, margins_name="Total")

# significance level
alpha = 0.05

# Calcualtion of Chisquare test statistics
chi_square = 0
rows = df['Do you wish you had more hours of sleep?'].unique()
columns = df['Do you categorise yourself more as an introvert or an extrovert ?'].unique()
for i in columns:
    for j in rows:
        O = data_crosstab[i][j]
        E = data_crosstab[i]['Total'] * data_crosstab['Total'][j] / data_crosstab['Total']['Total']
        chi_square += (O-E)**2/E
st.write(data_crosstab)

# The p-value approach
print("Approach 1: The p-value approach to hypothesis testing in the decision rule")
p_value = 1 - stats.norm.cdf(chi_square, (len(rows)-1)*(len(columns)-1))
conclusion = "Failed to reject the null hypothesis."
if p_value <= alpha:
    conclusion = "Null Hypothesis is rejected."
        
st.write("chisquare-score is:", chi_square, " and p value is:", p_value)
st.write(conclusion)
    

st.write("This test shows that there is a dependency between the two variables. Majority of introverts answered yes to desiring more hours of sleep as compared to extroverts.")
