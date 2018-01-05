#coding:utf-8
from bs4 import BeautifulSoup
import urllib2

def get_links_from_url(url):
    html_page = urllib2.urlopen(url)
    links = BeautifulSoup(html_page,"lxml").findAll('a')
    links = [i.get('href') for i in links if i.get('href') and not i.get('href').startswith('javascript:')]#去掉javascript开头的
    proto, rest = urllib2.splittype(url)
    domain = urllib2.splithost(rest)[0]
    links = map(lambda i : proto + '://' + domain + i if i[0] == '/' else url + i if i[0] == '#' else i,links)#把链接补全
    return links

def get_article_links():
    url = "http://www.jianshu.com/"
    link = get_links_from_url(url)
    links = [i for i in link if i.startswith('http://www.jianshu.com/c/')]#类别
    links_class = list(set(links))
    links_article = list()
    for link in links_class:
        links = get_links_from_url(link)
        links = [i for i in links if i.startswith('http://www.jianshu.com/p/') and not i.endswith('#comments')]#文章
        links = list(set(links))
        links_article.extend(links)
    links_article = list(set(links_article))
    return links_article

from goose import Goose
from goose.text import StopWordsChinese
import os

def save_articles_from_links(links,articles_path):
    g = Goose({'stopwords_class':StopWordsChinese})
    for url in links:
        article = g.extract(url = url)
        valid_title = map(lambda i : " " if not (
            (u'\u4e00' <= i <= u'\u9fff') or
            (u'\u0030' <= i <= u'\u0039') or
            (u'\u0041' <= i <= u'\u005a') or
            (u'\u0061' <= i <= u'\u007a')) else i,article.title)
        # test1 = isinstance(valid_title,basestring)
        # test2 = isinstance(valid_title,list)
        # test3 = isinstance(valid_title, unicode)
        valid_title = ''.join(valid_title)
        # test4 = isinstance(valid_title, basestring)
        # test5 = isinstance(valid_title, unicode)
        # test6 = isinstance(valid_title, str)
        article_file = os.path.join(articles_path,valid_title + '.txt')
        with open(article_file,'w') as f:
            f.write(article.cleaned_text.encode('utf-8'))

#从网站提取文章存入本地文件中
articles_path = r"articles1"
links = get_article_links()
save_articles_from_links(links,articles_path)
print links


#由TF-IDF判断词的重要性
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
import jieba
import os

vectorizer = CountVectorizer()
transformer = TfidfTransformer()
articles_path = r"articles"
corpus = []
titles = []
for root,dirs,files in os.walk(articles_path):
    for title in files:
        titles.append(title)
        file_name = os.path.join(root,title)
        with open(file_name) as f:
            s = f.read()
            words = jieba.lcut(s,cut_all = True)
            s = ' '.join(words)
            corpus.append(s)

tfidf = transformer.fit_transform(vectorizer.fit_transform(corpus))
word = vectorizer.get_feature_names()
weight = tfidf.toarray()
for i in range(len(weight)):
    print "--------------------"
    print "article",i,":",titles[i].decode('gbk')
    w = weight[i][::]
    tmp = zip(word,w)
    tmp = sorted(tmp,key = lambda i : i[1],reverse = True)
    print "weightiest:"
    for j in range(5):
        print "word:",tmp[j][0],"TF-IDF:",tmp[j][1]
