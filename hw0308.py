
# coding: utf-8

# In[1]:


weekdays_list = ['一','二','三','四','五']
weekdays_list[0] = 'a'
weekdays_list


# In[2]:


weekdays_list = ('一','二','三','四','五')
list(weekdays_list)


# In[3]:


a = [[[1,'a',2,'b'],'c'],'d']
a


# In[4]:


a[0][0][3]


# In[9]:


a = ['a','b','c']
b = ['aa','bb','cc']
a += b
a


# In[10]:


a = ['a','b','c']
b = ['aa','bb','cc']
a.append(b)
a


# In[11]:


a = ['a','b','c']
b = ['aa','bb','cc']
a.insert(2,'1')
a


# In[12]:


a = ['a','b','c']
b = ['aa','bb','cc']
del a[0]
a


# In[13]:


a = ['a','b','c']
a.remove('b')
a


# In[15]:


a = ['a','b','c']
a.index('a')


# In[16]:


a = ['a','b','c']
'b' in a


# In[17]:


a = ['a','b','c','a','a','a','c','d']
a.count('a')


# In[19]:


a = ['c','a','e','b']
a.sort()
a


# In[20]:


a.sort(reverse=True)
a


# In[21]:


a = ['c','a','e','b']
a


# In[22]:


b=a
b


# In[23]:


a[0] = '0'
a


# In[24]:


b


# In[25]:


a = ['c','a','e','b']
b = a.copy()
b


# In[28]:


roles = ('⽢甘道夫', '亞拉岡', '索倫倫', '勒勒苟拉斯', '亞玟')
a,b,c,d,e = roles
a


# In[29]:


school = [("班級","甲班"),("姓名","⽢甘道夫"),("學號","110999")]
dict(school)


# In[31]:


class_ntust = {"member1" : "⽢甘道夫","member2" : "亞拉岡","member3" : "索倫",}
class_ntust


# In[32]:


class_ntust['member1'] ='XXX'
class_ntust


# In[33]:


class_ntust1 = {"member1" : "⽢甘道夫","member2" : "亞拉岡","member3" : "索倫",}
class_ntust1


# In[34]:


class_ntust.update(class_ntust1)
class_ntust


# In[39]:


f = {'a':1,'b':2}
f


# In[40]:


f.clear()
f


# In[41]:


class_ntust = {"member1" : "⽢甘道夫","member2" : "亞拉岡","member3" : "索倫",}
class_ntust.keys()


# In[42]:


class_ntust.values()


# In[43]:


class_ntust.items()


# In[44]:


set('letters') 


# In[45]:


drinks = {"item1" : {"珍珠奶茶","紅茶"},
          "item2" : {"烏龍奶茶","烏龍茶"},
          "item3" : {"蜂蜜紅茶","紅茶"},
         }
drinks


# In[46]:


for name, contents in drinks.items():
    if '紅茶' in contents:
        print (name)


# In[47]:


drinks = {"item1" : {"珍珠奶茶","紅茶"},
          "item2" : {"烏龍奶茶","烏龍茶"},
          "item3" : {"蜂蜜紅茶","紅茶"},
         }
drinks


# In[49]:


for name, contents in drinks.items():
    if ('紅茶' in contents) and not ('珍珠奶茶' in contents):
        print (name,contents)


# In[51]:


a = {1,2}
b = {2,3}
a&b


# In[52]:


a|b


# In[53]:


a - b


# In[54]:


a^b


# In[57]:


marxes = ['Groucho', 'Chico', 'Harpo']
marxes.append('XXX')
marxes


# In[58]:


marxes.pop()
marxes


# In[59]:


marxes = ['Groucho', 'Chico', 'Harpo']
marxes.insert(0, 'Zeppo')
marxes


# In[60]:


marxes.pop(0)


# In[63]:


a = [1,2,3,4,4]
len(set(a)) != len(a)


# In[64]:


x = input('請輸入數字');len(set(x)) != len(x)


# In[71]:


tony = "fafa"
may = "mama"
if tony == "mama":
    if may == "mama":
        print("他是mama沒錯")
    else:
        print("他是企業家") 
else:
    if may == "mama":
        print("他是mama沒錯")
    else:
        print("他是企業家")
    


# In[72]:


count = 1
while count <= 10:
    print(count)
    count += 1


# In[73]:


while True:
    name = input("猜?按q取消")
    if name == "q":
        break
        print('aaa')


# In[ ]:


x = input('請輸入數字')
if x == 6:
    break

