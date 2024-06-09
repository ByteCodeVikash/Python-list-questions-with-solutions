#Python | Check if one list is subset of other


test_list=[9,4,5,8,10]
sub_list=[10,5,4]

print("This is original list",str(test_list))
print("this is original list",str(sub_list))

flag=0

if (all(x in test_list for x in sub_list)):
    flag=1


if (flag):
    print("Yes,list is subset of other")
else:
    print("No,list is not subset of other")    