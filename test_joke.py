#coding:utf-8
import urllib2
import bs4
import re


url='http://www.qiushibaike.com/hot/page/'
user_agent='Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)' 
headers= { 'User-Agent' : user_agent }  
req=urllib2.Request(url,headers=headers)
response=urllib2.urlopen(req)
html=response.read()

print html

print 'now get data'
soup=bs4.BeautifulSoup(html,'html.parser',from_encoding='utf-8')

links=soup.find_all('div',class_='content')
for link in links:
    print link.get_text()

#下面方法也行
#myItems = re.findall('<div.*?class="content".*?>(.*?)</div>',html.encode('utf-8'),re.S)  
#items=[]
#for item in myItems:    
            # item 中第一个是div的标题，也就是时间    
            # item 中第二个是div的内容，也就是内容    
    #items.append(item)    
        
#print items[2]   
    

