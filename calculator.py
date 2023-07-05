# a code to calculate addition, substraction and multiplication
# addition function
#import pdb
def add (a, b):
  sum=a+b
  return sum
# multiplication function
def multiply (a, b):
    return a*b
# get the user input
a=int(input("Please enter the value of a: "))
b=int(input("Please enter the value of b: "))

sum=add(a,b)
product=multiply(a,b)
z=sum+20

print ("The sum is",sum)
print("sum plus 20 is", z)
print ("The product is", multiply)
