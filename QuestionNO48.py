#Get first and last elements of a list in Python

my_list=[1,2,3,4,5,6]

print("Original list",str(my_list))

res=my_list[::len(my_list)-1]

print("The first and last element of the list are:",str(res))