#Python | Check if two lists are identical

test_list1=[1,2,3,4,5]
test_list2=[1,2,3,4,5]

print("this is orginal list list1",str(test_list1))
print("this is orginal list list2",str(test_list2))

test_list1.sort()
test_list2.sort()

if test_list1==test_list2:
    print("this is indentical list")
else:
    print("this is not indentical list")    