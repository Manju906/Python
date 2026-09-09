#conditions
#if,elif,else
#if,if-else,if-elif-else,multiple-elif,multiple-if,nested-if
#if-condition by using comparision operators
#<,>,<=,>=,==,!=
#IF
'''a=3
b=6
if a<b:
    print("less")'''
'''a=4
b=5
if a>b:
    print("less")'''
'''a=5
b=5
if a<=b:
    print("equal")'''
'''a=4
b=6
if a>=b:
    print("greater")'''
'''a=4
b=6
if a==b:
    print("equal")'''
'''a=4
b=4
if a==b:
    print("equal")'''
'''a=4
b=4
if a!=b:
    print("equal")'''
'''a=5
b=4
if a!=b:
    print("not equal")'''
'''a=20
if a>20:
    print("large")'''
'''a=30
if a>20:
    print("large")'''
'''a="python"
b="java"
if a==b:
    print("equal")'''
'''a="python"
b="python"
if a==b:
    print("equal")'''
'''a=int(input())
if a>20:
    print("True")'''
#if condition by using logical operators
#and,or,not
'''a=6
b=4
if a>b and b>a:
    print("True")'''
'''a=5
b=8
if a<=b and b<=a:
    print("true")'''
'''a=3
b=9
if a!=b and a==b:
    print("true")'''
'''a=5
b=3
if a<=b and b>=a:
    print("true")'''
'''a=3
b=9
if a!=b and a==b:
    print("true")'''
'''a=10
b=15
if a<b or b>a:
    print("greater")'''
'''a=13
b=15
if a<=b or b>=a:
    print("less")'''
'''a=8
b=12
if a!=b or a==b:
    print("equal")'''
'''a=5
b=10
if not a<b:
    print("less")'''
'''a=5
b=10
if not a>b:
    print("less")'''
'''a=int(input())
if a>10:
    print("greater")'''

'''a=int(input("value"))
b=int(input("value"))
if a>b and b>a:
    print("true")'''
#identifier (is ,is not)
'''a=10
if type(a) is int:
    print("int")'''
'''a=1.0
if type(a) is not int:
    print("false")'''
'''a=int(input("data"))
if a is 10:
    print("ten")'''
'''a=input("data")
if type(a) is str:
    print("yes")'''
#membership operator(in ,not in)
'''a=int(input("val1"))
b=[3,4,5,6,7,8]
if a in b:
    print("yes")'''
#IF-ELSE
#if-else condition using comparision operators
'''a=3
b=6
if a<b:
    print("less")
else:
    print("true")'''
'''a=7
b=10
if a>b:
    print("less")
else:
    print("true")#if 'if' condition fails else part will be executed'''
'''a=4
b=6
if a==b:
    print("equal")
else:
    print("not equal")'''
'''a=6
b=6
if a==b:
    print("equal")
else:
    print("not equal")'''
'''a=4
b=6
if a!=b:
    print("equal")
else:
    print("not equal")'''
'''a=int(input("val1"))
b=int(input("val2"))
if a==b:
    print("equal")
else:
    print("not equal")'''
#if-else condition by using logical operators(and,or,not)
'''a=6
b=9
if a<b and b>a:
    print("true")
else:
    print("false")'''
'''a=4
b=7
if a<b or b<a:
    print("less")
else:
    print("greater")'''
'''a=6
b=3
if not b<a:
    print("true")
else:
    print("false")'''
'''a=7
b=10
if not b<a and a>b:
    print("true")
else:
    print("false")'''
#if-else using identify/identity operator
'''a=3
if type(a) is int:
    print("int")
else:
    print("not int")'''
'''a=32
if type(a) is not int:
    print("int")
else:
    print("not int")'''
#if else using membership operator
'''a="python"
b="py"
if b in a:
    print("true")
else:
    print("false")'''
'''a="python"
b="hi"
if b in a:
    print("true")
else:
    print("false")'''
'''a="python"
b="py"
if b not in a:
    print("true")
else:
    print("false")'''
'''a=[1,2,3,4]
b=4
if b in a:
    print("true")
else:
    print("false")'''










#IF-ELIF-ELSE
'''a=10
b=20
if a<b:
    print("less")
elif b>a:
    print("greater")
else:
    print("false")'''
'''a=8
b=15
if a>b:
    print("less")
elif b>a:
    print("greater")
else:
    print("false")'''
'''a=10
b=20
if a==b:
    print("less")
elif b<a:
    print("greater")
else:
    print("false")'''
'''a=40
b=50
if a==b:
    print("less")
elif a>b:
    print("greater")
elif a!=b:
    print("not equal")
else:
    print("false")'''
'''a=70
b=80
if a==b:
    print("less")
elif a>b:
    print("greater")
elif b<a:
    print("lesser")
elif a!=b:
    print("not equal")
else:
    print("false")'''
#MULTIPLE-IF(all the conditions will be satisfied)/
'''a=5
b=10
if a<b:
    print("less")
if a!=b:
    print("not equal")
if b>a:
    print("greater")'''#o/p:less,not equal,greater
'''a=4
b=9
if a>b:
    print("less")
if a!=b:
    print("not equal")
if b>a:
    print("greater")'''#o/p:not equal,greater
#NESTED-IF(when first if is satified then it will go to second if otherwise it will come out and prints null)
'''a=7
b=10
if a<b:
    print("less")
    if b>a:
        print("greater")'''
'''a=8
b=9
if a==b:
    print("less")
    if b>a:
        print("greater")'''
'''a=7
b=10
if a<b:
    print("less")
    if a==b:
        print("equal")
    else:
        print("not equal")'''
'''a=7
b=10
if a>b:
    print("less")
    if a==b:
        print("equal")
    else:
        print("not equal")
else:
    print("true")'''
'''a=5
b=10
if a<b:
    print("less")
    if a==b:
        print("equal")
    else:
        print("not equal")'''







    







    
