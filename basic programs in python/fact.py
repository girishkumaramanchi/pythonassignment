def fact(n):
    factorial = 1
    for i in range(1, n+1):
        factorial *= i
    return factorial


val = int(input("Enter your value: "))
fact_of_val = fact(val)
print(fact_of_val)
