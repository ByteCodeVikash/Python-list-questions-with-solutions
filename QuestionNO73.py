#Python | Print all the common elements of two lists

def common_element(a,b):
    a_set=set(a)
    b_set=set(b)

    if(a_set&b_set):
        print(a_set & b_set)
    else:
        print("No common element")

a=[1,2,3,4,5]
b=[5,6,7,8,9]
common_element(a,b)            