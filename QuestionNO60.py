#How To Find the Length of a List in Python

test_list=[1,2,3,4,55,6]

length=len(test_list)
print(length)

#List Using Naive Method

My_list=[1,2,3,4,5,6,7,8,9]

print("this is orginal list",str(My_list))

counter=0
for i in My_list:
    counter=counter+1

print("length of list using naive method",str(counter))    