#Python | Get first element of each sublist

def Extract(lst):
    return [item[0] for item in lst]
     

lst = [[1, 2], [3, 4, 5], [6, 7, 8, 9]]
print(Extract(lst))