# coding:utf-8
import io
import sys
import urllib
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
from bs4 import BeautifulSoup
import codecs

def get_content(url):
    req = urllib.request.urlopen(url)
    html = req.read()
    html = html.decode("utf-8")
    html = BeautifulSoup(html, "html5lib")
    content = html.find(id="content").get_text(strip=True)
    return content


url = "http://www.liudatxt.com/so/11198/"

req = urllib.request.urlopen(url)

data = req.read()
data= data.decode("utf-8")
html = BeautifulSoup(data, "html5lib")

readerlist = html.find(id="readerlist")
i =1
for li in readerlist.find_all("li"):
    i=i+1
    text = li.find("a").get_text()
    link = "http://www.liudatxt.com" + li.find("a").attrs['href']
    print("%s - %s" % (text, link))
    content= get_content(link)
    f = codecs.open("./books/"+str(i)+".txt", "w", "utf-8")
    f.write(content)
    f.close()