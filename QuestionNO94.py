#Python | Replace substring in list of strings

test_list = ['4', 'kg', 'butter', 'for', '40', 'bucks']
 
 
print("The original list : " + str(test_list ))
 

res = [sub.replace('4', '1') for sub in test_list]
     

print("The list after substring replacement : " + str(res))