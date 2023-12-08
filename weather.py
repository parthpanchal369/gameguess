# list1 = [2,4,3,6,7,4,5,9,90,45,34,90]
# sorted_list = sorted(set(list1))
# second_highest = sorted_list[-2]
# print(second_highest)


# list2 = [2,3,4,74,34,56,56,74]
# sorting = sorted(set(list2))
# print(sorting[-2])

# my_list = "parth"
# for i in my_list:
#     # print(i)
#     pass

# list2 = [0,1,2,3,("a,b"),("c","d")]
#
# for x in list2:
#     print(x)

# dict1 = {"k1":10,"k2":20,"k3":30}
# for key, values in dict1.items():
#     print(key,"=",values)

# h1 = "Helloworld"
# h2 = {}
#
# for i in h1:
#     if i in h2:
#         h2[i] +=1
#
#     else:
#          h2[i] = 1
#
# for key,values in h2.items():
#     print(f"{key} = {values}")


# def is_palindrome(string):
#
#     new_string = str(string)
#
#     for i in new_string:
#         return new_string == new_string[::-1]
#
# string = input("Enter your sting: ")
# if is_palindrome(string):
#     print(f"your {string} is a palindrome")
#
# else:
#     print(f" Your {string} is not a palindrome")


# def is_prime(num):
#
#     for i in range(2,num):
#         if num % i == 0:
#             return False
#
#         else:
#             return True
#
# # num = int(input())
#
# for i in range(50,200):
#     if is_prime(i):
#         print(i)

# number = int(input("Enter your number: "))
# if is_prime(number):
#     print(f" {number} is a prime number")
#
# else:
#     print(f"{number} is not a prime number")


# h1 = "hello"
#
# for i in enumerate(h1):
#     print(i)


# h1 = [1,2,3,4],8
# h2 = ["apple","ball","dog","ky"]
#
# for i in zip(h1,h2):
#     print(i)

# mystring= "Hello"
# mylist = []
#
# for i in mystring:
#     mylist.append(i)
# print(mylist)

#
# string = "parth"
# list1 = []
#
# for i in string:
#     list1.append(i)
# print(list1)


# string = 'parth'
# list2 = [i for i in string]
# print(list2)

# list3 = [x for x in "manmad"]
# print(list3)


# def fizbuzz(number):
#
#     for num in range(1,number):
#         if num % 3 == 0 and num % 5 == 0:
#             print("Fizzbuzz")
#
#         elif num % 3 ==0:
#             print("Fizz")
#
#         elif num % 5 == 0:
#             print('Buzz')
#
#         else:
#             print(num)
#
# fizbuzz(100)

# print(fizbuzz(10))


# def even_check(number):
#
#     for num in number:
#         if num % 2 ==0:
#             return True
#
#         else:
#             pass
#     return False
#
# result =even_check([1,3,5])
# print(result)

# def even_check(number):
#     list_store = []
#     for num in number:
#         if num % 2 ==0:
#             list_store.append(num)
#
#         else:
#             pass
#
#     return list_store
#
# result = even_check([1,5,7,])
# print(result)

#
# stoke = [("apple",1000), ("mksft", 500) , ("google", 700)]
#
# for item,price in stoke:
    # print(price)



# def stoke_prices(company):
#
#     for item in company:
#
#         return item
#
#
# print(stoke_prices([("parth",10000),("keval", 80)]))



# -------------------------------------------------------------------------------------------------------------

# def best_employee(work_hours):
#
#     current_max = 0
#     employee_of_month = ''
#
#     for employee , hours in work_hours:
#         if hours > current_max:
#             current_max = hours
#             employee_of_month = employee
#
#         else:
#             pass
#     return employee_of_month , current_max
#
# work_hours = [("pp",6744),("kh",534)]
# print(best_employee(work_hours))





