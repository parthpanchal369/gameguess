from googlesearch import search

print("Welcome to the google search here: ")

query = input("what do you want to search on google ? ")

for i in search(query, start=0, stop=10):
    print(i)