Day 1 

a=1168
print(a)

b='Fahim'

print(b)
# check int type data
golu= 1168
print(type(golu))

#check float type data

x=3.90
print(type(x))

#check complex type data

y= 4j

print(type(y))

#string type 

z='Fahim'
print('My name is :'+' '+z)

#boolean type

Zbool= True
print(type(Zbool))

T=10
t=5
print(t==T)
print(t>T)
print(t<T)

#string formating
num1=20
num2=80

print(f'Addition result:{num1+num2}')
# or
print(f'Addition result:',num1+num2)

name1= 'Tuhin'
roll='29'
print(f'My name is {name1} & My roll is:{roll}')

#Binary type data
#byte
golulist=[1,2,3,4,5,100]
bb= bytes(golulist)
print(type(bb))

#bytearray
golulist1= [1,2,3,4,5,6,7,100]
b1=bytearray(golulist1)
print(type(b1))

b1[1]=50
print(b1[1])
# to see whole array
print(b1)
#or
print(list(b1))

#list type data

golulist=['ami','tumi','amra']
print(golulist)
golulist[0]='uni'
print(golulist)
print(type(golulist))

#tuple type same as list type but it's not mutable and use first bracket()

#range type
r=range(7)
for i in r:
    print(i)
    
#operator
#arithmatic operator
x1=22
y1=10

print(x1+y1)

print(f'Substraction result:{x1-y1}')

print(f'modulas result:{x1%y1}')
x2= 5 
y2=3
print(f'Exponential result:{x2**y2}')
#In floor division it doesn't show any floating number
print(f'Floor division result:{x1//y1}')






