#Python program to print all even numbers in a range

for even_number in range(4,15,2):
    print(even_number,end=' ')

#using user input

start=int(input("Enter here starting number:"))
end=int(input("Enter here end number:"))

for i in range(start,end+1):
    if i %2==0:
        print(i,end=' ')