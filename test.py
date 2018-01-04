import numpy as np,string
from sklearn.feature_extraction.text import CountVectorizer
from scipy.sparse import csr_matrix


def genticket():
    idx = np.array([1,2,3,4,5])
    letters = np.array(list(string.ascii_uppercase))

    i = [1,2,3,4,5]
    l = list(string.ascii_uppercase)

    print letters[idx]
    print letters[idx].tostring()

    print l[i]

def sklCountVec():
    texts = ["dog cat fish","dog cat cat","fish bird",'bird',"cat dog"]
    cv = CountVectorizer()
    cv_fit = cv.fit_transform(texts)
    words = cv.get_feature_names()
    ary = cv_fit.toarray()
    wds = np.sum(cv_fit.toarray(),0)

    print(type(wds))
    # print(cv_fit)
    # print(type(cv_fit))
    # print(cv.get_feature_names())
    # print(type(ary))
    # print(ary)
    # print(ary.sum(axis=0))

def csrM():
    indptr = np.array([0,2,4,6])
    indices = np.array([0,1,0,1,0,2])
    data = np.array([1,2,3,4,5,6])
    ary = csr_matrix((data,indices,indptr),shape=(3,4)).toarray()
    print ary

if __name__ == '__main__':
    sklCountVec()