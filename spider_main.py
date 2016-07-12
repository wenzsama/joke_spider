#coidng:utf-8

from baike import  baike_downloader, baike_parser, baike_outputer


class SpiderMain(object):
    def __init__(self):
        self.downloader=baike_downloader.Downloader()
        self.parser=baike_parser.Parser()
        self.outputer=baike_outputer.Outputer()
        
    def craw(self,root_url):
        for i in range(1,3):
            full_url=root_url+str(i)
            try:
                print 'craw'+str(i)+'page'
                html_cont=self.downloader.download(full_url)
                print html_cont;
                print 'cont ok'
                new_data=self.parser.parse(full_url,str(i),html_cont)
                print 'data get ok'
                print new_data[0]
                self.outputer.collect_data(new_data)
                print 'collect ok'
            except:
                print 'craw failed at page:'+str(i)
        self.outputer.output_html()
    
    
if __name__=="__main__":    
    root_url='http://www.qiushibaike.com/hot/page/'
    spider=SpiderMain()
    spider.craw(root_url)
    