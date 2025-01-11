# 1
# class Student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
# s1_name=input('enter 1 name: ')
# s1_age=int(input('enter 1 age: '))    #1st constructor class obj
# stud_1=Student(s1_name,s1_age)
# print(stud_1.name, stud_1.age)
# s2_name=input('enter 2 name: ')
# s2_age=int(input('enter 2 age: '))
# stud_2=Student(s2_name,s2_age)
# print(stud_2.name, stud_2.age)


# 2
class comp:
    def setAge(self, age):
        self.age=age
    def getAge(self):                         #set get method
        return self.age
Hon=comp()
carage=int(input('enter comp age: '))
Hon.setAge(carage)
print(Hon.getAge())


# 3
# class Person:
#     def setName(self, name):
#         self.name=name
    
#     def getName(self):
#         return self.name                    #set get clear ness
# p1=Person()
# p1_name=input('enter p1: ')
# p1.setName(p1_name)
# print(p1.getName())
# p2=Person()
# p2_name=input('enter p2: ')
# p2.setName(p2_name)
# print(p2.getName())


# 4
# class Greeting:
#     def sayHello(self, name=None, wish=None):
#         if name and wish:
#             return (f"hello{name}{wish}")
#         elif name:
#             return(f"hello{name}")          #method overloading
#         else:
#             return (f"hello")
# a=input("name: " )
# b=input('greet: ')
# greet=Greeting()
# print(greet.sayHello())


# class Bank:
#     def __init__(self,balance):
#         self.balance=balance
#         print(self.balance)
#     def dep(self,deposit):
#         self.balance+=deposit
#         print(self.balance)
#     def wit(self,withdraw):
#         self.balance-=withdraw
#         print(self.balance)
# inp=Bank(10000)
# while True:
#     inp.dep(int(input('how much depo: ')))
#     inp.wit(int(input('how much with: ')))
#     break
# print('Thank for using our system')


# practice 1
# class Student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
# s1=input('name')
# s2=int(input('age'))
# stud=Student(s1 ,s2)
# print(stud.name, stud.age)

# practice 3
# class Student:
#     def setName(self,name,clas):
#         self.name=name
#         self.clas=clas                   #doubt
#     def getName(self):
#         return self.name, self.clas
#         # return self.clas
# aps=Student()
# s1_name=input('enter name s1: ')
# s1_clas=int(input('enter class s1: '))
# aps.setName(s1_name, s1_clas)
# print(aps.getName())


# practice 4
# class Greeting:
#     def sayHello(self, name=None, greet=None):
#         if name and greet:
#             print(f'Hello {name} {greet}')
#         elif name:
#             print(f'Hello {name}')
#         else:
#             print(f'Hello')
# greet=Greeting()
# a=input('name: ')
# b=input('greet: ')
# greet.sayHello()