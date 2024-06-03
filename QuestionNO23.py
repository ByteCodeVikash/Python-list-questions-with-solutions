#Python program to print positive numbers in a list

l1=[1,2,3,4,5,6,7,-1,-2,-5]

for i in l1:
    if i>0:
        print(i,end=',')


#using list comperhension

list1=[-10,-21,-4,45,-66,93]

pos_nos=[num for num in list1 if num>0]

print("postive number in the list",pos_nos)