#!/usr/bin/env python
# coding: utf-8

# In[2]:


import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px


# In[5]:


tips = sns.load_dataset('tips')
tips


# In[8]:


sns.scatterplot(data=tips,x="total_bill",y="tip",hue="sex",style = "time",size = "size")


# In[10]:


gap = px.data.gapminder()
temp_df = gap[gap['country']=='India']
temp_df


# In[11]:


gap.head()


# In[12]:


gap.info()


# In[14]:


sns.lineplot(data = temp_df,x='year',y='lifeExp')


# In[15]:


gap = px.data.gapminder()
temp_df = gap[gap['country'].isin(['India','Brazil','Germany'])]
temp_df


# In[20]:


sns.relplot(kind='line',data=temp_df,x='year',y='lifeExp',hue='country',style ='continent',size = 'continent')


# In[28]:


sns.relplot(data=tips,x='total_bill',y="tip",kind= 'line',col='sex',row = 'day')


# In[24]:


sns.relplot(data=gap,x='lifeExp',y='gdpPercap',col='year',col_wrap = 3)


# In[29]:


sns.histplot(data=tips,x = 'total_bill')


# In[31]:


sns.kdeplot(data =tips ,x = 'total_bill')


# In[33]:


sns.displot(data =tips ,x = 'total_bill',y='tip',kind='hist')


# In[34]:


sns.kdeplot(data =tips ,x = 'total_bill',y='tip')


# In[37]:


temp_df = gap[gap['continent']=='Europe'].pivot(index='country',columns='year',values = 'lifeExp')
plt.figure(figsize=(15,15))
sns.heatmap(temp_df,annot=True,linewidth=0.5,cmap='summer')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




