#Python program to print all positive numbers in a range

start=int(input("Enter a starting number in range:"))
end=int(input("Enter a end number in range:"))

for i in range(start,end+1):
    if i >0:
        print(i,end=',')