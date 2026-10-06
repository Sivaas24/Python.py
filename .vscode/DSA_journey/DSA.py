'''# 1.Odd or even


num=int(input('Number: '))
if num%2==0:
    print("Even") 
else:
    print("Odd")'''


# 2. Max among 3
'''
a=int(input('Number: '))
b=int(input('Number: '))
c=int(input('Number: '))

if a>=b and a>=c:
    print("a is bigger")

elif b>=c and b>=a:
    print("B is bigger")

else:
    print("C is bigger")
'''

# 3. Grade Calculator
'''
mark= int(input("Mark"))

if mark>=90:
    print("A")

elif mark>=80:
    print("B")

elif mark>=70:
    print("C")

elif mark>=60:
    print("d")

else :
    print("Fail")'''

# 4. Leap Year Checker
'''
Year =int(input("Year :"))

if (Year%4==0 and Year%100!=0)or Year %400==0:
    print('Leap Year')
else :
    print("Non leap year")'''



# 5. Simple Login
'''
US="Sivaa"
PW="123"

for i in range(3):
    a=str(input(""))
    b=str(input(""))
    if a==US and b==PW:
        print("Okayy")
    else:
        print('incorrect password ')
else:
    print("Not verfied")

'''

# 1. Print Numbers

'''
num = int(input())

for i in range(1,num+1):
    print(i)

'''

# 2. Print sum of n Numbers
'''
num =int(input("Number :"))
sum=0
for i in range(1,num+1):
    sum=sum+i

print(sum)
'''
# 3.Print the multiplication table of a given number up to 10.
'''
num=int(input("Enter :"))
tables=int(input("Enter :"))

for i in range(1,num+1):
    print(i,"*",tables,'=',i*tables)

'''
# 4.Calculate the factorial of a number N.
'''
num=int(input("Enter :"))
sum=1
for i in range(1,num+1):
    sum=sum*i
print(sum)'''

# 5.Input a number and print it in reverse order.

'''
num=int(input("Enter :"))

reverse=0

while num>0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10
print(reverse) 


'''

# 6.Count the total number of digits in a given number
'''
num=int(input("Enter :"))

count = 0

while num > 0:
    num = num // 10
    count = count + 1
print(count)
'''

# 7.Print a right triangle pattern with N rows using asterisks (*).
'''
num=5

for i in range(1,num+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()
'''

# 8.Print a pyramid pattern of N rows centered with asterisks.

n = 5

for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")

    for j in range(2 * i - 1):
        print("*", end="")

    print()



































