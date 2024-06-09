#Python | Finding strings with given substring in list

Lst=['This','is','a','good','boy']

print("this is original list",str(Lst))

sub='good'

res=[i for i in Lst if sub in i]

print("All string with given substring is",str(res))