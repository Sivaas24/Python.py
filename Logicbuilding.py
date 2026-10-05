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
'''
num=int(input())

if num%2==0:
    print("Even")
else:
    print("Odd")'''

# ques 3
'''
num=int(input())

if num%5==0:
    print("Done")
else:
    print("Nope")

# ques 4

num=int(input())

if num%3==0 and num%5==0:
    print("done")

else:
    print("Not")'''


# ques 5
'''
Year=int(input("Year : "))

if Year%400==0:
    print("Leap year")
elif Year%4==0:
    print("Leap year")
elif Year%100==0:
    print("Not a leap year")
else:
    print("Not a leap year")
'''

# ques 6
'''
a=int(input())
b=int(input())

if a<b:
    print("B is bigger")

else:
    print("A is bigger")

'''

# ques 7
'''
a=int(input())
b=int(input())
c=int(input())
if a<b:
    print("B is bigger")
elif a>b:
    print("A is bigger")
else:
    print("c is bigger")

'''

# ques 8

'''
temp = int(input("Enter temperature: "))

if temp < 20:
    print("Cold")
elif temp <= 30:
    print("Warm")
else:
    print("Hot")
'''


# ques 9
'''

char=str(input())

if char in "AEIOUaeiou":
    print("Vowels")
else:
    print("Constant")

'''

# ques 10
'''
char = str(input())

if char.isupper():
    print("Upper case")

elif char.islower():
    print("lower case")

elif char.isdigit():
    print("Digit")

else:
    print("Special charcter")'''


# part - B

# 1. Check Valid Triangle
'''
A=int(input(""))
B=int(input(""))
C=int(input(""))

if A+B>C and A+C>B and B+C>A:
    print("Valid Triangle")

else:
    print("Not Valid")
'''

# 2.If the sides form a valid triangle, determine whether it is equilateral, isosceles, or
#scalene.

'''
A=int(input(""))
B=int(input(""))
C=int(input(""))

if A+B>C and A+C>B and B+C>A:
    if A==B and B==C and A==C :
        print("Equal triangle ")
    elif A==B or B==C or A==C:
        print("Isolecs triangle")
    else:
        print("Scalene triangle")
else:
    print("Not valid triangle")

'''

# 3. Take marks (0–100) and print the corresponding grade (A/B/C/D/F).
'''
Marks=int(input("Enter mark :"))

if Marks>=90:
    print("A")
elif Marks>=80:
    print("B")
elif Marks>=70:
    print("C")
elif Marks>=60:
    print("D")
else:
    print("Fail")

'''

# 4. Check if one of two given numbers is a multiple of the other.
'''

a=int(input())
b=int(input())

if a%b==0 or b%a==0:
    print("Num is divisble by each other")
else:
    print("No valid")

'''



# 5. Take the hour of the day (0–23) and print “Good Morning”, “Good Afternoon”, “Good
 # Evening”, or “Good Night”.

'''
hour=int(input())

if hour >= 5 and hour<12:
    print("Good morning ")
elif hour >=12 and hour <16:
    print("Good after noon")
elif hour >=17 and hour <20:
    print("Good evening ")
else:
    print("Good night")
'''
    


# 6. Check voting eligibility for a given age (18+).
'''
Age=int(input())

if Age>+18:
    print("Age eligible")
else:
    print("Not eligble")

'''


# 7 Take two numbers and determine whether both are even, both are odd, or one is
# even and one is odd.

'''
a=int(input())
b=int(input())

if a%2==0 and b%2==0:
    print("Both are even ")
elif a%2!=0 and b%2!=0:
    print("Both are odd")
else:
    print("One is Odd and one is Even ")

'''


# 8.Take an alphabet character and check if it lies between ‘a’ and ‘m’ or ‘n’ and ‘z’.

'''
ch=str(input("Enter :")).lower()

if ch in 'abcdefghijklmABCDEFGHIJKLM':
    print("Char between a-m")
elif ch in 'nopqrstuvwxyzNOPQRSTUVWXYZ':
    print("Char between n-z ")
else :
    print("Mixed and not valid chars")

'''

# 9. Day Number → Day Name
'''
day = int(input("Enter day number (1-7): "))

if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
elif day == 4:
    print("Thursday")
elif day == 5:
    print("Friday")
elif day == 6:
    print("Saturday")
elif day == 7:
    print("Sunday")
else:
    print("Invalid day")

'''

# 10. Take a month number (1–12) and print the number of days in that month (ignore leap
# years).

'''

month =int(input("Enter a month 1-12 : "))


if month==4 or month==6 or month==9 or month==11:
    print("30 dayss !")
elif month==2 :
    print("Leap year ")
elif month >= 1 and month <= 12:
    print("31 days")
else :
    print("31 dayss !")


'''


# 1.Get 3 number find equal and check the digit are same are different

'''
num=int(input("Enter : "))

first=num//100
last=num%10
middle=(num//10)%10

if first!=middle and middle!=last and last!=first:
    print("No number repeated")

else:
    print("some mum is repeated")


'''


# 2.Get 3 number and if check mid num is high low or neither

'''
num=int(input("Enter : "))

b=(num//10)%10
a=num//100
c=num%10

if b<a and b<c:
    print("b is smallest")

elif b>a and b>c:
    print("b is greatest")

else:
    print("Middle digit is neither")

'''

# 3.Take a 4-digit number and check if the first and last digits are equal.

'''
num= int(input("Enter : "))

first=num//1000
last=num%10


if first == last :
    print('Equal')
else:
    print("Not equal")
'''

# 4.Check whether a given integer is single-digit, double-digit, or multi-digit.

'''
num= int(input("Num :"))
if num<=9 and num>=0:
    print("Single digit")
elif num<=99 and num>=10:
    print("Double digit")
else:
    print("multi number")
'''

# 5.check if number is multiple of 7 and ends with 7

'''
num=int(input("Num :"))

last_digit=num%10

if num%7==0 and last_digit==7:
    print("Multiple of 7 ")

else:
    print("No")

'''


# 6. Quadrant x,y sum

''''

x=int(input("X= "))
y=int(input("Y= "))

if x>0 and y>0:
    print("Q-1")
elif x<0 and y>0:
    print("Q-2")
elif x<0 and y<0:
    print("Q-3")
elif x>0 and y<0:
    print("Q-4")
elif x==0and y==0:
    print("origin")
else:
    print("point lies in a axis")

'''


# 7. currency divided into equally

'''
currency=int(input("Enter :"))

if currency%100==0:
    print("ok")

else:
    print("not ok")

'''


# 8.num is lies btn 100-999
'''
num=int(input("Num :"))

if num<=100 or num<=999:
    print("Yes")

else:
    print("No")
'''

# 9.take 2 angles compute third angle
'''
a=int(input())
b=int(input())

c=180-(a+b)

print("Triangel c :", c)

'''

# 10.Perfect Square — Without sqrt()
'''

num=int(input("Enter :"))
for i in range(1,num+1):
    if i*i==num:
        print("Square root")
        break
else:
    print("Not Sqrt")
    
'''
# ------------------------------------------------------------------------------------------

# 1.check wheater its a num digit or chr
'''
ch = input("Enter a character: ")

if ('A' <= ch <= 'Z') or ('a' <= ch <= 'z'):
    print("Letter")
elif '0' <= ch <= '9':
    print("Digit")
else:
    print("Neither")
'''


# 2.Take a number and print: Fizz → divisible by 3 Buzz → divisible by 5 FizzBuzz → divisible by both

Num=int(input())

if Num%3==0 and Num%5==0:
    print("Fizz buzz")
elif Num%3==0:
    print("Fizz")
elif Num%5==0:
    print("Buzz")
else:
    print("Invalid")


# 3.Find the Median of Three Numbers








    











































