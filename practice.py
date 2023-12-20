# Python program to add two numbers

# num1 = int(input("Entyer your number: "))
# num2 = int(input("Enter your second number: "))
#
# num3 = num1 + num2
# print(f'Addition oftwo number is  {num3}')

# Max of two numbers


# num1 = int(input("Enter your firs  number: "))
# num2 = int(input("Enter your second number"))
#
# # result = max(num1, num2)
# # print(result)
#
# if num1 > num2:
#     print(num1)
#
# else:
#     print(num2)

# Python program to factorial of number

# def factorail(n):
#
#     if n == 0 or n == 1:
#         return 1
#
#     result = n * factorail(n-1)
#     return result
#
# num1 = int(input())
#
# print(factorail(num1))


# def factorail(n):
#
#     if n < 0:
#         return 0
#
#     elif n == 0 or n ==1:
#         return  1
#
#     else:
#         fact = 1
#         while(n > 1):
#             fact *= n
#             n -= 1
#         return fact
#
# n = int(input())
# print(factorail(n))


# intrest of rate


def simple_interest(p, t, r):

    print("principle  amount is: ",p)
    print("Time period is ", t)
    print("rate of interest is ", r)

    si = p * t * r / 100

    print(f'simple interest is {si}')


simple_interest(25000, 1, 3)


def armstrong(number):



