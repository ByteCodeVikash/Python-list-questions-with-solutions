#Python program to print all odd numbers in a range

start=int(input("Enter a start range: "))
end=int(input("Enter a end range: "))

for i in range(start,end+1):
    if i%2!=0:
        print(i,end=',')