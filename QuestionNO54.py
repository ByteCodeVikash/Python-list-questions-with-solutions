#Python | Remove None values from list

test_list=[1,None,3,4,None,6,1,None,None,None,6,9,2,4,None]

print("this is original list",str(test_list))

res=[]

for i in test_list:
    if i!=None:
        res.append(i)

print("this is after removal none in list",str(res))

#using list comprehension

my_list=[None,3,1,4,None,None,None,9,2,4,6,None,None]

print("this is orginal list",str(my_list))

res=[i for i in my_list if i is not None]

print("this is after removal None list",str(res))
