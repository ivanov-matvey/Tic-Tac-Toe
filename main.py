import random


def draw_table():
    return (f"     A   B   C  \n"
            f"   —————————————\n"
            f"1  | {board[0][0]} | {board[0][1]} | {board[0][2]} |\n"
            f"   —————————————\n"
            f"2  | {board[1][0]} | {board[1][1]} | {board[1][2]} |\n"
            f"   —————————————\n"
            f"3  | {board[2][0]} | {board[2][1]} | {board[2][2]} |\n"
            f"   —————————————")


def win():
    for i in wins:
        if (board[i[0][0]][i[0][1]] == board[i[1][0]][i[1][1]]
                == board[i[2][0]][i[2][1]] == player_symbol):
            print("Вы выиграли!")
            return True
        if (board[i[0][0]][i[0][1]] == board[i[1][0]][i[1][1]]
                == board[i[2][0]][i[2][1]] == machine_symbol):
            print("Вы проиграли!")
            return True


def draw():
    count = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] != " ":
                count += 1
    if count == 9:
        print("Ничья.")
        return True


def random_step():
    valid = False
    while not valid:
        rnd_step = [random.randint(0, 2), random.randint(0, 2)]
        if board[rnd_step[0]][rnd_step[1]] not in (
                player_symbol, machine_symbol):
            board[rnd_step[0]][rnd_step[1]] = machine_symbol
            valid = True


def step():
    valid = False
    while not valid:
        cell = input("Клетка: ")
        if ((len(list(cell)) == 2) and (list(cell)[0] in ("A", "B", "C")) and
                (list(cell)[1] in ("1", "2", "3")) and
                (board[cells[list(cell)[1]]][cells[list(cell)[0]]] == " ")):
            valid = True
        else:
            print("[!] Вы ввели неверное значение.")
    board[cells[list(cell)[1]]][cells[list(cell)[0]]] = player_symbol


board = [[" ", " ", " "],
         [" ", " ", " "],
         [" ", " ", " "]]

cells = {"A": 0, "B": 1, "C": 2,
         "1": 0, "2": 1, "3": 2}

wins = [[[0, 0], [0, 1], [0, 2]],
        [[1, 0], [1, 1], [1, 2]],
        [[2, 0], [2, 1], [2, 2]],
        [[0, 0], [1, 0], [2, 0]],
        [[0, 1], [1, 1], [2, 1]],
        [[0, 2], [1, 2], [2, 2]],
        [[0, 0], [1, 1], [2, 2]],
        [[0, 2], [1, 1], [2, 0]]]

queue = random.randint(1, 2)
if queue == 1:
    player_symbol = "X"
    machine_symbol = "O"
    print(draw_table())
    print("Ваш ход первый.")
if queue == 2:
    player_symbol = "O"
    machine_symbol = "X"
    random_step()
    print(draw_table())
    print("Ваш ход второй.")

start = True
while start:
    step()
    random_step()
    print(draw_table())
    if win() or draw():
        start = False
