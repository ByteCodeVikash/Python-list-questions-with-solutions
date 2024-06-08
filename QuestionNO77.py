#Python | Union of two or more Lists

def union(list1,list2):
    final_list=list1+list2
    return final_list

list1=[1,2,3,4,5]
list2=[6,7,8,9,10]
print(union(list1,list2))

#using sorted method

def Union_lst(lst1,lst2):
    final_list=sorted(lst1+lst2)
    return final_list
lst1=[11,22,33,44,55]
lst2=[66,77,88,99]
print(Union_lst(lst1,lst2))