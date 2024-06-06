#Python | How to get the last element of list

test_list=[1,2,3,4,5,6]

print("this is orginal list",str(test_list))

for i in range(0,len(test_list)):
    if i==len(test_list)-1:
        print("the last element find using loop",str(test_list[i]))