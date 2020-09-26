def check_prime_number(val):
    sqrt_val = int(pow(val, 0.5))
    # print(sqrt_val)
    flag = 0
    for i in range(2, sqrt_val + 2):
        # print(i, val % i)
        rem = val % i
        # print(rem)
        if val == 1:
            flag = 1
        elif val == 2:
            flag = 0
        elif val == 3:
            flag = 0
        elif rem == 0:
            # print("there is a factor")
            flag = 1
            break
    return flag


def print_prime_numbers_till_value(val):
    print("prime numbers till {}".format(val))
    for i in range(1, val + 1):
        x = check_prime_number(i)
        if x == 1:
            pass
            # print("{} is not a prime number".format(val))
        else:
            print(i, end=" ")
            # print("{} is a prime number".format(val))


val = int(input("Enter your value: "))
print(val, type(val))
is_prime = check_prime_number(val)
if is_prime == 1:
    print("{} is not a prime number".format(val))
else:
    print("{} is a prime number".format(val))
print_prime_numbers_till_value(val)

