#Python | Program to convert String to a List

#using list

s="this is string"
l=list(s)
print(l)

#using list comprehension

string1="Vikash"
list1=[i for i in string1]
print(list1)

#using split method

def convert(string):

    list1=list(string.split(" "))

    return list1

li="this is split string"
print(convert(li))