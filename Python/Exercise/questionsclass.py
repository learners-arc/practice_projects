# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def display(self):
#         return self.name, self.age
# a=input("Enter your name: ")
# b=int(input("Enter your age: "))
# p1=Person(a,b)
# print(p1.display())
# # print(p1.name)
# # print(p1.age)
# class Student(Person):
#     def __init__(self,name,age, grade):
#         super().__init__(name,age)
#         self.grade = grade
#     def show(self):
#         return self.grade
# a=input("Enter your name: ")
# b=int(input("Enter your age: "))
# c=int(input("Enter your score: "))
#
# p2=Student(a,b,c)
# print(p2.display())
# print(p2.show())


#rectangle and calculate area and perimeter

# class Rectangle:
#     def __init__(self, width, height):
#         self.width=width
#         self.height=height
#     def area(self):
#         return self.width * self.height
#     def perimeter(self):
#         return 2*(self.width+self.height)
# a=int(input("enter widht: "))
# b=int(input("enter height: "))
# cal=Rectangle(a,b)
# print(cal.area())
# print(cal.perimeter())


# bank system
# class Bank:
#     def __init__(self, balance):
#         self.balance = balance
#     def withdraw(self, amount):
#         self.balance -= amount
#         return self.balance
#     def deposit(self, amount):
#         self.balance += amount
#         return self.balance
# a=int(input("Enter balance: "))
# det=Bank(a)
# b=int(input("Enter withdraw amnt: "))
# c=int(input("Enter deposit amnt: "))
# print(det.withdraw(b))
# print(det.deposit(c))

# class Calculator:
#     def __init__(self, num):
#         self.num = num
#     def add(self,b):                     # working
#         return self.num + b
#     def subtract(self):
#         return self.num - b
#     def multiply(self):
#         return self.num * b
#     def divide(self):
#         return self.num / b
# a=int(input("Enter a number: "))
# b=int(input("Enter a number 2nd: "))
# cal=Calculator(a)



# a=int(input())
# sum=0
# while a>0:
#     b=a%10                 # sum of digit
#     sum+=b
#     a//=10
# print(sum)

# a=int(input())
# print(factorial(a))
# a=int(input())
# m=1                                           #factorial
# for i in range(1,a+1):
#     m*=i
#     print(i,end=" ")
# print()
# print(m)

# def perfect():
#     n=int(input("Enter a number: "))
#     b=[]
#     s=0
#     for i in range(1,n):                               #perfect number
#         if n%i==0:
#             b.append(i)
#             s+=i
#     if s==n:
#         print(n,"is a perfect number.")
#
#     else:
#         print(n,"is not a perfect number.")
#     print(b)
# perfect()


# def palindrome():
#     n=input("Enter a number: ")
#     r=n[::-1]
#     if n==r:                                         #palindrome
#         print("It is a palindrome")
#     else:
#         print("It is not a palindrome")
# palindrome()

# def triangle():
#     n=int(input("Enter a number of rows: "))
#     for i in range(n):
#         for j in range(i+1):
#             print(n-j,end=" ")
#         print()
# triangle()

# while True:
import math
def is_prime():
    n = int(input("Enter a number: "))  # Take input from the user.

    if n <= 1:                         # Prime numbers are greater than 1.
        print(n, "is not a prime number.")
        return
    for i in range (2, int(math.sqrt(n))+1):
    # for i in range(2, int(n**0.5) + 1):  # Check divisors from 2 to √n.
        if n % i == 0:                  # If divisible, it's not prime.
            print(n, "is not a prime number.")
            return

    print(n, "is a prime number.")       # If no divisors found, it's prime.

# Call the function
is_prime()

# import os
# os.remove("/home/anshkumar/Documents/intro.txt")
# for encoding error , "a.txt",encoding="UTF-8")

# a=open("/home/anshkumar/Documents/intro.txt","w")
# # print(a.read())
# print(a.write("This is going to delete"))
