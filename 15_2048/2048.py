import random


mat = [[0 for row in range(4)] for col in range(4)]
valid_usr_input = ('a', 'A', 'w', 'W', 's', 'S', 'd', 'D', 'r', 'q')
# print mat

# for i in range(4):
# print'{0:^6} {1:^6} {2:^6} {3:^6}'.format([mat[0][i] for i in range(4)])

# str(mat[0][i]).center(6)


def print_mat():

    for i in range(4):
        print'{0:^6} {1:^6} {2:^6} {3:^6}'.format(mat[i][0], mat[i][1], mat[i][2], mat[i][3])


def new_num():
    while True:
        pos = random.randint(0, 15)
        i = pos / 4
        j = pos % 4
        if not mat[0][j]:
            mat[0][j] = random.choice([2, 4])
            break
    print 'pos: ', pos, 'i: ', i, 'j: ', j


def receive_input():
    while True:
        usr_move_to = raw_input("move to:")
        if usr_move_to in valid_usr_input:
            break
        else:
            print 'need a valid input:'
            move_left()
            new_num()
            print_mat()


def move_left():
    tmp = [0,0,0,0]
    k = 0
    for j in range(4):
        if mat[0][j]:
            tmp[k] = mat[0][j]
            k += 1
    j = 0
    while j < len(tmp) - 1:  # [::-1]:
        if tmp[j] == tmp[j+1]:
            tmp[j] += tmp[j+1]
            if j+2 < len(tmp):
                tmp[j+1:-1] = tmp[j+2:]
            # tmp[-1] = 0
        j += 1
    mat[0] = tmp[::]


# new_num()
mat[0] = [2,4,2,2] # 16 4 2 4
print_mat()
receive_input()
# new_num()
# print_mat()
