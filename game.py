def show_board(board):
    for i in range(len(board)):
        print (*board[i])
    
def inp(board,x,y,var):
    board[x-1][y-1]=var
def check(board):
    if ((board[0][0]==board[0][1]==board[0][2]!='*')or #0 0
            (board[0][0]==board[1][1]==board[2][2]!='*')or
            (board[0][0]==board[1][0]==board[2][0]!='*')or
            (board[0][1] == board[1][1] == board[2][1] != '*') or
            (board[0][2] == board[1][2] == board[2][2] != '*') or
            (board[1][0] == board[1][1] == board[1][2] != '*') or
            (board[2][0] == board[2][1] == board[2][2] != '*') or
            (board[2][0] == board[1][1] == board[0][2] != '*')

    ):
        return True
def main():
    board=[["*" for i in range(0,3)] for j in range(0,3)]
    count=0
    while(count<=9):
        show_board(board)
        if(count==9):
            print("Ничья")
            break
        if count%2==0:
            print("Ход X.Введите номер строки и столбца(координата[(строка),(столбец)])")
            x=int(input())
            print("Введите номер столбца(координата[(строка),(столбец)])")
            y=int(input())
            inp(board,x,y,'X')
            count+=1
            if check(board):
                print("Игрок 'X' выиграл")
                break
        else:
            print("Ход O.Введите номер строки и столбца(координата[(строка),(столбец)])")
            x = int(input())
            print("Введите номер столбца(координата[(строка),(столбец)])")
            y = int(input())
            inp(board,x,y,'O')
            if check(board):
                print("Игрок 'O' выиграл")
                break
            count += 1


main()