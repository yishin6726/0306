
# coding: utf-8

# In[2]:


import requests
response = requests.get("http://www.novelscape.net/wxxs/j/jingyong/ffwz/001.htm")
response.encoding = "big5"
book1 = response.text
book1


# In[4]:


book1.find('四')


# In[5]:


word = '四'
book1.count(word)

