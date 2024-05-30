#Python | Cloning or Copying a list

'''using extend method'''

def cloning(l1):
    l1_copy=[]
    l1_copy.extend(l1)
    return l1_copy

l1=[1,2,3,4,5,6]
l2=cloning(l1)
print("Original list",l1)
print("Cloning list",l2)


'''Using Assignment Operator'''

def cloning(l1):
    l1_copy=l1
    return l1
l1=[1,2,3,4,5]
l2=cloning(l1)

print("Origianl list",l1)
print("After cloning list",l2)