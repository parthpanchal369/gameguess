# fibonacii

# def fibonacci(n):
#
#     fib_siquence = [0,1]
#
#     if n <= 0:
#         return 0
#
#     for i in range(0,n):
#         next = fib_siquence[-1] + fib_siquence[-2]
#         fib_siquence.append(next)
#
#     return fib_siquence

# n = int(input())
#
# print(fibonacci(n))


# num = int(input())
#
# n1, n2 = 0,1
# count = 0
#
# if num < 0:
#     print("Enter positive number")
#
# elif num == 1:
#     print(n2)
#
# else:
#     while count < num:
#         nth = n1 + n2
#         n1 = n2
#         n2 = nth
#         count+= 1
#         print(n1)

#frequency of number

# def frequence_count(number):
#
#     frequence = {}
#
#     for num in number:
#         if num in frequence:
#             frequence[num] += 1
#
#         else:
#             frequence[num] = 1
#
#     for key, value in frequence.items():
#         print(f'{key} = {value}')
#
# number = input()
# (frequence_count(number))

