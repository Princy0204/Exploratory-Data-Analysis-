#!/usr/bin/env python
# coding: utf-8

# In[24]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv("heart_disease_health_indicators_BRFSS2015.csv")


# In[25]:


#loading dataset
df.head()


# In[26]:


#shape of the data
df.shape


# In[27]:


#size of data 
df.size


# In[28]:


#data information
df.info()


# In[29]:


#describing the data
df.describe()


# In[30]:


#column of data
df.columns


# In[31]:


df.values


# In[32]:


type(df.values)


# In[33]:


#column to list
df.columns.tolist()


# In[34]:


# to drop columns:
df=df.drop(['Fruits','Veggies'],axis=1)


# In[35]:


df.head()


# In[36]:


#check for missing values:
df.isnull().sum()


# In[37]:


#checking for duplicate values:
df.nunique()


# In[38]:


#visualization of column data
for i in df.columns:
    plt.figure(figsize=(2,1))
    sns.countplot(data =df, x=i)
    plt.show()


# In[39]:


#histogram 
sns.histplot(df['Age'])
plt.xlabel('Age')
plt.ylabel('PhysHlth')
plt.title('Distribution of Age')
plt.show()
# provides insight into how ages are distributed among the surveyed individuals, potentially correlating this distribution with their physical health status.


# In[40]:


#scatterplot 
sns.scatterplot(x='Age', y='MentHlth', data=df)
plt.xlabel('Age')
plt.ylabel('MentHlth')
plt.title('Age vs. MentHlth')
plt.show()
#scatter plot provides a visual representation of the relationship between age and mental health 


# In[41]:


#violin plot
plt.figure(figsize=(8, 6))
sns.violinplot(x='Sex', y='Age', data=df)
plt.title('Violin Plot')
plt.xlabel('Sex')
plt.ylabel('Age')
plt.show()
# provides a comprehensive visualization of the distribution of ages for males and females allowing for comparisons and insights into age


# In[42]:


#boxplot
sns.boxplot(x='Age',y='Education',data=df)

#relationship between education level and age distributions vary across different education levels


# In[43]:


#heatmap
plt.figure(figsize=(15,10))
#using seaborn to create heatmap
sns.heatmap(df.corr(),annot=True,fmt='.2f',cmap='Pastel2',linewidths=2)
plt.title('correlation heatmap')
plt.show()
#Each cell in the heatmap represents the correlation coefficient between two variables. 
#Darker shades indicate stronger correlations
#Lighter shades suggest weaker correlations. 
#observing clusters of dark-colored cells, indicating strong correlations among a group of variables. 


# In[21]:


#jointplot
sns.jointplot(x='Education', y='Income', data=df, kind='scatter')
plt.show()

