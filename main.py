import random

top_limit = input("Введите верхнюю границу диапазона: ")

if top_limit.isdigit():
    top_limit = int(top_limit)

    if top_limit <= 0:
        print('Пожалуйста, введите число больше 0 в следующий раз.')
        quit()
else:
    print('Пожалуйста, введите число в следующий раз.')
    quit()

random_number = random.randint(0, top_limit)
attempts = 0

while True:
    attempts += 1
    user_guess = input("Попробуйте угадать число: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('Пожалуйста, введите число в следующий раз.')
        continue

    if user_guess == random_number:
        print("Поздравляю, вы угадали!")
        break
    elif user_guess > random_number:
        print("Ваше число больше загаданного!")
    else:
        print("Ваше число меньше загаданного!")

print("Вы угадали число за", attempts, "попыток")
