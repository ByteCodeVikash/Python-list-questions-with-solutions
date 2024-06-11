#Python | Remove square brackets from list

test_list = [5, 6, 8, 9, 10, 21]
 

print("The original list is : " + str(test_list))
 

res = str(test_list)[1:-1]
 

print("List after removing square brackets : " + res)