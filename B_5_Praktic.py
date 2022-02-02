field = list(range(1, 10))

def draw_field(field):
    for i in range(3):
        print (field[0+i*3], " ", field[1+i*3], " ", field[2+i*3])

def take_input(play_motion):
    valid = False
    while not valid:
        ans_play = input("Куда ставим " + play_motion+"? ")
        ans_play = int(ans_play)

        if ans_play >= 1 and ans_play <= 9:
            if (str(field[ans_play-1]) not in "XO"):
                field[ans_play-1] = play_motion
                valid = True
            else:
                print ("Клетка занята !")
        else:
            print ("Некорректный ввод. Введите число от 1 до 9 чтобы походить.")

def check_win(field):
    win_coord = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(2,4,6),(0,4,8))
    for each in win_coord:
        if field[each[0]] == field[each[1]] == field[each[2]]:
            return field[each[0]]
    return False

def main(field):
    counter = 0
    win = False
    while not win:
        draw_field(field)
        if counter % 2 == 0:
            take_input("X")
        else:
            take_input("O")
        counter += 1
        if counter > 4:
            tmp = check_win(field)
            if tmp:
                print (tmp, "выиграл!")
                win = True
                break
        if counter == 9:
            print ("Ничья!")
            break
    draw_field(field)

main(field)
