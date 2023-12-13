import random
import math

lower = int(input("Enter your lowest number: "))
upper = int(input("Enter your highest number: "))

x = random.randint(lower, upper)
maths_log = math.log(upper - lower + 1,2)
print(f"you have ony {round(maths_log)} chanses")

count = 0

while count < maths_log:
    count+= 1

    guess = int(input("Enter your guessing number:- "))

    if x == guess:
        print(f"Congratulations you have did it in {count} try")
        break

    elif x > guess:
        print("you have guess it too small")

    elif x < guess:
        print("You have guess it too high")

if count >= maths_log:
    print(f"The number is  {x}")
else:
    print("Better luck next time! ")





