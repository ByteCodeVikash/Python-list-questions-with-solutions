#Python program to print all negative numbers in a range

start=int(input("Enter a starting range:"))
end=int(input("Enter a end range: "))

for i in range(start,end+1):
    if i<0:
        print(i,end=',')