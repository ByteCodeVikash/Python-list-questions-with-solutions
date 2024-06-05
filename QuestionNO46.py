#Python | Create list of numbers with given range

#using for loop

def createList(r1,r2):

    if (r1==r2):
        return r1
    else:
        res=[]

    while (r1<r2+1):
        res.append(r1)
        r1+=1
    return res

r1,r2=-1,1
print(createList(r1,r2))   


#using list comprehension

def createList(r1,r2):
    return [item for item in range(r1,r2+1)]

r1,r2=-1,1
print(createList(r1,r2))