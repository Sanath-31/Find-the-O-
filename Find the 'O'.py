#!/usr/bin/env python
# coding: utf-8

# In[1]:


from random import shuffle


# In[2]:


mylist = [' ','O',' ']


# In[3]:


def shuffle_list(mylist):
    shuffle(mylist)
    return mylist


# In[4]:


shuffle_list(mylist)


# In[7]:


def player_guess():
    
    guess = ''
    
    while guess not in ['0','1','2']:
        guess = input("Pick a number from 0,1 or 2: ")
        
    return int(guess)


# In[8]:


my_index = player_guess()


# In[10]:


def check_guess(mylist,guess):
    if mylist[guess] == 'O' :
        print("Correct!")
    else:
        print("Oops, wrong guess!")
        print(mylist)


# In[13]:


#INITIAL LIST
mylist = [' ','O',' ']

#SHUFFLED LIST
mixedup_list = shuffle_list(mylist)

#USER GUESS
guess = player_guess()

#CHECK GUESS
check_guess(mixedup_list,guess)


# In[ ]:




