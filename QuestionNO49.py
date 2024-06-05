#Python | Ways to create a dictionary of Lists

d=dict((val,range(int(val),int(val)+2))
       for val in ['1','2','3'])

print(d)