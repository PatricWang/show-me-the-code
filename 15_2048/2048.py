mat = [[i for i in range(4)] for j in range(4)]
#print mat

#for i in range(4):
#print'{0:^6} {1:^6} {2:^6} {3:^6}'.format([mat[0][i] for i in range(4)])

str(mat[0][i]).center(6)

print'{0:^6} {1:^6} {2:^6} {3:^6}'.format(mat[0][0],mat[0][1],mat[0][2],mat[0][3])