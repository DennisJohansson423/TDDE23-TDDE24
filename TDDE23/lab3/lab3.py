def choose(n, k):
    if 2*k < n:
        k = n-k
    if k == 0 or k == n:
        return 1
    else:
        return fac(n,k)//fac(n-k,0)
    
def fac(n,k):
    if n == 1:
        return 1
    elif n == k:
        return 1
    else:
        return n * fac(n-1,k)


def new_board():
    return dict()

def is_free(board,x,y):
    return not (x,y) in board

def place_piece(board,x,y,name):
    if is_free(board,x,y):
        board[(x,y)] = name
        return True
    return False

def get_piece(board,x,y):
    if is_free(board,x,y):
        return False
    return board[(x,y)]

def remove_piece(board,x,y):
    if is_free(board,x,y):
        return False
    del board[(x,y)]
    return True

def move_piece(board,x,y,new_x,new_y):
    if not is_free(board,x,y) and is_free(board,new_x,new_y):
        name = get_piece(board,x,y)
        place_piece(board, new_x,new_y,name)
        remove_piece(board,x,y)
        return True
    return False

def count(board,direction,place,name):
    if direction == "column":
        index = 0
    else:
        index = 1
    num = 0
    for cordinates in board:
        if cordinates[index] == place and board[cordinates] == name:
            num += 1

    return num

def nearest_piece(board,x,y):
    if not board:
        return False
    min_lenght = None
    for cordinates in board:
        distans = (x - cordinates[0])**2 +(y - cordinates[1])**2
        distans = distans **(1/2)
        if min_lenght == None:
            min_lenght = (cordinates,distans)
        elif distans < min_lenght[1]:
            min_lenght = (cordinates,distans)
    return min_lenght[0]
