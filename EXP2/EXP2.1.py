num = int(input("Enter the number:"))

if num % 2 == 0:
    print("even")
else:
    print("odd")

for i in range(1,11):
    print(i)

num1= int(input ("Enter the value of first number:"))
num2= int(input ("Enter the value of second number:"))
num3= int(input ("Enter the value of third number:"))

if num1 > num3 :
     print("num1 is greater")
elif num2 > num3:
     print("num2 is greater")
elif  num3 > num1:
     print("num3 is greater")