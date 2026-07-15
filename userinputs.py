'''a=2
b=4
print(a+b)'''
'''a=3
b=8
c=a+b
print(c)'''
#runtimeinput
'''a=int(input())
b=int(input())
print(a+b)'''
'''a=float(input("enter the a value"))
b=float(input("enter the b value"))
print(a+b)'''
'''a=str(input("data1"))
b=str(input("data2"))
print(a+b)'''
'''fname=input("first name")
lname=input("last name")
print((fname+" "+lname).title())'''
'''a=complex(input("enter the a value"))
b=complex(input("enter the b value"))
print(a+b)'''
'''a=bool(input("enter the a value"))
b=bool(input("enter the b value"))
c=bool(input("enter the c value"))
print(a+b+c)'''
'''a=input()
print(a)'''
'''a=int(input("a value"))
b=int(input("b value"))
option=int(input("chose the option 1.add 2.sub 3.mul"))
print(a+b)
print(a-b)
print(a*b)'''
'''a=int(input("a value"))
b=int(input("b value"))
option=int(input(chose the option
                 1.add
                 2.sub
                 3.mul))'''
'''print(a+b)
print(a-b)
print(a*b)'''
'''a=int(input("a value"))
b=int(input("b value"))
option=input("chose the option add sub mul")
print(a+b)
print(a-b)
print(a*b)'''

#swapping of two variables
#first method simple
'''a=int(input("enter a value "))
b=int(input("enter b value "))
print(b,a)'''
#second method using temporary variable
'''a=int(input("enter a value "))
b=int(input("enter b value "))
temp=a
a=b
b=temp
print(a,b)'''
#third method using operators
'''a=int(input("enter a value "))
b=int(input("enter b value "))
a=a+b
b=a-b
a=a-b
print("a value is",a)
print("b value is",b)'''
#fourth method using number formatting
'''a=int(input("enter a value "))
b=int(input("enter b value "))
a=a+b
b=a-b
a=a-b
print("after swapping a=%d,b=%d" %(a,b))'''
#task2
''''a=(["codegnan","python","course"])
print(word.upper in a())'''
'''b=str(a)
print(b.upper())'''
#task3
'''a=[10,20,30,40,50,"code"]
#o/p:[10,20,30,40,50,"c","o","d","e"]
a.extend("code")
print(a)'''
#task4
'''a=[5,7,9,10,11,13]
#o/p:[5,7,9,10,11,12,13]
a.insert(5,12)
print(a)'''
#task5
'''a=[9,7,4,0,1,5,10,8,6,3]
#o/p:[0,1,3,4,5,6,7,8,9,10]
a.sort()
print(a)'''
#task6
'''a=("apple","banana","mango")
#o/p:apple,banana,mango,grapes
b=list(a)
b.append("grapes")
print(b)
c=tuple(b)
print(type(c))'''
#task7
id=int(input("Enter ID: "))
name=input("Enter name: ")
mobile=int(input("Enter mobile number: "))
mailid=input("Enter mailid: ")
collegename=input("Enter College Name: ")
Branch=input("Enter branch name: ")
print("................student profile....................")
print("id no is",id)
print("name is",name)
print("mobile is",mobile)
print("college is",collegename)
print("branch is",Branch)
