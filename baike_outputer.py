#coding:utf-8


class Outputer(object):
    def __init__(self):
        self.datas=[]
    
    def collect_data(self,data):
        if data is None:
            return 
        self.datas.append(data)
    
    def output_html(self):
        fout=open('outputJoke.html','w')
        fout.write("<html>")
        fout.write("<body>")
        fout.write("<table>")
        count=1;
        for data in self.datas:
            
            for single in data:
                fout.write("<tr>")
                fout.write("<td>%s</td>" % (str(count)+'. '+single))             
                fout.write("</tr>")
                count+=1
        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")
        
        fout.close()    
    



