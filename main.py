import random


def draw_table():
    return (f"     A   B   C  \n"
            f"   —————————————\n"
            f"1  | {cells[1]} | {cells[2]} | {cells[3]} |\n"
            f"   —————————————\n"
            f"2  | {cells[4]} | {cells[5]} | {cells[6]} |\n"
            f"   —————————————\n"
            f"3  | {cells[7]} | {cells[8]} | {cells[9]} |\n"
            f"   —————————————")


def step():
    cell_valid = False
    while not cell_valid:
        cell = input("Клетка: ")
        if cell in cell_names and cells[cell_names.index(cell) + 1] not in (machine_symbol, player_symbol):
            cell_valid = True
        else:
            print("[!] Вы ввели неверное значение.")
    cells[cell_names.index(cell) + 1] = player_symbol


def random_step():
    random_index_valid = False
    while not random_index_valid:
        random_index = random.randint(1, 9)
        if cells[random_index] not in (machine_symbol, player_symbol):
            cells[random_index] = machine_symbol
            random_index_valid = True


def win():
    if ((cells[1] == cells[2] == cells[3] == player_symbol)
            or (cells[4] == cells[5] == cells[6] == player_symbol)
            or (cells[7] == cells[8] == cells[9] == player_symbol)
            or (cells[1] == cells[4] == cells[7] == player_symbol)
            or (cells[2] == cells[5] == cells[8] == player_symbol)
            or (cells[3] == cells[6] == cells[9] == player_symbol)
            or (cells[1] == cells[5] == cells[9] == player_symbol)
            or (cells[3] == cells[5] == cells[7] == player_symbol)):
        print("Вы выиграли!")
        return True
    if ((cells[1] == cells[2] == cells[3] == machine_symbol)
            or (cells[4] == cells[5] == cells[6] == machine_symbol)
            or (cells[7] == cells[8] == cells[9] == machine_symbol)
            or (cells[1] == cells[4] == cells[7] == machine_symbol)
            or (cells[2] == cells[5] == cells[8] == machine_symbol)
            or (cells[3] == cells[6] == cells[9] == machine_symbol)
            or (cells[1] == cells[5] == cells[9] == machine_symbol)
            or (cells[3] == cells[5] == cells[7] == machine_symbol)):
        print("Вы проиграли.")
        return True
    if (cells[1] != " " and cells[2] != " " and cells[3] != " " and cells[4] != " " and cells[5] != " "
            and cells[6] != " " and cells[7] != " " and cells[8] != " " and cells[9] != " "):
        print("Ничья.")
        return True


cell_names = ("A1", "B1", "C1", "A2", "B2", "C2", "A3", "B3", "C3")
cells = {1: " ", 2: " ", 3: " ", 4: " ", 5: " ", 6: " ", 7: " ", 8: " ", 9: " "}

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
    if win():
        start = False
