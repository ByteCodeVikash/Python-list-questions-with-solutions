#Python program to print odd numbers in a List

list=[1,2,3,4,5,6,7,8,9]

for i in list:
    if i%2!=0:
        print(i,end=',')


#list comprehension

lst=[10, 21, 4, 45, 66, 93]  

res=[i for i in lst if i%2!=0]

print(res)