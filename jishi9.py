import requests
from bs4 import BeautifulSoup
import pymongo

'''
测试
只是测试
'''
class Xs(object):
    def __init__(self, url):
        self.url = url
        self.header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36'
        }
        self.client = pymongo.MongoClient('localhost', 27017)
        self.xs_set = self.client.xs_db.xs_set

    # 获取章节的url
    def section_url(self):
        response = requests.get(self.url, headers=self.header)
        response.encoding = response.apparent_encoding
        soup = BeautifulSoup(response.text, 'lxml')
        div = soup.select('.box_con')[1]
        section = div.select('dd a')[11:21]
        for s in section:
            href = self.url[:-5] + s['href']
            yield href

    # 获取标题和内容并存入数据库
    def content(self):
        n = 1
        for href in self.section_url():
            resp = requests.get(href, headers=self.header)
            resp.encoding = resp.apparent_encoding
            soup1 = BeautifulSoup(resp.text, 'lxml')
            title = soup1.select('h1')[0].string
            con = soup1.select('#content')[0].get_text().strip()
            print('正在存入第%d章。。。' % n)
            self.xs_set.insert({title: con})
            print('第%d章存入成功！' % n)
            n += 1


if __name__ == '__main__':
    url = 'http://www.biqudu.com/0_65'
    xs = Xs(url)
    xs.content()
