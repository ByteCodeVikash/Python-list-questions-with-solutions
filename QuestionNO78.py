#Remove all the occurrences of an element from a list in Python


def remove_item(test_list,item):
    res=[i for i in test_list if i!=item]
    return res

if __name__=="__main__":
    test_list=[1,2,3,4,5,6]
    item=1
    print("The original list is :",str(test_list))
    res=remove_item(test_list,item)

    print("The list after performing the remove operation is:",str(res))