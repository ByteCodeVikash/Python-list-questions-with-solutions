#Python program to print all odd numbers in a range

Start=int(input("Enter a first number: "))
End=int(input("Enter a End number: "))

for i in range(Start,End+1):

    if i%2!=0:
      print(i,end=',')