# Palindrome Using String
n=input("Enter the String To Check For Palindrome:")
if (n==n[::-1]):
    print("Palindrome")
else:
    print("Not Palindrome")

# Factorial of N Numbers
fact=1
n=int(input("Enter the Number For Factorial:"))
for i in range(1, n+1):
    fact=fact*i
print(fact)

# Largest Among 2 Numbers
a=int(input())
b=int(input())
if(a>b):
    print("A is Larger")
else:
    print("B is Larger")

# Amstrong Number
n=int(input())
s=sum(int(i)**len(str(n)) for i in str(n))
if (n==s):
    print("Valid Code")
else:
    print("Invalid Code")

# Prime Number From Range
print("Prime numbers from 1 to 50:")
for n in range(2,51):
    prime=True
    if n>1:
        for i in range(2,int(n**0.5)+1):
            if (n%i)==0:
                prime=False
                break
    else:
        prime=False
    if prime:
        print(n)

# Fahrenhit to Celcius
f=int(input("Enter the Fahrenhit Number:"))
c=f-32
print(c*(5/9))

# Celcius to Fahrenhit
c=int(input("Enter the Celcius Number:"))
f=c+32
print(f*(9/5))

# Swap 2 Numbers without Temporary Variable
a=int(input("Enter the First Number:"))
b=int(input("Enter the Second Number:"))
a,b=b,a
print(a,b)

# Fibonacci Series of N Terms
n=int(input("Enter the Number of Fibonacci Series:"))
a=0
b=1
for i in range(0,n):
  print(a)
  c=a+b
  a=b
  b=c

# Mean of 3 Numbers
from statistics import mean
a,b,c=map(int,input("Enter 3 Numbers:").split())
d=mean([a,b,c])
print(d)

#Checking the Vowels in an String
a=input("Enter the String To Check For Vowels:")
vowels="aeiouAEIOU"
count=0
print("Vowels are:")
for i in a:
  if i in vowels:
    print(i,end=" ")
    count+=1
print("\n")
print("The Count of Vowels:",count)

n=int(input("Enter the Number for * Patterns:"))
for i in range(0,n):
  for j in range(i):
    print("*",end="")
  print("\n")

n=int(input("Enter the Number for * Patterns:"))
for i in range(0,n):
  for j in range(n-i):
    print("*",end="")
  print("\n")

#Find Largest and Smallest of an Given Number
a=[3,17,2,9,7,65,92]
largest=a[0]
smallest=a[0]
for i in a:
  if i > largest:
    largest=i
  elif i < smallest:
    smallest=i
print(largest)
print(smallest)

#Calculate all Operator
a=int(input("Enter the First Number:"))
b=int(input("Enter the Second Number:"))
op=input("Enter the Operator:")
match op:
  case '+':
    print(a+b)
  case '-':
    print(a-b)
  case '*':
    print(a*b)
  case '/':
    print(a/b)
  case '%':
    print(a%b)
  case _:
    print("Invalid Choice")

#GCD & LCM of 2 Numbers
a=int(input("Enter the First Number:"))
b=int(input("Enter the Second Number:"))
x=a
y=b
while b!=0:
  a,b=b,a%b
gcd=a
lcm=(x*y)//gcd
print(gcd)
print(lcm)

n=int(input("Enter A Number:"))
if (n>0):
  print("Positive")
elif(n<0):
  print("Negative")
else:
  print("Zero")

n=int(input("Enter the Number to Check Leap Year:"))
if (n%4==0) and (n%100!=0) or (n%400==0):
  print("Leap Year")
else:
  print("Not Leap Year")

#Anagram Program using Sorted Program
n=input("Enter the First String:")
m=input("Enter the Second String:")

if sorted(n) == sorted(m):
  print("Anagram")
else:
  print("Not Anagram")

n=int(input("Enter the Number of Pattern:"))
for i in range(1,n+1):
  for j in range(1,i+1):
    print(j,end=" ")
  print("\n")

n=int(input("Enter the Number For * Pattern:"))
for i in range(n):
  print(" "*i+"*"*(n-i))

n=int(input())
for i in range(1,n+1):
  print(" "*(n-i)+"* "*i)
for i in range(n-1,0,-1):
  print(" "*(n-i)+"* "*i)

a=int(input("Enter the First Number:"))
b=int(input("Enter the Second Number:"))
c=int(input("Enter the Third Number:"))

print(max(a,b,c))

#Anagram Using Counter
from collections import Counter
a=input()
b=input()
if Counter(a)==Counter(b):
  print("Anagram")
else:
  print("Not Anagram")

n = int(input("Enter a number:"))
if (n > 0) and ((n & (n - 1)) == 0):
    print(f"{n} is a power of 2")
else:
    print(f"{n} is not a power of 2")

s=input()
longest=""
for i in range(len(s)):
  current=""
  for j in range(i,len(s)):
    if s[j] not in current:
      current+=s[j]
    else:
      break
  if len(current)>len(longest):
    longest=current
print(len(longest))

#Reverse Only Vowels in a String

s = list(input())

vowels = "aeiouAEIOU"

left = 0
right = len(s) - 1

while left < right:

    while left < right and s[left] not in vowels:
        left += 1

    while left < right and s[right] not in vowels:
        right -= 1

    s[left], s[right] = s[right], s[left]

    left += 1
    right -= 1

print("".join(s))

#Longest Substring Palindrome

s=input()
if s==s[::-1]:
  print("Palindrome")
for i in range(len(s)):
  for j in range(i,len(s)):
    e=s[i:j]
    if e==e[::-1]:
      if len(e)>len(s):
        s=e
print(s)

from collections import Counter
sa=input().split()
sb=input().split()
e=list(sa)
f=list(sb)
l1=set()
l2=set()
if len(e)==len(f):
      for i in sa:
        for j in sb:
          if i == j:
            l1.add(i)
          else:
            l2.add(i)

h=len(l2)
if (h==1):
  print("Yes")
else:
  print("NO")

#Reverse Number are Prime
n=int(input())
x=list(map(int,input().split()))
for i in range(1,n+1):
  d=x[i]
  if(x[i]==0):
    d=x[i-1]+1
    print(d)
    break

def prime(n):
  for i in range (2,int(n**0.5)+1):
    if n%i==0:
      return False
  return True
def rev_num(reversed):
  return int(str(reversed)[::-1])
n=int(input("Enter the Number to Find Reverse Number Prime:"))
re=rev_num(n)
if prime(n) and prime(re):
  print(n,"-",re)
  print("Both are Prime")

else:
  print(n,"-",re)
  print("Not Prime")
#Adam Number
n=int(input())
l=[]

for i in range(1,n+1):
  if i%2==1:
    print(i)
  if i%2==0:
    print("-",i)

def sqr(n):
  return n*n
def rev_sqr(n):
  return (int(str(n)[::-1]))
n=int(input())
re=rev_sqr(n)
d=sqr(n)
t=sqr(re)
e=rev_sqr(d)
if e == t:
  print("Adam Number")
else:
  print("Not Adam Number")

from statistics import mean
class student:
  def __init__(self,name,mark):
    self.name=name
    self.mark=mark
name=input("Enter the Name:")
mark=list(map(int,input().split()))
s=student(name,mark)
print("Total:",sum(s.mark))
print("Average:",float(mean(s.mark)))
print("Highest:",max(s.mark))
print("Status: ",end="")
print("Fail" if min(s.mark)<35 else "Pass")

from statistics import mean
class Employee:
  def __init__(self,name,score):
    self.name=name
    self.score=score
  def display(self):
    print(max(self.score))
    print(float(mean(self.score)))
    count=0
    for i in self.score:
      if i>80:
        count+=1
    print(count)
name=input("Enter the Name:")
score=list(map(int,input().split()))
e=Employee(name,score)
e.display()

class Parking:
  def __init__(self,values):
    self.values=values
  def show (self):
    dup=set()
    s=set()
    count=0
    for i in self.values:
      if i in s:
        dup.add(i)
      else:
        s.add(i)
        count+=1
    print("Duplicate Vehicles:",dup)
    print("Unique Vehicles:",count)



values=list(map(int,input().split()))
p=Parking(values)
p.show()

from collections import Counter
a=input()
b=input()
d=set(a)
c=set(b)
if Counter(d)==Counter(c):
  print("Equivalent Logs")
else:
  print("Not Equivalent Logs")

from statistics import mean
class Cricketor:
  def __init__(self,name,score):
    self.name=name
    self.score=score
  def show(self):
    print("Highest Score:",max(self.score))
    print("Lowest Score:",min(self.score))
    print("Average Score:",mean(self.score))
    count=0
    for i in range(len(self.score)):
      if self.score[i]>=50:
        count+=1
    print("Half Century:",count)
name=input("Enter the Name:")
score=list(map(int,input().split()))
c=Cricketor(name,score)
c.show()

class Shopping:
  def __init__(self,prices):
    self.prices=prices
  def show(self):
    print("Total Bill:",sum(self.prices))
    print("Costliest Item:",max(self.prices))
    d=0
    for i in self.prices:
      if i >5000:
        d=i*0.15
      else:
        print("No Discounts")
    print("Discounted Bill:",d)
prices=list(map(int,input().split()))
s=Shopping(prices)
s.show()
