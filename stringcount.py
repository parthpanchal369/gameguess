# def vowels_count(s):
#     vowels = ''
#     count = ''
#
#     for i in s:
#         if i.lower() in('a','e','i','o','u') :
#             vowels+= i
#
#         elif i.lower() in (s):
#             count+= i
#
#
#     return vowels , count
#
# string = input("Enter your string: ")
# result = vowels_count(string)
# print(result)

# def vowels_count(s):
#     vowels = []
#
#     for char in s:
#         if char.lower() in ('a', 'e', 'i', 'o', 'u'):
#             vowels.append(char)
#
#     return vowels
#
# input_str = input("Enter your string: ")
# result = vowels_count(input_str)
# print(result)


# def vowel_diff(s):
#     new_data = ''
#     alpha = ''
#     vowels = 'a'
#
#     for i in s:
#         if i.lower() in vowels:
#             new_data+= i.split(a)
#
#
#         elif i in alpha:
#             alpha+= i
#
#
#     return new_data
#
# s = input("Enter your string: ")
# result = vowel_diff(s)
# print(result)


# my_string = "bcdahkleaijkaipqrsaifvmkakl"
# result = my_string.split("a")
# print(result)

# my_string = "abcdefghijklmnopqrstuvwxyzABCDEfghijklmnopqrstuvwxyz"
# new_str = ''
#
# for char in my_string:
#
#     if char.lower() not in ('a','e','i','o','u'):
#         new_str+= char
#
#     else:
#         print(new_str)
#         new_str =''
#
# print(new_str)


my_string = input("Enter your string: ")
new_string = ''

for val in my_string:

    if val.lower() not in ('a','e','i','o','u'):
        new_string += val

    elif new_string == " ":
        continue

    else:
        if new_string:
            print(new_string)
        new_string= ''

if new_string:
    print(new_string)
#

# my_string = input("string here: ")
# new_string = ''
#
# for val in my_string: 
#     if val.lower() not in ('a', 'e', 'i', 'o', 'u',):
#         new_string += val
#     elif val == ' ':
#         continue
#     else:
#         if new_string:
#             print(new_string)
#         new_string = ''
#
# if new_string:
#     print(new_string)

















