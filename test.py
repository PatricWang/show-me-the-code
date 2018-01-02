import numpy as np,string

def genticket():
    idx = np.array([1,2,3,4,5])
    letters = np.array(list(string.ascii_uppercase))

    i = [1,2,3,4,5]
    l = list(string.ascii_uppercase)

    print letters[idx]
    print letters[idx].tostring()

    print l[i]

if __name__ == '__main__':
    genticket()