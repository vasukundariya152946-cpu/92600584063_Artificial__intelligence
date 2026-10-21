# 8. Write a program to solve N-Queens problem. 
# Name:- Kundariya Vasu 
 # Enrollment No :- 92600584063

# no  two queens can be in the smae Rpw 
# mo two queens can be in the same colums , 
# no two queens can be omn the same dialog

def solve_n_queens(n):
    
    board = [-1] * n
    
    def solve(row):

        if row==n:
            for r in range(n):
                for c in range(n):              
                    print("Q" if board[r]== c else "." ,end=" ")
                print()
            return True
        
        for col in range(n):
            safe=True
            
            for r in range(row):
            
                if(board[r] == col or abs(board[r] - col) == abs(r - row)):
                    safe=False
                    break
                
            if safe: 
                board[row]=col
                if solve(row + 1):
                    return True
        return False
    
    if not solve(0):
        print(" No Solution exists")

n=int(input("Enter the number of Queens :"))
solve_n_queens(n)
# Q . . . . 
# . . Q . .
# . . . . Q
# . Q . . .
# . . . Q .