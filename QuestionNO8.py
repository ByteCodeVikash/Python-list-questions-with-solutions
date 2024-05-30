#Different ways to clear a list in Python

list=[1,2,3,4,5]

print("List before clearing",list)

while (len(list)!=0):
    list.pop()
print("List after clearing",list)    