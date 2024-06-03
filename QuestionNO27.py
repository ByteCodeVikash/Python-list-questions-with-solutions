#Python program to count positive and negative numbers in a list

list1=[11,-2,-5,45,67,-3,-1]

neg_count,pos_count=0,0

for i in list1:

    if i>0:
        pos_count+=1
    else:
        neg_count+=1

print("List of postive count",pos_count)
print("List of negative count",neg_count)        
