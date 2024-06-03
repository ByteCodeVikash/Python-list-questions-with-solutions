#Python program to print negative numbers in a list

#using simple if method

list1=[-21,25,67,-2,-1,93]

for i in list1:
    if i<0:
        print(i,end=',')


#using list comperhension

list1=[22,-93,34,-8,-6,45,-1]

neg_nos=[num for num in list1 if num<0]

print("Negative number in the list",neg_nos)