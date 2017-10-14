
# coding: utf-8

# In[1]:

import pandas as pd


# In[7]:

url = 'http://blog.collegetuitioncompare.com/2013/08/top-10-management-information-systems-college-tuition-comaprison.html'


# In[8]:

data = pd.read_html(url, header = 0)


# In[9]:

read_data = data[0]


# In[10]:

read_data


# In[11]:

read_data.dtypes


# In[15]:

df = pd.DataFrame(read_data)


# In[17]:

df.to_csv('acceptance_stats', index=False, encoding='utf-8')


# In[ ]:



