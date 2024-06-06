#Python Program to Accessing index and value in list

test_list=[1,2,3,4,5,6,7]

print("this is original list",str(test_list))

print("List index-value are:")
for i in range(len(test_list)):
    print(i,end=' ')
    print(test_list[i])


#using list comprehension

My_list=[1,2,3,4,5,6,7] 

print("This is original list",str(My_list))

print("List index-value:")

print([list((i,test_list[i]))for i in range(len(My_list))])