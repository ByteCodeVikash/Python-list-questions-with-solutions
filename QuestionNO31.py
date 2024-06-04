#Python | Convert set into a list

set={1,2,4,5,6}

my_list=list(set)

print(my_list)

#using list comprehension

def convert(s):
    return [ele for ele in s]

s={1,2,3,4}

print(convert(s))