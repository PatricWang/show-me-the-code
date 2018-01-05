#coding:utf-8
from goose import Goose
from goose.text import StopWordsChinese
from bs4 import BeautifulSoup
import urllib2

url = 'http://blog.csdn.net/tyronne/article/details/46930647'
html_doc = r'src.html'
dst_file = r'cleanText.txt'

html_page = urllib2.urlopen(url)
links = BeautifulSoup(html_page,'lxml').findAll('a')
links = [i.get('href') for i in links if i.get('href') and not i.get('href').startswith('javascript:')]
proto,rest = urllib2.splittype(url)
tmp = urllib2.splithost(rest)
domain = urllib2.splithost(rest)[0]
links = map(lambda i : proto + '://' + domain + i if i[0] == '/' else url + i if i[0] == '#' else i,links)
for link in links:
    print link


with open(html_doc,'r')as f:
    words = f.read()
g = Goose({'stopwords_class':StopWordsChinese})
article = g.extract(raw_html = words)

#存txt
with open(dst_file,'w') as f:
    f.write(article.title.encode('utf8') + '\n')
    f.write(article.cleaned_text.encode('utf8'))
#print(article.title)
#print(article.cleaned_text)