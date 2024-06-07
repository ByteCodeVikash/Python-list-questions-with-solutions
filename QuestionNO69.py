#Python Program to Convert a list of multiple integers into a single integer

My_list=[1,2,3,4,5,6]
for i in My_list:
    print(i,end='')

#using list comprehension


lst=[1,2,3,4,5,6,7]
s=[str(i) for i in lst]
print("".join(s))