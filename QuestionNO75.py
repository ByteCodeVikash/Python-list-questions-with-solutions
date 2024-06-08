#Python – Check if a list is empty or not

def Enqury(lst):
    if len(lst)==0:
        return 0
    else:
        return 1
lst=[]
if Enqury(lst):
    print("this list is not empty")
else:
    print("this list is empty")        
