#Different ways to clear a list in Python

test_list=[1,2,3,4,5,6,7,8,9]

print("Before clear list",test_list)

test_list.clear()

print("After clear list",test_list)

#Clear a List using Slicing

my_list=[9,8,7,6,5,4,3,2,1]

print("Before clear list",my_list)

my_list=my_list[:0]

print("After clear list",my_list)