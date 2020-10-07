#!/usr/bin/env python
# coding: utf-8

# In[27]:


import numpy as np
import pandas as pd

import matplotlib as mpl
import matplotlib.pyplot as plt

get_ipython().run_line_magic('matplotlib', 'inline')


# In[36]:


covid_data = pd.read_csv('https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv')


# In[37]:


covid_data.head()


# In[38]:


pd.to_datetime(covid_data['date'])


# In[39]:


cov_data_sort = covid_data.sort_values(['state','date'])


# In[40]:


cov_data_sort['del_cases'] = cov_data_sort['cases'].diff()
cov_data_sort['del_deaths'] = cov_data_sort['deaths'].diff()


# In[41]:


cov_data_sort.head()


# In[ ]:





# In[43]:


# looping through each unique state
for st in cov_data_sort.state.unique():
    
    # creating the data frame filtered to a single state
    plot_data = cov_data_sort[cov_data_sort['state']==st]
    
    # which data will be plotted
    x = plot_data['date']
    y1 = plot_data['del_cases'].rolling(7,min_periods=1,center=True).mean()  # 7-day moving average
    y2 = plot_data['del_cases']
    y3 = plot_data['del_deaths'].rolling(7,min_periods=1,center=True).mean() # 7-day moving average
    y4 = plot_data['del_deaths']
    
    
    # creating the subplot with 1 axis    
    fig, ax1 = plt.subplots(figsize=(45,7))
    
    # formatting the first y-axis and x-axis
    ax1.set_title(f'{st} Covid Cases and Deaths', fontsize=25)
    ax1.set_xlabel('Date', fontsize=20)
    ax1.set_ylabel('Daily Cases', color='blue', fontsize=20)
    plt.xticks(rotation=45,ha='right')
    ax1.set_ylim(0,y2.max())
    
    ax1.spines['left'].set_color('blue')
    ax1.tick_params(axis='y', colors='blue')
    ax1.legend(['Cases: 7-day Average'],loc='upper left')
    
    # plots the first y-axis data
    ax1.plot(x, y1, color='blue')
    ax1.bar(x, y2, color='blue', alpha=.3)
      
    # creating the 2nd y-axis with an x-axis shared with the first y-axis
    ax2 = ax1.twinx()    
    
    # formatting the second y-axis
    ax2.set_ylabel('Daily Deaths', color='red', fontsize=20)
    ax2.set_ylim(0,y3.max()*3)
        
    ax2.spines['right'].set_color('red')
    ax2.tick_params(axis='y', colors='red')
    ax2.legend(['Deaths: 7-day Average'],loc='upper right')
    
    # plots the second y-axis data
    ax2.plot(x, y3, color='red')
    ax2.bar(x, y4, color='indianred')
                
    plt.grid(True)
    
    #plt.show()
    plt.savefig(f"state_covid_plots\{st}_Covid_Data.png")
    
    plt.close()
    

