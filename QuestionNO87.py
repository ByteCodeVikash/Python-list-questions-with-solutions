#Python program to count Even and Odd numbers in a List

My_list=[1,2,3,4,5,6,7,8,9]

even_count,odd_count=0,0         

for i in My_list:
    if i %2==0:
        even_count+=1
    else:
        odd_count+=1    
        

print("Even numbers of the list",even_count)
print("Odd numbers   of the list",odd_count)
