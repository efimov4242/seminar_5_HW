# 1.  Создайте программу для игры с конфетами человек против человека.
#     Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому
# игроку, чтобы забрать все конфеты у своего конкурента?
#     a) Добавьте игру против бота
#     b) Подумайте как наделить бота ""интеллектом""

import random

def player_round(max_num, num, player):
    take_candy = -1
    while 0 > take_candy or take_candy > max_num or take_candy > num:
        take_candy = int(input(f'Сколько конфет из {num} возмет игрок {player}? '))
        if take_candy > max_num:
            print(f'Не надо быть жадным - максимально количество конфет которые можно взять -  {max_num}!')
        elif take_candy > num:
            print(f'Осталось всего {num} кофет!')
        elif take_candy == 0:
            print(f'Надо взять минимум одну конфету!')
    return take_candy

def bot_round(max_num, num):
    if num <= max_num:
        take_candy = num
    elif num > max_num and num - max_num <= max_num + 1:
        take_candy = num - max_num - 1
    else:
        take_candy = num - (num // (max_num + 1)) * (max_num + 1) + 1
    take_candy = 1 if take_candy == 0 or take_candy > max_num else take_candy
    print(f'Бот берет {take_candy} конфет(у).')
    return take_candy

candy = 201
max_candy = 28
print(f'  На столе лежит {candy} конфет(а). Играют два игрока делая ход друг после друга. \
Первый ход определяется жеребьёвкой.\nЗа один ход можно забрать не более чем {max_candy} конфет. \
Все конфеты оппонента достаются сделавшему последний ход. Если хотите играть с ботом - введите имя "bot".')
p_name = []
p_name.append(input("Имя первого игрока: "))
p_name.append(input("Имя второго игрока: "))

in_game_player = random.randint(0,1)

print(f'Первым ходит игрок {p_name[in_game_player]}')

game_candy = candy

while game_candy > 0:
    if 'bot' not in p_name[in_game_player]:
        game_candy -= player_round(max_candy, game_candy, p_name[in_game_player])
    else:
        game_candy -= bot_round(max_candy, game_candy)
    print(f'Осталось конфет - {game_candy}.')
    in_game_player = int(not bool(in_game_player))
print(f'Победил игрок {p_name[int(not bool(in_game_player))]}!')



# 2. Создайте программу для игры в 'Крестики-нолики'
# НЕОБЯЗАТЕЛЬНО Добавить игру против бота с интеллектом

print('Не хотели бы сыграть в крестики-нолики!')

board = list(range(1,10))

def design_board(board):
    print('-'*12)
    for i in range(3):
        print('|', board[0+i*3],'|', board[1+i*3], '|', board[2+i*3], '|')
        print('-'*12)

def choice(tic_tac):
    flag = False
    while not flag:
        player_index = input('Ваш ход, выберите цифру клетки ' + tic_tac + ' --> ')
        try:
            player_index =int(player_index)
        except:
            print('Нажмите кнопку соответсвующую цифре в клетке')
            continue
        if player_index >= 1 and player_index <= 9:
            if(str(board[player_index-1]) not in 'XO'):
                board[player_index-1] = tic_tac
                flag = True
            else:
                print('Здесь уже что-то стоит')
        else:
            print('Попробуйте еще раз')

def victory_check(board):
    victory = ((0,1,2),(3,4,5),(6,7,8),
               (0,3,6),(1,4,7),(2,5,8),
               (0,4,8),(2,4,6))
    for i in victory:
        if board[i[0]] == board[i[1]] == board[i[2]]:
            return board[i[0]]
    return False

def game(board):
    counter =0
    vic = False
    while not vic:
        design_board(board)
        if counter % 2 == 0:
            choice('X')
        else:
            choice('0')
        counter +=1
        if counter > 4:
            tt_win = victory_check(board)
            if tt_win:
                print(tt_win,'Победа')
                vic = True
                break
            if counter == 9:
                print('Победила, ДРУЖБА)')
                break
        design_board(board)
game(board)


# 3. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# aaaaabbbcccc -> 5a3b4c
# 5a3b4c -> aaaaabbbcccc


def encode(s):

    encoding = "" # сохраняет выходную строку

    i = 0
    while i < len(s):
        # подсчитывает количество вхождений символа в индексе `i`
        count = 1

        while i + 1 < len(s) and s[i] == s[i + 1]:
            count = count + 1
            i = i + 1

        # добавляет к результату текущий символ и его количество
        encoding += str(count) + s[i]
        i = i + 1

    return encoding


if __name__ == '__main__':

    s = 'aaaaabbbcccc'
    print(encode(s))



