#Remove Special Characters from String Python

string="Ge;ek * s:fo ! r;Ge * e*k:s !"

test_str=''.join (i for i in string if i.isalnum())

print(test_str)