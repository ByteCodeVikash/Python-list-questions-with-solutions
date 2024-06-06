#Python | Convert a string representation of list into list

ini_list="[1,2,3,4,5]"

print("initial list",ini_list)
print(type(ini_list))


res=ini_list.strip('][').split(',')

print("final list",res)
print(type(res))

#using eval method

ini_list='[1,2,3,4,5,6,7,8]'

print("initial list",ini_list)
print(type(ini_list))

res=eval(ini_list)

print("Final list",res)
print(type(res))