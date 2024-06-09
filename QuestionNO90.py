#Python | Maximum and minimum element’s position in a list

my_list=[8,7,10,5]

min_ele, max_ele = my_list[0], my_list[0]
 
for i in range(1, len(my_list)):
    if my_list[i] < min_ele:
        min_ele = my_list[i]
         
    if my_list[i] > max_ele:
        max_ele = my_list[i]
         
print('Minimum Element in the list', my_list, 'is', min_ele)
print('Maximum Element in the list', my_list, 'is', max_ele)

