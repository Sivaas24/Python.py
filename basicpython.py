#Exam mark average 
'''
a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())
f=a+b+c+d+e
g=f/5
print(g)
if g>35:
    print("Super avrage")
else:
    print("Not good")'''


'''for i in range(2):
    print(i)'''

#Tables
'''
i=1
j=10
for i in range(i,j+1):
    print(i," x 2 =  ",i*2)
'''

#print the between numbers
'''a=int(input())
b=int(input())
for i in range(a+1,b):
    print(i)'''

#Print even numbers count
'''a=0
for i in range(1,10+1):
    if i%2==0:
        a=a+1
print(a)
'''

#count odd and even number btwn 2 numbers
'''odd=0
even=0
for i in range(1,10+1):
    if i%2==0:
        even+=1
    else:
        odd+=1
print("odd  count = ",odd)
print("even count = ",even)'''


#Divisible by 3 and 5 range 1-100
'''count=0
for i in range(1,100+1):
    if i%3==0 and i%5==0:
        count+=1
print(count)'''


#addition of 5 natrual number
'''a=0
for i in range(1,6):
    a=a+i
print(a)'''

'''sum=0
for i in range(10):
    i=int(input())
    sum=sum+i
print(sum/10)'''


#Nested for loop

'''for i in range(1,6):
    for j in range(1,6):
        print(j)'''

'''for i in range(1,5):
    print("week : ",i)
    for j in range(1,8):
        print("day :",j)'''

# Pattern priniting

'''for i in range(1,5):
    for j in range(1,i+1):
        print("*",end=" ") 
    print("")
for x in range(5,0,-1):
    for y in range(1,x+1):
        print("*",end=" ")
    print()'''

#Pattern printing

'''n=int(input())
for i in range(n):
    for j in range(i,n-1):
        print(" ",end=" ")
    for k in range(i+1):
        print("*",end=" ")
    print()'''

'''# While loop
a = []
i = 4

while i > 1:
    i = i - 1
    a.append(i)

print(a)

product = 1
for i in a:
    product *= i

print(product)'''


#que 1
'''
num=int(input())
if(num<0):
    print("Negative number")
elif(num==0):
    print("Zero")
else:
    print("positive number")'''

# ques 2

num=int()




































