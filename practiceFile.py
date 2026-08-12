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

a=int(input("enter first digit:"))
b=int(input("enter second digit:"))
operator=input("enter operator:")

if operator=='+':
    print(a+b)
elif operator=='-':
    print(a-b)
elif operator=='*':
    print(a*b)
elif operator=='/':
    print(a/b)
elif operator=='%':
    print(a%b)
elif operator=='**':
    print(a**b)  
else :
    print("invalid opeartor")
