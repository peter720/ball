import math
var = 5 # integer variable
bob = 2
bob
print(var + bob)
x = var + bob
print(x)
y = input("enter a number: ")
w = input("enter another number: ")
num1 = int(y)
num2 = int(w)
o = num1 + num2
print(o)

def sum3(a, b, c):
    z = a+b+c
    return z
    #return a+b

##def sum3(a, b):
 ##   return a+b

def rangeSum(n=10):
    sum = 0
    for i in range(n+1):
        #sum = i
        sum = sum + i
    #print(sum)
    return sum

m = rangeSum()
print(m)
print(m*5)
print(rangeSum(50))
print(sum3(var, bob, 6))
##print(sum3(var, bob))
##hw
def rangesphere(r=17.0):
    return float(4/3)*math.pi*(r**3)
def spherearea(r=17.0):
    return 4.0*math.pi*(r**2)
uh = (spherearea())
print(uh)
print(rangesphere())

def testScore(grade= input("Enter a score")):
    i = int(grade)
    if i >= 90 and i <= 100:
        g = "A"
    elif i >= 80:
        g = "B"
    elif i >= 70:
        g = "C"
    elif i >= 60:
        g = "D"
    elif i >= 0:
        g = "F"
    return g
print(testScore())

              

