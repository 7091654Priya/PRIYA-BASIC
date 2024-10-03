#!/usr/bin/env python
# coding: utf-8

# In[1]:


def countLines(name):
    with open(name,'r')as file:
        lines = file.readlines()
    return len(lines)

def countChars(name):
    with open(name,'r')as file:
        content = file.read()
    return len(content)

def test(name):
    num_Lines = countLines(name)
    num_Chars = countChars(name)
    print(f'file: {name}')
    print(f'Number of Lines:{num_Lines}')
    print(f'Number of Characters:{num_chars}')
    
if __name__ == "_main_":
    test( 'Test.txt')

