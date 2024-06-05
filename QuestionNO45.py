#Find average of a list in python

def average(list1):
    return sum(list1)/len(list1)

list1=[1,2,3,4,5]
avg=average(list1)

print("Average of the list= ",round(avg,2))