N = 3
play_field = [["-","-","-"],["-","-","-"],["-","-","-"]]
count = 0

def check_turn(ind):
    global play_field
    x = ind // 10 - 1
    y = ind % 10 - 1
    # rows and columns check
    if play_field[x][2] == play_field[x][1] == play_field[x][0]:
        return True
    elif play_field[0][y] == play_field[1][y] == play_field[2][y]:
        return True
    else:
        if abs(x - y) == 0: # 1 diagonal
            return play_field[0][0] == play_field[1][1] == play_field[2][2]
        elif abs(x - y) == 2: # 2 diagonal
            return play_field[0][2] == play_field[1][1] == play_field[2][0]
        else:
            return False

def print_field():
    print("  1 2 3")
    for i in range(3):
        print(i + 1, end=" ")
        for j in range(3):
            print(play_field[i][j], end=" ")
        print()

while True:
    step = int(input(f"\n Player {count % 2 + 1}, please input field number: "))

    if ((step // 10) not in [1,2,3] and (step % 10) not in [1,2,3]):
        print("\n index of field is wrong. try again")
        continue
    else:
        play_field[step // 10 - 1][step % 10 - 1] = "x" if count % 2 == 0 else "o"
        print_field()
        if check_turn(step):
            print(f"\n Player {count % 2 + 1} is winner")
            break

        count += 1
        if count > 8:
            print("\n No one is winner")
            break



