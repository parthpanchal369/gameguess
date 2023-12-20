# def myfunc(*args):
#     return [a for a in args if a%2 == 1]
#
# result =myfunc(1,2,3,4,5,6)
# print(result)



# def palindrome(string):
#
#     new_str = str(string)
#
#     return new_str == string[::-1]
#
# string = input("Enter your string here:  ")
#
# if palindrome(string):
#     print("It is palindrome")
#
# else:
#     print("It is not a palindorme")

list1 =['parth.panchal@prama.ai',
        'vrutik@prama.ai',
        'parthpanchal801@gmail.com',
        'kevalradadiya@gmai.com'
        ]


list2 = ['parth.panchal@prama.ai',
         'modi.vedant@prama.ai',
         'yash.makvana@prama.ai',
         'vrutik@prama.ai',
         'udai.hirpara@prama.ai']

regester_email = []

for name in list1:
    if name.endswith("@prama.ai"):
        regester_email.append(name)
#
print("Who have register for meetup from prama: ", regester_email)


# list1 = ['parth.panchal@prama.ai',
#          'vrutik@prama.ai',
#          'parthpanchal801@gmail.com',
#          'kevalradadiya@gmai.com']
#
# list2 = ['parth.panchal@prama.ai',
#          'modi.vedant@prama.ai',
#          'yash.makvana@prama.ai',
#          'vrutik@prama.ai',
#          'udai.hirpara@prama.ai']
#
# common_prama_emails = []
#
# for email1 in list1:
#     if email1.endswith('@prama.ai') and email1 in list2:
#         common_prama_emails.append(email1)
#
# print("Common email addresses with '@prama.ai':", common_prama_emails  )
#
#




