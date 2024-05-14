# Battleship game
# Author = Behdad
def main():
    print_banner()
    letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    grid_content = print_grid(letters, numbers)
    print(grid_content)
    row_to_hit = input("Enter your row from A to J: ").upper()
    column_to_hit = int(input("Enter your column from 1 to 10: "))
    boolian = check_to_hit_correct(row_to_hit, column_to_hit, letters, numbers)
    while boolian != True:
        row_to_hit = input("Enter your row from A to J: ").upper()
        column_to_hit = int(input("Enter your column from 1 to 10: "))
        boolian = check_to_hit_correct(row_to_hit, column_to_hit, letters, numbers)
    player_1(row_to_hit, column_to_hit, grid_content)

def print_banner():
    print(f"**********")
    print(f"BATTLE SHIP 2024")
    print(f"----------")
    print(f"Created by: Behdad Khorasani")
    print(f"**********")

def print_grid(row, column):
    result_grid = []
    for letter in row:
        for number in column:
            # empty box
            print(f"\u2610 ", end="")
            # checked box \u2611
            pair_tuple = (letter, number)
            result_grid.append(pair_tuple)
    result_grid.sort()
    return result_grid

def check_to_hit_correct(row_to_hit, column_to_hit, correct_letters, correct_numbers):
    if row_to_hit in correct_letters and column_to_hit in correct_numbers:
        return True
    else:
        return False

def player_1(row_selected, column_selected, grid_list):
    for value in grid_list:




main()
