#Python | Multiply all numbers in the list

def multiplyList(mylist):

    result=1

    for i in mylist:
        result=result*i

    return result

list1=[1,2,3,4,5]
list2=[2,3,4,6,7]

print(multiplyList(list1))
print(multiplyList(list2))