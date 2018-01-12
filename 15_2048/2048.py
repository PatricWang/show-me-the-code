mat = [[i for i in range(4)] for j in range(4)]
#print mat

#for i in range(4):
#print'{0:^6} {1:^6} {2:^6} {3:^6}'.format([mat[0][i] for i in range(4)])

#str(mat[0][i]).center(6)

def PrintMat():
    for i in range(4):
        print'{0:^6} {1:^6} {2:^6} {3:^6}'.format(mat[i][0],mat[i][1],mat[i][2],mat[i][3])