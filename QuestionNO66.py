#Python | Test if string contains element from list

test_string="There are 2 apple for 4 person"

test_list=['apple','orange']

print("this is original string",str(test_string))

print("this is original list",str(test_list))

res=[i for i in test_list if (i in test_string)]

print("yes! this is present in list",str(bool(res)))