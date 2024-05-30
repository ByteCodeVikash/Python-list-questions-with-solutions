#Check if element exists in list in Python

def checkNO(list,number):

    if number in list:
        print("YES,this is present",number,"in the list")
    else:
        print("NO this is not present in the list")

list=[1,2,4,5,6] 
number=4
checkNO(list,number)           