#Python program to interchange first and last elements in a list


def swaplist(new_list):

    size=len(new_list)

    temp=new_list[0]

    new_list[0]=new_list[size-1]
    new_list[size-1]=temp
    return new_list

new_list=[1,2,3,4,5]

print(swaplist(new_list))