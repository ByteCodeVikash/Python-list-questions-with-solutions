#Reversing a List in Python

#using slicing mehtod

def revers(list1):

    new_list=list1[::-1]

    return new_list

list1=[1,2,3,4,5,6,7,8]
print(revers(list1))

#using revers method

My_list=[9,8,7,6,5,4,3,2,1]
My_list.reverse()

print("using reverse ()",My_list)

print("Using reverse()",list(reversed(My_list)))