import requests
import lxml.html

url = "http://tieba.baidu.com/p/2166231880"
url1 = 'http://tech.sina.com.cn/roll/2018-01-08/doc-ifyqiwuw8036983.shtml'
path = "./img/"

page = requests.get(url1).text
doc = lxml.html.document_fromstring(page)
for idx,el in enumerate(doc.cssselect('img.BDE_Image')):
    with open(path + '%03d.jpg' % idx, 'wb') as f:
        f.write(requests.get(el.attrib['src']).content)
    #print el.attrib['src']
    # if el.attrib['src'].endswith('.jpg'):
    #     with open(path + '%03d.jpg' % idx,'wb') as f:
    #         f.write(requests.get(el.attrib['src']).content)