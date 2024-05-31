#Python | Sum of number digits in List

test_list=[12,1234,23,45,67]

print("This is original list is"+str(test_list))

res=[]

for ele in test_list:
    sum=0
    for digit in str(ele):
        sum+=int(digit)
    res.append(sum)

print("List integer summation"+str(res))        
