#Python | Get unique values from a list

# using traversal method

def unique(list1):

    unique_list=[]

    for i in list1:
        if i not in unique_list:
            unique_list.append(i)

    for i in unique_list:
        print(i)


list1=[1,2,3,4,5,1,1,1,3,4,2]
print("The unique list form the fist list")
unique(list1)

list2=[2,3,4,5,2,3,7,8,1,2,2]
print("\nth unique value from the 2nd list")
unique(list2)

#using set

def unique(list1):

    unique_set=set(list1)

    unique_list=list(unique_set)

    for i in unique_list:
        print(i)


list1=[1,2,3,4,1,1,2,3,6,7,1]
print("The unique element from the first element")
unique(list1)

list2=[7,5,8,6,6,7,1,2,3,1,7,8,9]
print("\nth value from the 2nd list")
unique(list2)