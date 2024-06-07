#Python | Append String to list

test_list=[1,2,3,4,5]

test_str="apple"

print("this is original list",str(test_list))
print("this is original string ",str(test_str))

test_list.append(test_str)

print("the list after appending is",str(test_list))

#using '+' operator

my_list=[1,2,3,4,5,6]

my_str='banana'

print("this is original list",str(my_list))
print("this is original string",str(my_str))

my_list+=[my_str]

print("The list after appending is",str(my_list))