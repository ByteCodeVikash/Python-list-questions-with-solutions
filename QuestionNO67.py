#Python | Split a sentence into list of words

lst='Hello world'
print(lst.split())

#using list comprehension

def convert(my_list):
    return ([i for i in my_list.split()])
My_list='this is list'
print(convert(My_list))