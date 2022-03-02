def render():
    global board
    for y in board:
        for x in y:
            print(x, end=" ")
        print()


def move(move: int, player: int) -> int:
    global board
    options = [x[move] for x in board]
    print("options", options)
    movey = options.index(0)
    print("movey", movey)
    spot = 0
    while board[spot][move] != 0:
        spot += 1
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
        spot = board[movex][movey]
        try:
            spot = board[movex][movey]
        except IndexError:
            pass
        if board[movey][x] == player:
            counter += 1
        else:
            counter = 0
        if counter > 3:
            return True
    #vertical win
    for y in range(movey-3,movey+4):
        if board[y][movex] == player:
            counter += 1
        else:
            counter = 0
        if counter > 3:
            return True
    #diagonal 1 down
    y = movey-3
    for x in range(movex-3,movex+4):
        if board[x][y] == player:
            counter += 1
        else:
            counter = 0
        if counter > 3:
            return True
    y += 1
    #diagonal 2 up
    y = movey-3
    for x in range(movex-3,movex+4):
        if board[x][y] == player:
            counter += 1
        else:
            counter = 0
        if counter > 3:
            return True
    y += 1
    
board = [[0] * 7 for i in range(6)]

play = True
player = 1

while play:
    movecol = int(input("column"))
    render()
    y = move(movecol, player)
    render(board)
    print(check_win_move(player))
    player *= -1