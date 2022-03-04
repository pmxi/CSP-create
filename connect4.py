def render():
    global board
    for y in board:
        for x in y:
            if x == 1:
                print("\u001b[31mX\u001b[0m", end=" ")
            elif x == -1:
                print("\u001b[33mO\u001b[0m", end=" ")
            else:
                print("-", end=" ")
        print()
    print("0 1 2 3 4 5 6")


def move(move: int, player: int) -> int:
    global board
    options = [x[move] for x in board]
    print("options", options)
    movey = options.index(0)
    print("movey", movey)
    spot = 5
    while board[spot][move] != 0:
        spot -= 1
    board[spot][move] = player
    return spot


# def check_win(l: list, player: int) -> bool:
#     # horizontal check
#     count = 0
#     for horizontal in l:
#         for piece in horizontal:
#             if piece == player:
#                 count += 1
#                 if count >= 4:
#                     return True
#             else:
#                 count = 0
#     for vertical in range(5):
#         for piece in horizontal:
#             if piece == player:
#                 count += 1
#                 if count >= 4:
#                     return True
#             else:
#                 count = 0
#     return False

# check win around a new move because that is the only place a new win can occur
def check_win_move(movex: int, movey: int, player: int) -> bool:
    global board
    counter = 0
    #horizontal win
    for x in range(movex-3,movex+4):
        if x in range(7):
            spot = board[movey][x]
            if spot == player:
                counter += 1
            else:
                counter = 0
        if counter > 3:
            return True
    #vertical win
    counter = 0
    for y in range(movey-3,movey+4):
        if y in range(6):
            spot = board[y][movex]
            if spot == player:
                counter += 1
            else:
                counter = 0
        if counter > 3:
            return True
    #diagonal 1 down
    counter = 0
    y = movey-3
    for x in range(movex-3,movex+4):
        if x in range(7) and y in range(6):
            spot = board[y][x]
            if spot == player:
                counter += 1
            else:
                counter = 0
        if counter > 3:
            return True
        y += 1
    #diagonal 2 up
    counter = 0
    y = movey+3
    for x in range(movex-3,movex+4): # change movey to x
        if x in range(7) and y in range(6):
            spot = board[y][x]
            if spot == player:
                counter += 1
        if counter > 3:
            return True
        y -= 1
    return False
    
board = [[0] * 7 for i in range(6)]

play = True
player = 1

while play:
    print("P: X") if player == 1 else print("P: O")
    movecol = int(input("column: "))
    y = move(movecol, player)
    render()
    print(check_win_move(movecol, y, player))
    player *= -1