from random import randint

rand_num = randint(0, 100)

while True:
    a = int(input())
    if a > rand_num:
        print("Загаданное число меньше!")
    elif a < rand_num:
        print("Загаданное число больше!")
    else:
        print("Вы угадали число!")