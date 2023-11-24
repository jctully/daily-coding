
'''
This problem was asked by Dropbox.

Conway's Game of Life takes place on an infinite two-dimensional board of square cells. Each cell is either dead or alive, and at each tick, the following rules apply:

Any live cell with less than two live neighbours dies.
Any live cell with two or three live neighbours remains living.
Any live cell with more than three live neighbours dies.
Any dead cell with exactly three live neighbours becomes a live cell.
A cell neighbours another cell if it is horizontally, vertically, or diagonally adjacent.

Implement Conway's Game of Life. It should be able to be initialized with a starting list of live cell coordinates and the number of steps it should run for. Once initialized, it should print out the board state at each step. Since it's an infinite board, print out only the relevant coordinates, i.e. from the top-leftmost live cell to bottom-rightmost live cell.

You can represent a live cell with an asterisk (*) and a dead cell with a dot (.).
'''

def print_board(live_list):
    xmin = min(live_list)[0]
    xmax = max(live_list)[0]
    ymin = min(live_list, key = lambda c : c[1])[1]
    ymax = max(live_list, key = lambda c : c[1])[1]

    lo = min(xmin, ymin)
    hi = max(xmax, ymax)
    for i in range(lo, hi+1):
        for j in range(lo, hi+1):
            if (i,j) in live_list:
                print('*', end = '')
            else:
                print('.', end='')
        print()
    print()

def live_neighbors(i,j,live_list):
    live = 0
    for x,y in live_list:
        if x == i and y == j: continue
        if abs(x - i) < 2 and abs(y - j) < 2:
            live += 1
    return live

def conway(live_list, n_steps):

    for _ in range(n_steps):
        xmin = min(live_list)[0]
        xmax = max(live_list)[0]
        ymin = min(live_list, key = lambda c : c[1])[1]
        ymax = max(live_list, key = lambda c : c[1])[1]

        live_list_new = []
        for i in range (xmin-1, xmax+2):
            for j in range(ymin-1, ymax+2):
                ln = live_neighbors(i,j,live_list)
                if (i,j) in live_list:
                    if 1 < ln < 4:
                        live_list_new.append((i,j))
                elif ln == 3:
                    live_list_new.append((i,j))

        print_board(live_list_new)
        live_list = live_list_new

lis = [(2, 1), (2, 2), (2, 3)]
conway(lis, 5)