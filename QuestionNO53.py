#Python | Convert number to list of integers


num=2019

print("this is original string",str(num))

res=[int(i) for i in str(num)]

print("the list of number in list",str(res))

#using enumerate

n=2029
res=[int(i) for a,i in enumerate(str(n))]
print(res)