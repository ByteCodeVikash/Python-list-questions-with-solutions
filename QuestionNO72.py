#Python program to sort a list of tuples by second Item

#using sort()method

def Sort_tuple(tup):
    tup.sort(key=lambda x:x[1])
    return tup

tup=[('shiva',10),('viku',9),('jalaj',44),('nikil',33)]
print(Sort_tuple(tup))

#using sorted method

def Sort_tup(tupl):
    return(sorted(tupl,key=lambda x:x[1]))

tupl=[('anil',28),('amit',3),("Akilesh",44),('ninit',4)]
print(Sort_tup(tupl))