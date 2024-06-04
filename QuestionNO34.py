#Python | Converting all strings in list to integers


lis=['1','2','3','4']
res=[eval(i) for i in lis]

print("Modified list is",res)

#using list comprehension

test_list=['1','2','3','4','5']

test_list=[int(ele) for ele in test_list]

print("Modified list is :" +str(test_list))