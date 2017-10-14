
# coding: utf-8

# In[7]:

import pandas as pd


# In[8]:

url = 'http://higheredublog.com/top-universities-for-ms-in-mis-in-usa/'


# In[9]:

data = pd.read_html(url, header = 0)


# In[10]:

read_data = data[0]


# In[11]:

read_data.columns = ['RANKING', 'UNIVERSITY', 'PROGRAM']


# In[12]:

read_data.dtypes


# In[22]:

df = pd.DataFrame(read_data)


# In[23]:

df


# In[25]:

df.to_csv('univ_ranking.csv', index=False, encoding='utf-8')


# In[ ]:



