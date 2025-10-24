import random
import bext
import sys

tile_types = (0, 1, 2, 3, 4, 5)
color_map = {
    0: "red",
    1: "green",
    2: "blue",
    3: "yellow",
    4: "cyan",
    5: "purple"
}

board_width = 14
board_height = 14
moves_per_game = 20
upper_border = chr(9472)
vertical_border = chr(9474)
top_left_corner = chr(9484)
top_right_corner = chr(9488)
bottom_left_corner = chr(9492)
bottom_right_corner = chr(9496)
tile = chr(9608)

def get_new_board():
    board = {}
    for x in range(board_width):
        for y in range(board_height):
            board[(x, y)] = random.choice(tile_types)

    for _ in range(board_width * board_height):
        x = random.randint(0, board_width - 2)
        y = random.randint(0, board_height - 1)
        board[(x+1, y)] = board[(x, y)]
    return board

def display_board(board):
    bext.fg("white")
    print(top_left_corner + (upper_border * board_width) + top_right_corner)
    for y in range(board_height):
        if y == 0:
            print(">", end= "")
        else:
            print(vertical_border, end="")
        for x in range(board_width):
            bext.fg(color_map[board[(x, y)]])
            print(tile, end="")
        bext.fg("white")
        print(vertical_border)
    print(bottom_left_corner + (upper_border * board_width) + bottom_right_corner)

def ask_player_for_move():
    while True:
        result_dict = {"R":0, "G":1, "B":2, "Y":3, "C":4, "P":5}
        bext.fg("white")
        print("Choose one of ", end='')
        bext.fg("red")
        print("(R)ed ", end='')
        bext.fg("green")
        print("(G)reen ", end='')
        bext.fg("blue")
        print("(B)lue ", end='')
        bext.fg("yellow")
        print("(Y)ellow ", end='')
        bext.fg("cyan")
        print("(C)yan ", end='')
        bext.fg("purple")
        print("(P)urple ", end='')
        bext.fg("white")
        print("(Q)uit")
        response = input("> ").upper()
        if response == "Q":
            sys.exit()
        elif response not in result_dict and response != "Q":
            print("Invalid input")
            continue
        else:
            return result_dict[response]

def change_tile(tile_color, board, x, y, color_to_change=None):
    if x == 0 and y == 0:
        color_to_change = board[(x, y)]
        if color_to_change == tile_color:
            return
    board[(x, y)] = tile_color
    if x > 0 and board[(x-1, y)] == color_to_change:
        change_tile(tile_color, board, x-1, y, color_to_change)
    if x < board_width - 1 and board[(x+1, y)] == color_to_change:
        change_tile(tile_color, board, x+1, y, color_to_change)
    if y > 0 and board[(x, y-1)] == color_to_change:
        change_tile(tile_color, board, x, y-1, color_to_change)
    if y < board_height - 1 and board[(x, y+1)] == color_to_change:
        change_tile(tile_color, board, x, y+1, color_to_change)


def check_win(board):
    color = board[(0, 0)]
    for x in range(board_width):
        for y in range(board_height):
            if board[(x, y)] != color:
                return False
    return True


print("Welcome to flooder game")
new_board = get_new_board()
moves_left = moves_per_game

while moves_left > 0:
    display_board(new_board)
    print(f"Moves left: {moves_left}")
    player_move = ask_player_for_move()
    change_tile(player_move, new_board, 0, 0)
    moves_left -= 1
    if check_win(new_board):
        print("You won the game")
        break
else:
    print("You loose motherflecker, You ran out of moves(in case you haven't heard motherflecker, watch the series SUITS)")