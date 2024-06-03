#Remove multiple elements from a list in Python

list1=[11,5,17,18,23,50]

for i in list1:
    if i%2==0:
        list1.remove(i)

print("New list after removing all even number:",list1) 


#list comprehension

list1 = [11, 5, 17, 24, 5, 6, 86, 23]
new_list = [i for i in list1 if i % 2 != 0]

print("New list after removing all even numbers:", new_list)
