
a = int(input("Enter a number: "))

# using for loop
def factorial(n):
    result = 1
    for i in range(2,n+1):
        result *=i
    return result

output = factorial(a)
print("Factorial of", a , "is", output)

#using recursion

def factorial2(x):
    if x == 0 or x == 1:
        return 1
    else:
        return x * factorial2(x-1)

output2 = factorial2(a)
print("Factorial of", a , "is", output2)

