#Python program to print even numbers in a list

my_list=[1,2,3,4,4,5,6,7,7]

emp_list=[]

for i in my_list:
    if i % 2==0:
        emp_list.append(i)

print(emp_list)   


#using list comprehension

test_list=[9,8,7,6,5,4,3,2,1]

li=[i for i in test_list if i%2==0]

print(li,end=',')