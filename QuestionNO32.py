#Python | Convert a List into a Tuple

My_list=[1,2,3,4,5]

My_tuple=tuple(My_list)

print(My_tuple,type(My_tuple))

#second method

def convert(list):
    return tuple(i for i in list)

list=[1,2,3,4]

print(convert(list))