#Python | Merge list elements


test_list = ['I', 'L', 'O', 'V', 'E', 'G', 'F', 'G']


print ("The original list is : " + str(test_list))


test_list[5 : 8] = [''.join(test_list[5 : 8])]
 
print ("The list after merging elements : " + str(test_list))
