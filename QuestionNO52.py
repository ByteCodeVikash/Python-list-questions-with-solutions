#Python | Find most frequent element in a list

def frequent(list):

    counter=0
    num=list[0] 

    for i in list:
        curr_freliquency=list.count(i)
        if (curr_freliquency>counter):
            counter=curr_freliquency
            num=i
    return num

list=[1,2,4,5,2,3,4,2,3,9,2]
print(frequent(list))        


#pythonic Naive approach

def most_freuent(list):
    return max(set(list),key=list.count) 

list=[1,2,4,7,9,1,1,2,3,6]
print(most_freuent(list))      