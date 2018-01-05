#coding:utf-8
import numpy as np,string
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from scipy.sparse import csr_matrix
from bs4 import BeautifulSoup
import urllib2
from goose import Goose
from goose.text import StopWordsChinese
import os
import jieba


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


html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

def bs4Demo():
    soup = BeautifulSoup(html_doc,'html.parser')
    print soup.prettify()
    print soup.title
    print soup.title.name
    print soup.title.string
    print soup.title.parent.name

def get_links_from_url(url):
    html_page = urllib2.urlopen(url)
    links = BeautifulSoup(html_page, "lxml").findAll('a')
    links = [i.get('href') for i in links if
             i.get('href') and not i.get('href').startswith('javascript:')]  # 去掉javascript开头的
    proto, rest = urllib2.splittype(url)
    tmp = urllib2.splithost(rest)
    domain = urllib2.splithost(rest)[0]
    links = map(lambda i: proto + '://' + domain + i if i[0] == '/' else url + i if i[0] == '#' else i, links)  # 把链接补全
    return links

def get_article_links():
    url = "http://www.jianshu.com/"
    link = get_links_from_url(url)
    print link
    links = [i for i in link if i.startswith('http://www.jianshu.com/c/')]#类别
    print links
    links_class = list(set(links))
    links_article = list()
    for link in links_class:
        links = get_links_from_url(link)
        links = [i for i in links if i.startswith('http://www.jianshu.com/p/') and not i.endswith('#comments')]#文章
        links = list(set(links))
        links_article.extend(links)
    links_article = list(set(links_article))
    return links_article

def save_articles_from_links(links,articles_path):
    g = Goose({'stopwords_class':StopWordsChinese})
    for url in links:
        article = g.extract(url = url)
        valid_title = map(lambda i : " " if not (
            (u'\u4e00' <= i <= u'\u9fff') or
            (u'\u0030' <= i <= u'\u0039') or
            (u'\u0041' <= i <= u'\u005a') or
            (u'\u0061' <= i <= u'\u007a')) else i,article.title)
        valid_title = ''.join(valid_title)
        article_file = os.path.join(articles_path,valid_title + '.txt')
        with open(article_file,'w') as f:
            f.write(article.cleaned_text.encode('utf-8'))

def gooseDem():
    url = 'http://news.china.com/domesticgd/10000159/20180104/31912819.html'
    g = Goose()
    article = g.extract(url = url)

    print isinstance(article.title,list)
    tmp = article.title + 'qwe'
    print tmp
    title = ''.join(article.title)
    print article.title
    print type(article.title)
    print article.meta_keywords
    print article.meta_description

def collect_keywd():
    vectorizer = CountVectorizer()
    transformer = TfidfTransformer()
    articles_path = r"articles1"
    corpus = []
    titles = []
    for root, dirs, files in os.walk(articles_path):
        for title in files:
            titles.append(title)
            file_name = os.path.join(root, title)
            with open(file_name) as f:
                s = f.read()
                words = jieba.lcut(s, cut_all=True)
                s = ' '.join(words)
                corpus.append(s)

    tfidf = transformer.fit_transform(vectorizer.fit_transform(corpus))
    word = vectorizer.get_feature_names()
    weight = tfidf.toarray()
    for i in range(len(weight)):
        print "--------------------"
        print "article", i, ":", titles[i].decode('gbk')
        w = weight[i][::]
        tmp = zip(word, w)
        tmp = sorted(tmp, key=lambda i: i[1], reverse=True)
        print "weightiest:"
        for j in range(5):
            print "word:", tmp[j][0], "TF-IDF:", tmp[j][1]

def jiebaDemo():
    seg_list = jieba.cut("我来到北京清华大学",cut_all = True)
    print("Full Mode: " + "/".join(seg_list))

    seg_list = jieba.cut("我来到北京清华大学",cut_all = False)
    print("Default Mode: " + "/".join(seg_list))

    seg_list = jieba.cut("他来到了网易杭研大厦")
    print(",".join(seg_list))

    seg_list = jieba.cut_for_search("小明硕士毕业于中国科学院计算所，后在日本京都大学深造")  # 搜索引擎模式
    print(", ".join(seg_list))

    seg_list = jieba.lcut("小明硕士毕业于中国科学院计算所，后在日本京都大学深造")  # 搜索引擎模式
    print(", ".join(seg_list))

if __name__ == '__main__':
    collect_keywd()