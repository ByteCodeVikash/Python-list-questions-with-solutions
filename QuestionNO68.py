#Python | Remove empty strings from list of strings

test_list=["","I","am","","","is","","best"]

print("this is original list",str(test_list))

while("" in test_list):
    test_list.remove("")

print("modified list is",str(test_list))  

#using list comprehension

my_list=["","","You","are","","not","best","",""]
print("This is original string",str(my_list))

res=[i for i in my_list if i]

print("Modified list",str(res))