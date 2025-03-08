import random

q =random.randint(1,10)

answer=int(input('Вгадай число'))

if answer== q:
    print("Yes", q)
else:
    print("No", q)