#Python | Multiply all numbers in the list

#using traversal method

def multi(my_list):

    result=1
    for i in my_list:
        result=result*i
    return result

l1=[1,2,3,4]
l2=[4,5,6,7]
print(multi(l1))
print(multi(l2))    


#using for loop

def multiply(list1):
    product=1

    for i in list1:
        product*=i
    return product

list1=[1,2,3,4,5]
result=multiply(list1)
print(result)    