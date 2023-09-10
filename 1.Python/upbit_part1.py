#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import pandas as pd


# ## 1. Parse data

# In[2]:


url = "https://th-api.upbit.com/v1/candles/days?market=THB-BTC&count=200"
headers = {}


# In[3]:


response = requests.get(url)
data = response.json()
df = pd.DataFrame(data)


# In[4]:


df.info()


# In[5]:


df.head()


# In[6]:


result_df = pd.DataFrame()
result_df['timestamp'] = df['candle_date_time_utc']
result_df['open'] = df['opening_price']
result_df['high'] = df['high_price']
result_df['low'] = df['low_price']
result_df['close'] = df['prev_closing_price']


# In[7]:


result_df


# ## 2. calculate and display

# ### maximum_closing_price

# In[8]:


maximum_closing_price = result_df['close'].max()
maximum_closing_price_rows = result_df[result_df['close'] == maximum_closing_price]
print(maximum_closing_price_rows)


# ### minimum_closing_price

# In[9]:


minimum_closing_price = result_df['close'].min()
minimun_closing_price_rows = result_df[result_df['close'] == minimum_closing_price]
print(minimun_closing_price_rows)


# ### average closing price

# In[10]:


avg_price = result_df['close'].mean()
print(avg_price)


# ## 3. price changing

# In[11]:


result_df['price_changing'] = result_df['close'].diff()
result_df


# ## 4. Filter table 

# In[12]:


filterd_df = result_df[result_df['price_changing']>10000]
filterd_df = filterd_df.head()


# ## 5. Correlation price_changing and high

# In[13]:


correlation = filterd_df['price_changing'].corr(filterd_df['high'])


# In[14]:


correlation


# In[15]:


filterd_df.to_csv('upbit_data.csv')

