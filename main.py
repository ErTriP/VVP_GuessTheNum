import random

print("Я загадал число в промежутке от 0 до 100. Сможешь угадать?")
Num = int(random.random()*100)
print(Num)

while True:
    print("Y/N")
    Answer = input();
    if Answer == 'N':
        quit()
    elif Answer == 'Y':
        while True:
            print("Введи число")
            PNum = int(input())
            if PNum == Num:
                print("Ты угадал!")
                quit()
            elif PNum > Num:
                print("Моё число меньше")
            elif PNum < Num:
                print("Моё число больше")
    else:
        print("Неверный ввод")