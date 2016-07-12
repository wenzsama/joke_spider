
#coding:utf-8
import bs4
import re


class Parser(object):
    def _get_new_data(self,full_url,page,soup):
        
        cont_data=[]
        links=soup.find_all('div',class_='content')
        for link in links:
            cont=link.get_text()
            cont_data.append(cont)
           
        return cont_data   
    
    def parse(self,full_url,page,html_cont):
        if full_url is None or html_cont is None:
            return 
        soup=bs4.BeautifulSoup(html_cont,'html.parser',from_encoding='utf-8')
        new_data=self._get_new_data(full_url,page,soup)
        return new_data
    



