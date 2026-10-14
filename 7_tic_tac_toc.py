# TEO PLAYER GAME -TIC-TAC-TOE 
# USING HEurustic function

# display the boiard

def display(board):
    print()
    print(board[0],"|",board[1],"|",board[2])
    print("--+--+--")
    print(board[3],"|",board[4],"|",board[5])
    print("--+--+--")
    print(board[6],"|",board[7],"|",board[8])
    print()
    
# heuristic funcation
def heuristic(board):
    win=[
        (0,1,2),
        (3,4,5),
        (6,7,8),
        (0,3,6),
        (1,4,7),
        (2,5,8),
        (0,4,8),
        (2,4,6)
    ]
    for a,b,c in win:
        if board[a]==board[b]==board[c]=="X":
            return 10
        elif board[a]==board[b]==board[c]=="O":
            return -10
    return 0

# maintain game

board =[" "]*9
player ="X"

for turn in range(9):
    
    display(board)
    print("Player",player)
    
    position = int(input("Enter position (1-9) :")) -1
    
    if position <0 or position>8 or board[position]!=" ":
        print("Invalid position! Try again.")
        continue
    
    board[position]=player
    
    # CHECKVHURESITIC Value 
    
    score=heuristic(board)
    
    if score==10:
        display(board)
        print("Player X wins!")
        break
    
    if score == -10:
        display(board)
        print("Player o wins !")
        break
    
    # change playrer
    if player=="X":
        player="O"
    else:
        player="X"
else:
    display(board)
    print("Game Draw !")
    
    
#     |   |  
# --+--+--
#   |   |
# --+--+--
#   |   |

# Player X
# Enter position (1-9) :2

#   | X |
# --+--+--
#   |   |
# --+--+--
#   |   |

# Player O
# Enter position (1-9) :3

#   | X | O
# --+--+--
#   |   |
# --+--+--
#   |   |

# Player X
# Enter position (1-9) :1

# X | X | O
# --+--+--
#   |   |
# --+--+--
#   |   |

# Player O
# Enter position (1-9) :4

# X | X | O
# --+--+--
# O |   |
# --+--+--
#   |   |

# Player X
# Enter position (1-9) :6

# X | X | O
# --+--+--
# O |   | X
# --+--+--
#   |   |

# Player O
# Enter position (1-9) :9

# X | X | O
# --+--+--
# O |   | X
# --+--+--
#   |   | O

# Player X
# Enter position (1-9) :8

# X | X | O
# --+--+--
# O |   | X
# --+--+--
#   | X | O

# Player O
# Enter position (1-9) :5

# X | X | O
# --+--+--
# O | O | X
# --+--+--
#   | X | O

# Player X
# Enter position (1-9) :7

# X | X | O
# --+--+--
# O | O | X
# --+--+--
# X | X | O

# Game Draw !
# PS D:\vasu\Ai> 