#anonymous functions->nameless functions
#write a function to calculate 2*x+5 where x=5
'''def f(x):
    print(2*x+5)
f(5)'''

'''def f():
    x=int(input("value"))
    print(2*x+5)
f()'''

#Lambda()
#syntax
#a=lambda arg:expr
'''a=lambda x:2*x+5
print(a(5))'''

#runtime
'''a=int(input("a value"))
b=lambda x:2*x+5
print(b(a))'''

#tasks
#multiplication
'''c=lambda x,y:x*y
print(c(2,4))'''

'''a=int(input("a value"))
b=int(input("b value"))
c=lambda a,b:a*b
print(c(a,b))'''

'''a="python"
#o/p:PYTHON
c=lambda a:a.upper()
print(c(a))'''

'''a=input("Enter the string:")
b=lambda a:a.upper()
print(b(a))'''

'''a="hello world"
#Hello World
b=lambda a:a.title()
print(b(a))'''

'''a=input("enter a value:")
b=lambda b:b.title()
print(b(a))'''


'''a=input("enter a value:")
b=lambda b:b.title()
print(b(a))'''

#fname+lname=fullname
'''f_n=input("enter your first name:")
l_n=input("enter your last name:")
x=lambda f_n,l_n:((f_n+" "+l_n).title())
print(x(f_n,l_n))'''

'''a,b=[x for x in input("enter the names:").split(",")]
c=lambda a,b:(a+" "+b).title()
print(c(a,b))'''

'''a,b=input("enter the names:").split(",")
c=lambda a,b:(a+" "+b).title()
print(c(a,b))'''

#Filter()
#a=[10,20,30,50,34,21,94,60,100]
'''if a%2==0:
    print(a)''' #error

'''for i in a:
    if i%2==0:
        print(i)'''

'''b=list(filter(lambda x:x%2==0,a))
print(b)'''

#[],(),{},set()
'''a=[]
print(type(a))

b=()
print(type(b))

c={}
print(type(c))

d=set()
print(type(d))'''

'''a=[[],(),set(),{}," ",4,6.7,"python",4+9j,True,False]
b=list(filter(None,a))
print(b)'''


#map()->each object from a collection and forms a new collection
'''a=[2,5,7,9,12,15,20,90,60]
b=[1,4,6,13,19,35,40,60]
c=list(map(max, a,b))
print(c)

d=list(map(min, a,b))
print(d)'''

#Railway Ticket Application
def ticket():
    Gender=str(input("Enter your gender:"))
    Age=int(input("Enter your Age:"))
    original=1000
    discount=
    if Gender=="Male" and Age>60:
        discount=30
        print('''You got the discount of 30%
              Ticket Price is 300''' )
    elif Gender=="Male" and Age<60:
        print("Your ticket price is 1000")
    elif Gender=="Female" and Age>60:
        print('''you got the discount of 50%
               Ticket Price is 500''')
    else:
        print("Your ticket price is 700")
ticket()




