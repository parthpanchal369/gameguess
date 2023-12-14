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

my_string = "bcdefghijklmnopqrstuvwxyza"
new_str = ''
i = 0
for char in my_string:
    i+=1

    if char =="a" or char =="e" or char == "i" or char =="o" or char =="u":
        print(new_str)
        new_str = ''

    else:
        new_str+= char










