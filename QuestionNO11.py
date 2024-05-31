#Python | Count occurrences of an element in a list

def countX(lst,x):
    return lst.count(x)

lst=[1,2,1,2,3,4,5,5,11,1,1,1]
x=1
print('{}has occurred{}times'.format(x,countX(lst,x)))