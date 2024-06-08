#Python | Cloning or Copying a list

#using slicing method

def cloning(l1):
    copy_li=l1[:]
    return copy_li

l1=[1,2,3,4,4,5,6,7]
l2=cloning(l1)
print("Original list",l1)
print("After cloning list",l2)

#using assignment operator 

def copy(lst):
    copy_list=lst
    return copy_list
lst=[9,8,7,6,5,4,3,2,1]
l2=copy(lst)
print("this is orignal list",lst)
print("this is copy list",l2)