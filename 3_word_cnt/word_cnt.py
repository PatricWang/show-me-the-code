from sklearn.feature_extraction.text import CountVectorizer
import numpy as np


vectorizer = CountVectorizer()
text_path = r"1.txt"
with open(text_path,'r') as f:
    s = f.readlines()
    X = vectorizer.fit_transform(s)
words = vectorizer.get_feature_names()
counts = np.sum(X.toarray(),0).tolist()
results = sorted(zip(words,counts),key = lambda x:x[1],reverse = True)
for word,count in results:
    print word,count