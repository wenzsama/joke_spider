#coding:utf-8
import urllib2


class Downloader(object):
    
    
    def download(self,url):
        if url is None:
            return None
        user_agent='Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)' 
        headers= { 'User-Agent' : user_agent }  
        req=urllib2.Request(url,headers=headers)
        response=urllib2.urlopen(req)
        if response.getcode()!=200:
            return None
        html_cont=response.read()
        return html_cont
        
    
    


  


