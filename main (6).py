def factorial(n):
  if n==1:
    return 1
  else:
    return n*factorial(n-1)
num=int(input("enter a number:"))
print("the factorial of a {0} is :".format(num),factorial(num))