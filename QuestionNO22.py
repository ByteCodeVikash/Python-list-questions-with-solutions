#Python program to count Even and Odd numbers in a List

l1=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]

even_count,odd_count=0,0

for i in l1:
    if i%2==0:
        even_count+=1
    else:
        odd_count+=1

print("Even number in the list",even_count)
print("Odd number in the list",odd_count)            
