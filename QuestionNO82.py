#Python | Remove all values from a list present in other list

test_list=[1,2,3,4,5,6,7]

remove_list=[2,3,6]

print("this is original list",str(test_list))

print("this is original list",str(remove_list))

res=[i for i in test_list if i not in remove_list]

print("the list after performing remove operation",str(res))