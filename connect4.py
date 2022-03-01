def render(l):
    for y in l:
        for x in y:
            print(x, end=" ")
        print()

def move(l, move):
    options = [x[move] for x in l]
    print("options", options)
    movey = options.index(0)
    print("movey", movey)
    spot = 0
    while l[spot][move] != 0:
        spot +=1
    l[spot][move] = 1
    return l

board = [[0] * 7 for i in range(6)]

play = True

while play:
    movecol = int(input("column"))
    render(board)
    l = move(board, movecol)
    render(l)