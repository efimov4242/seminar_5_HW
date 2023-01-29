import random

name1 = input("Ввведите имя первого игрока: ")
name2 = input("Введите имя второго игрока: ")

igrok = random.randrange(1, 3)
count = int(input("Введите количество конфет: "))

if igrok == 1:
    print("Первый ход делает", name1)
else:
    print("Первый ход делает", name2)

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
            player2 = int(input())
            while player2 > 28:
                print(f'Введи число не более 28: ')
                player2 = int(input())
            count = count - player2
            if count <= 28:
                if igrok == 1:
                    print(f"Осталось {count} конфет, их забирает {name1}. Выиграл(a) {name1}")
                else:
                    print(f"Осталось {count} конфет, их забирает {name2}. Выиграл(a) {name2}")
        else:
            if igrok == 1:
                print(f"Осталось {count} конфет, их забирает {name2}. Выиграл(a) {name2}")
            else:
                print(f"Осталось {count} конфет, их забирает {name1}. Выиграл(a) {name1}")