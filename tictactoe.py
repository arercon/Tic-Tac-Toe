def draw_field(string):
    print('---------')
    for x in range(9):
        if x% 3 == 0:
            print("|", end=' ')
        if string[x] == '_' or string[x] == ' ':
            print(' ', end=' ')
        else:
            print(string[x], end=' ')
        if x % 3 == 2:
            print("|\n")
    print('---------')


string='_________'
draw_field(string)
turn = 0
cti = {
    0: "1 3", 1: "2 3", 2: "3 3", 3: "1 2", 4: "2 2", 5: "3 2", 6: "1 1", 7: "2 1", 8: "3 1"
}



def check_win(string):
    winnerX = ''
    winnerO = ''
    if string[0:3] == 'XXX' or string[3:6] == 'XXX' or string[6:9] == 'XXX':
        winnerX = 'X'
    elif (string[0] + string[3] + string[6]) == 'XXX' or (string[1] + string[4] + string[7]) == 'XXX' or (
            string[2] + string[5] + string[8]) == 'XXX':
        winnerX = 'X'
    elif (string[0] + string[4] + string[8]) == 'XXX' or (string[2] + string[4] + string[6]) == 'XXX':
        winnerX = 'X'
    if string[0:3] == 'OOO' or string[3:6] == 'OOO' or string[6:9] == 'OOO':
        winnerO = 'O'
    elif (string[0] + string[3] + string[6]) == 'OOO' or (string[1] + string[4] + string[7]) == 'OOO' or (
            string[2] + string[5] + string[8]) == 'OOO':
        winnerO = 'O'
    elif (string[0] + string[4] + string[8]) == 'OOO' or (string[2] + string[4] + string[6]) == 'OOO':
        winnerO = 'O'
    return winnerX + winnerO


def check_finished(string):
    if check_win(string) == 'X':
        print('X wins')
        return True
    elif check_win(string) == 'O':
        print('O wins')
        return True
    elif '_' in string:
        return False
    else:
        print('Draw')
        return True

while 1:
    coordinates = input('Type 2 coordinates from 1-3(1,1 in left corner, 3,3 in right corner):')
    try:
        val = int(coordinates[0])
        val1 = int(coordinates[-1])
    except ValueError:
        print("You should enter numbers!")
        continue
    if (0 > int(coordinates[0]) > 3) or (0 > int(coordinates[-1]) > 3):
        print("Coordinates should be from 1 to 3!")
        continue
    for index, c in cti.items():
        if c == coordinates:
            if string[index] is not '_':
                print("This cell is occupied! Choose another one!")
            elif turn%2 == 0:
                string = string[:index] + string[index].replace('_', 'X') + string[index + 1:]
                draw_field(string)
                turn +=1
            else:
                string = string[:index] + string[index].replace('_', 'O') + string[index + 1:]
                draw_field(string)
                turn += 1
    if check_finished(string) == True:
        break
