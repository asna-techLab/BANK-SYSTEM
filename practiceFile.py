# ---practice Q1----

#person_name=input("enter the name of hero:")
#age=53
#height=1.83

#print (person_name)

#---sum of two numbers----

#a=int(input("enter 1st number:"))
#b=int(input("enter 2st number:"))

#print("sum:" ,a+b)

#---- practice Q2 ------
#a =int(input("enter price of 1st product"))
#b =int(input("enter price of 2st product"))
#c =int(input("enter price of 3st product"))

#Total= a+b+c
#print ("total bill:",Total)

#Avg = (a+b+c)/3
#print ("average:",Avg)

#person_name=input("enter the name of hero:") 
#print (person_name)
#print('o' in person_name)

#str1=4>9
#print(str1)

#------- MINI CALCULATOR --------

# a=int(input("enter first digit:"))
# b=int(input("enter second digit:"))
# operator=input("enter operator:")

# if operator=='+':
#     print(a+b)
# elif operator=='-':
#     print(a-b)
# elif operator=='*':
#     print(a*b)
# elif operator=='/':
#     print(a/b)
# elif operator=='%':
#     print(a%b)
# elif operator=='**':
#     print(a**b)  
# else :
#     print("invalid opeartor")

#-------LOOPS-------

# counter=1
# while counter<=6:
#     print("ASNA SAJID")
#     counter += 1
    
# i=1
# while i<=5:
#     print(i * "*")
#     i += 1

#for loop

# for i in range(2, 20, 2): #table of 2
#     print(i)
    
# for i in range(1,50):
#     if(i==21):
#         break
#     if(i%3 == 0):
#         print(i)
        
        
#-------practice Q4---------------

#print all odd no. from 1 to 20

# for i in range(1,20):
#     if (i%2 != 0):
#         print(i)
        

# #print the table of 57

# for i in range(57,570,57):
#     print(i)
    
# #print all multipls of 3 from 1-50 but skip 15

# for i in range (1,50):
#     if (i==15):
#         continue
#     if (i % 3==0):
#         print(i)
        
# #take two  numbers a and b and print first number between 1 and 1000 that is divisible by both

# a=int(input("enter 1st number:"))
# b=int(input("enter 2st number:"))

# for num in range (1,1001):
#     if num % a == 0 and num % b == 0:
#         print("First number:", num)
#         break
#     else:
#         print("no valid number")
#         break

#-----------exercise 5-------------

# list={101,105,101,108,105,104}
# print(list)

#------------function---------

# def sum(a, b):
#     print(a - b)

# sum(10, 20)

# def cal_gst(price):
#     new_price=price + price * 0.18
#     print(new_price)
    
# cal_gst(20)

#--------------OOPS IN PYTHON---------------

# class Student:
#     name="asna sajid"
#     age=20
    
    
# s1=Student() #OBJECT
# print(s1.name)
# print(s1.age)
    
    #--------PARAMETERIZED CONSTUCTOR---------
# class Student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
       
        
# s1=Student("asna", 20)
# print(s1.name,s1.marks)

# s2=Student("sajid",40)
# print(s2.name,s2.marks)        

#---METHODSS------

# CREATE a class that takes name and marks of three subjects as arguments in constuctor.
#then create a method to print average

# class Subjects:
#     def __init__(self,sub_name,marks):
#         self.name=sub_name
#         self.marks=marks
        
#     def avg(self):
#             sum=0
#             for val in self.marks:
#                 sum+=val
#             print("hi", self.name,"your avaerage marks are",sum/3)
        
# s1=Subjects("Asna", [99,87,78])
# print(s1.avg())

#Static methids and INHERITANCE

class car:
    @staticmethod
    def start():
        print("car start...")
        
    @staticmethod
    def stop():
        print("car stop...")  
        
class hondacity(car):     
    def __init__(self, car_name):
        self.car_name=car_name

car1=hondacity("civic")
car1.start()
car1.stop()

    