import random

name1 = input("Ввведи свое имя: ")
print(f'Привет, {name1}!\nМеня зовут Лунтик - я бот и буду с тобой играть в игру с конфетами! Выиграет тот, кто заберет последние конфеты.\nЕсли готов(а) - нажми любую клавишу....')
print()
input()

igrok = random.randrange(1, 3)
count = int(input("Введи общее количество конфет: "))

if igrok == 1:
    print('Твой ход первый :(')
else:
    print("Первый хожу я :)")

while count > 0:
    if count > 28:
        print(f'возьми не более 28 конфет: ')
        player1 = int(input())
        while player1 > 28:
            print(f'введи число не более 28: ')
            player1 = int(input())
        count = count - player1
        if count > 28:
            print(f'возьми не более 28 конфет: ')
            player2 = random.randrange(1, 3)
            while player2 > 28:
                print(f'Введи число не более 28: ')
                player2 = random.randrange(1, 3)
            count = count - player2
            if count <= 28:
                if igrok == 1:
                    print(f"Осталось {count} конфет! {name1} - ты ваиграл(а)!")
                else:
                    print(f"Осталось {count} конфет! Я - выиграл!")
        else:
            if igrok == 1:
                print(f"Осталось {count} конфет! Я - выиграл!")
            else:
                print(f"Осталось {count} конфет! {name1} - ты ваиграл(а)!")
