#导入包转换链接中的中文字符
import urllib.parse

class HtmlOutputer(object):
    def __init__(self):
        self.datas = []
        self.names = []

    def collect_data(self,data,name):
        if data is None:
            return
        self.datas=data
        self.names=name

    def output_html(self):
        fhand = open('D://HTML/'+self.names[0]+'.html', 'w', encoding='utf-8')

        fhand.write('<!DOCTYPE html>')
        fhand.write('<html lang="en">')
        fhand.write("<head><meta http-equiv='content-type' content='text/html;charset=utf-8'></head>")
        fhand.write('<link rel="stylesheet" href="./layout.css">')
        fhand.write('<body>')
        fhand.write('<div id="wrap">')

        count=1
        fhand.write('<div class="block">')
        fhand.write('<h2>%d. %s</h2>' % (count,self.datas['title']))
        summary_node = self.datas['summary']
        for summary in summary_node:
            fhand.write('<p>%s</p>' % summary.get_text())
        imgs_node = self.datas['imgs']
        for img in imgs_node:
            fhand.write('<img src="%s"></img>' % img['src'])
        fhand.write('</div>')
        count +=1

        fhand.write('</div>')
        fhand.write('</body>')
        fhand.write('</html>')
