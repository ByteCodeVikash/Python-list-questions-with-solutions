#Check if element exists in list in Python
#using 'in' statement

my_list=[1,2,3,4,5,6]

i=5

if i in my_list:
    print("Exist")
else:
    print("Not exist")   

#using loop

thislist=[11,22,33,44]

for i in thislist:
    if i == 33:
        print("this is present")