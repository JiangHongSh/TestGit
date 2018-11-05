import urllib.parse

class HtmlOutputer(object):
    def __init__(self):
        self.datas = []

    def collect_data(self,data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        fhand = open('output2.html', 'w', encoding='utf-8')

        fhand.write('<!DOCTYPE html>')
        fhand.write('<html lang="en">')
        fhand.write("<head><meta http-equiv='content-type' content='text/html;charset=utf-8'></head>")
        fhand.write('<link rel="stylesheet" href="./layout.css">')
        fhand.write('<body>')
        fhand.write('<div id="wrap">')

        count=1
        for data in self.datas:
            fhand.write('<div class="block">')
            fhand.write('<h2>%d. %s</h2>' % (count,data['title']))
            # print(data)
            fhand.write('<p>%s</p>' % data['summary'])
            fhand.write('</div>')
            count +=1

        fhand.write('</div>')
        fhand.write('</body>')
        fhand.write('</html>')
