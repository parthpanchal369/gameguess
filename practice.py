def myfunc(*args):
    return [a for a in args if a%2 == 0]

result =myfunc(1,2,3,4,5,6)
print(result)