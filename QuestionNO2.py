#Python program to swap two elements in a list

def swapPostion(list,pos1,pos2):

    list[pos1],list[pos2]=list[pos2],list[pos1]

    return list
list=[1,2,3,4,5]
pos1,pos2=1,3

print(swapPostion(list,pos1,pos2))