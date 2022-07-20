N = 3
play_field = [["-","-","-"],["-","-","-"],["-","-","-"]]
count = 0
check_index = []

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
    s = input(f"\n Player {count % 2 + 1}, please input field number: ")

    if s.isdigit():
        step = int(s)

        if step // 10 not in [1,2,3] and step % 10 not in [1,2,3]:
            print("\n index of field is wrong. try again")
            continue
        else:
            if step in check_index:
                print("\n This step has been already done. try again")
                continue
            else:
                check_index.append(step)

                play_field[step // 10 - 1][step % 10 - 1] = "x" if count % 2 == 0 else "o"
                print_field()
                if check_turn(int(step)):
                    print(f"\n Player {count % 2 + 1} is winner")
                    break

                count += 1
                if count > 8:
                    print("\n No one is winner")
                    break
    else:
        print("\n only numbers are allowed. Try again")
        continue



