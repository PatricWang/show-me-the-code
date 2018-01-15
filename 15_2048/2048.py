# coding:utf-8
import random
import copy
import curses

mat = []
valid_usr_input = ('a', 'w', 's', 'd', 'r', 'q')
usr_cmd = ''
score = 0


def reset_mat():
    global mat
    mat = [[0 for row in range(4)] for col in range(4)]


def print_mat():
    for i in range(4):
        print'{0:^6} {1:^6} {2:^6} {3:^6}'.format(mat[i][0], mat[i][1], mat[i][2], mat[i][3])


def new_num():
    while True:
        if not contain_zero():
            return False
        pos = random.randint(0, 15)
        i = pos / 4
        j = pos % 4
        if not mat[i][j]:
            mat[i][j] = random.choice([2, 4])
            return True


def receive_input():
    global usr_cmd,score
    while True:
        usr_cmd = raw_input("score:{}, ".format(score) + "pls input cmd:").lower()
        if usr_cmd in valid_usr_input:
            break
        else:
            print 'need a valid input:'


def contain_zero():
    for row in mat:
        if 0 in row:
            return True
    return False


def move_left():
    for i in range(4):
        tmp = [num for num in mat[i] if num != 0]
        tmp += [0 for k in range(4 - len(tmp))]
        merge_num(tmp)
        mat[i] = tmp[::]


def merge_num(tmp):
    j = 0
    global score
    while j < len(tmp) - 1:  # [::-1]:
        if tmp[j] == tmp[j + 1]:
            tmp[j] += tmp[j + 1]
            score += tmp[j]
            tmp[j + 1] = 0
            if j + 2 < len(tmp):
                tmp[j + 1:-1] = tmp[j + 2:]
                tmp[-1] = 0
        j += 1


def move_up():
    for j in range(4):
        tmp = [0, 0, 0, 0]
        k = 0
        for row in mat:
            if row[j]:
                tmp[k] = row[j]
                k = k+1
        merge_num(tmp)
        k = 0
        for row in mat:
            row[j] = tmp[k]
            k += 1


def move_down():
    for j in range(4):
        tmp = [0, 0, 0, 0]
        k = 0
        for row in mat[::-1]:
            if row[j]:
                tmp[k] = row[j]
                k = k+1
        merge_num(tmp)
        k = 0
        tmp.reverse()
        for row in mat:
            row[j] = tmp[k]
            k += 1


def move_right():
    for i in range(4):
        tmp = [num for num in mat[i][::-1] if num != 0]
        tmp += [0 for k in range(len(mat[i]) - len(tmp))]
        merge_num(tmp)
        mat[i] = tmp[::-1]


def exit_game():
    print 'exit'
    exit()


def main():
    usr_cmd_dic = {
        'w':move_up,
        'a':move_left,
        's':move_down,
        'd':move_right,
        'r':reset_mat,
        'q':exit_game
    }
    reset_mat()
    game_continue = True
    new_num()
    while game_continue:
        print_mat()
        receive_input()
        tmp_mat = copy.deepcopy(mat)    # tmp_mat = mat的话等于tmp_mat是mat的引用，tmp_mat会跟着mat变
        usr_cmd_dic[usr_cmd]()
        if tmp_mat == mat and contain_zero():
            print 'same'
            continue
        game_continue = new_num()

    print 'over, sorce= %d' % score


def draw(screen):
    screen.addstr('qqqqqqq\n')
    screen.addstr('------ ------ ------ ------\n')
    def print_row(row):
        screen.addstr(''.join('|{: ^5}'.format(num) if num > 0 else '|     'for num in row) + '|\n')

    for row in mat:
        print_row(row)
        screen.addstr('------ ------ ------ ------\n')
    screen.getch()

reset_mat()
new_num()
curses.wrapper(draw)
# main()

# new_num()
# reset_mat()
# tmpm = mat[:]
# mat[0][0] = 2
# mat[1] = [3,3,3,3]
# #tmpm[0]=[1,1,1,1]
# print mat
# print tmpm
# mat[0] = [2,4,2,2] # 16 4 2 4
# print_mat()
# move_up()
# print '\n'*2
# print_mat()
# receive_input()
# new_num()
# print_mat()

# tmp = [2,2,1,3]
# merge_num(tmp)
# print tmp