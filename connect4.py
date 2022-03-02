def render(l) -> None:
    for y in l:
        for x in y:
            print(x, end=" ")
        print()


def move(l, move, player) -> list:
    options = [x[move] for x in l]
    print("options", options)
    movey = options.index(0)
    print("movey", movey)
    spot = 0
    while l[spot][move] != 0:
        spot += 1
    l[spot][move] = player
    return l


def check_win(l, player) -> bool:
    # horizontal check
    count = 0
    for horizontal in l:
        for piece in horizontal:
            if piece == player:
                count += 1
                if count >= 4:
                    return True
            else:
                count = 0
    for vertical in range(5):
        for piece in horizontal:
            if piece == player:
                count += 1
                if count >= 4:
                    return True
            else:
                count = 0
    return False


board = [[0] * 7 for i in range(6)]

play = True
player = 1

while play:
    movecol = int(input("column"))
    render(board)
    l = move(board, movecol, player)
    render(l)
    print(check_win(board, player))
    player *= -1
