#Python Program to Convert a List to String

#using for loop

def listtostring(s):

    str1=""

    for ele in s:
        str1+=ele

    return str1 

s=["This","is","a","boy"]

print(listtostring(s))

#using list comprehension

s=['I','want',4,'apple','and',18,'banana']

listtostr=' '.join([str(ele) for ele in s])

print(listtostr)