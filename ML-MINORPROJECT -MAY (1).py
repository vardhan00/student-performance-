#!/usr/bin/env python
# coding: utf-8

# ## Objective of this Analysis:
# 
# To understand the how the student's performance (test scores) is affected by the other variables (Gender, Ethnicity, Parental level of education, Lunch, Test preparation course).
#     
# ## What to do in  Exploratory Data Analysis:
# 
# 1.	To Analyse insights in the data set.
# 2.	To understand the connection between the variables and to uncover the underlying structure
# 3.	To extract the important Variables.
# 4.	To test the underlying assumptions.
# 5.	Provide Insights with Suitable Graphs and Visualizations.
# 6.	Write all your inferences with supporting Analysis and Visualizations.
# 

# In[3]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[4]:


passmark = 40


# Read the data from csv file

# In[14]:


df = pd.read_csv(r'C:\Users\Admin\Downloads\asd.csv')


# print the first five lines of data

# In[15]:


df.head()


# size of data frame

# In[16]:


print (df.shape)


# In[17]:


df.describe()


# checking the missing values

# In[18]:


df.isnull().sum()


# In[41]:


plt.rcParams['figure.figsize'] = (100, 100)
sns.set(font_scale=5) 
p = sns.countplot(x="math score", data = df, palette="muted")
_ = plt.setp(p.get_xticklabels(), rotation=90) 


# In[21]:


df['Math_PassStatus'] = np.where(df['math score']<passmark, 'F', 'P')
df.Math_PassStatus.value_counts()


# In[62]:


plt.rcParams['figure.figsize'] = (10, 5)
sns.set(font_scale=1) 
p = sns.countplot(x='parental level of education', data = df, hue='Math_PassStatus', palette='bright')
_ = plt.setp(p.get_xticklabels(), rotation=90)


# In[96]:


plt.rcParams['figure.figsize'] = (10, 5)
sns.set(font_scale=1) 
p = sns.countplot(x='gender', data = df, hue='Math_PassStatus', palette='bright')
_ = plt.setp(p.get_xticklabels(), rotation=90) 


# In[97]:


plt.rcParams['figure.figsize'] = (10, 5)
sns.set(font_scale=1) 
p = sns.countplot(x='race/ethnicity', data = df, hue='Math_PassStatus', palette='bright')
_ = plt.setp(p.get_xticklabels(), rotation=90) 


# In[98]:


plt.rcParams['figure.figsize'] = (10, 5)
sns.set(font_scale=1) 
p = sns.countplot(x='lunch', data = df, hue='Math_PassStatus', palette='bright')
_ = plt.setp(p.get_xticklabels(), rotation=90) 


# In[99]:


plt.rcParams['figure.figsize'] = (10, 5)
sns.set(font_scale=1) 
p = sns.countplot(x='test preparation course', data = df, hue='Math_PassStatus', palette='bright')
_ = plt.setp(p.get_xticklabels(), rotation=90) 


# In[64]:


plt.rcParams['figure.figsize'] = (100, 100)
sns.set(font_scale=5) 
sns.countplot(x="reading score", data = df, palette="muted")
plt.show()


# In[24]:


df['Reading_PassStatus'] = np.where(df['reading score']<passmark, 'F', 'P')
df.Reading_PassStatus.value_counts()


# In[25]:


p = sns.countplot(x='parental level of education', data = df, hue='Reading_PassStatus', palette='bright')
_ = plt.setp(p.get_xticklabels(), rotation=90)


# In[100]:


p = sns.countplot(x='gender', data = df, hue='Reading_PassStatus', palette='bright')
_ = plt.setp(p.get_xticklabels(), rotation=90)


# In[101]:


p = sns.countplot(x='race/ethnicity', data = df, hue='Reading_PassStatus', palette='bright')
_ = plt.setp(p.get_xticklabels(), rotation=90)


# In[102]:


p = sns.countplot(x='lunch', data = df, hue='Reading_PassStatus', palette='bright')
_ = plt.setp(p.get_xticklabels(), rotation=90)


# In[103]:


p = sns.countplot(x='test preparation course', data = df, hue='Reading_PassStatus', palette='bright')
_ = plt.setp(p.get_xticklabels(), rotation=90)


# In[44]:


plt.rcParams['figure.figsize'] = (100, 100)
sns.set(font_scale=5)
p = sns.countplot(x="writing score", data = df, palette="muted")
_ = plt.setp(p.get_xticklabels(), rotation=90) 


# In[27]:


df['Writing_PassStatus'] = np.where(df['writing score']<passmark, 'F', 'P')
df.Writing_PassStatus.value_counts()


# In[28]:


p = sns.countplot(x='parental level of education', data = df, hue='Writing_PassStatus', palette='bright')
_ = plt.setp(p.get_xticklabels(), rotation=90) 


# In[104]:


p = sns.countplot(x='gender', data = df, hue='Writing_PassStatus', palette='bright')
_ = plt.setp(p.get_xticklabels(), rotation=90) 


# In[105]:


p = sns.countplot(x='race/ethnicity', data = df, hue='Writing_PassStatus', palette='bright')
_ = plt.setp(p.get_xticklabels(), rotation=90) 


# In[106]:


p = sns.countplot(x='lunch', data = df, hue='Writing_PassStatus', palette='bright')
_ = plt.setp(p.get_xticklabels(), rotation=90) 


# In[107]:


p = sns.countplot(x='test preparation course', data = df, hue='Writing_PassStatus', palette='bright')
_ = plt.setp(p.get_xticklabels(), rotation=90) 


# In[117]:


plt.rcParams['figure.figsize'] = (20, 20)
sns.set(font_scale=1) 
plt.subplot(251)
plt.title('With Gender',fontsize = 15)
sns.countplot(hue="test preparation course", x="gender", data=df)
plt.subplot(254)
plt.title('With Parental Level Of Education',fontsize = 15)
sns.countplot(hue="test preparation course", y="parental level of education", data=df)
plt.subplot(253)
plt.title('With Lunch',fontsize = 15)
sns.countplot(hue="test preparation course", x="lunch", data=df)
plt.subplot(252)
plt.title('With Ethnicity',fontsize = 15)
sns.countplot(hue="test preparation course", y="race/ethnicity", data=df)
plt.show()


# In[29]:


df['OverAll_PassStatus'] = df.apply(lambda x : 'F' if x['Math_PassStatus'] == 'F' or 
                                    x['Reading_PassStatus'] == 'F' or x['Writing_PassStatus'] == 'F' else 'P', axis =1)

df.OverAll_PassStatus.value_counts()


# In[32]:


df['Total_Marks'] = df['math score']+df['reading score']+df['writing score']
df['Percentage'] = df['Total_Marks']/3


# In[57]:


def GetGrade(Percentage, OverAll_PassStatus):
    if ( OverAll_PassStatus == 'F'):
        return 'F'    
    if ( Percentage >= 80 ):
        return 'A'
    if ( Percentage >= 70):
        return 'B'
    if ( Percentage >= 60):
        return 'C'
    if ( Percentage >= 50):
        return 'D'
    if ( Percentage >= 40):
        return 'E'
    else: 
        return 'F'

df['Grade'] = df.apply(lambda x : GetGrade(x['Percentage'], x['OverAll_PassStatus']), axis=1)

df.Grade.value_counts()


# In[35]:


sns.countplot(x="Grade", data = df, order=['A','B','C','D','E','F'],  palette="muted")
plt.show()


# In[36]:


p = sns.countplot(x='parental level of education', data = df, hue='Grade', palette='bright')
_ = plt.setp(p.get_xticklabels(), rotation=90)


# In[108]:


p = sns.countplot(x='gender', data = df, hue='Grade', palette='bright')
_ = plt.setp(p.get_xticklabels(), rotation=90)


# In[109]:


p = sns.countplot(x='race/ethnicity', data = df, hue='Grade', palette='bright')
_ = plt.setp(p.get_xticklabels(), rotation=90)


# In[110]:


p = sns.countplot(x='lunch', data = df, hue='Grade', palette='bright')
_ = plt.setp(p.get_xticklabels(), rotation=90)


# In[111]:


p = sns.countplot(x='test preparation course', data = df, hue='Grade', palette='bright')
_ = plt.setp(p.get_xticklabels(), rotation=90)

