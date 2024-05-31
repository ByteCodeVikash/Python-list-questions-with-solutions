#Python program to print odd numbers in a List

lst=[1,2,3,4,5,6,7,8,9]

emp_lst=[]

for i in lst:
    if i%2!=0:
        emp_lst.append(i)

print(emp_lst)        