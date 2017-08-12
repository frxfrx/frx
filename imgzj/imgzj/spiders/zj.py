# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
from scrapy.http import Request

class ZjSpider(scrapy.Spider):
    name = "zj"
    allowed_domains = ["www.tupianzj.com"]
    start_urls = ['http://www.tupianzj.com']

    def parse(self, response):
        soup = BeautifulSoup(response.text,'lxml')
        ul = soup.find('ul',class_='fix')
        a = ul.find_all('a')
        for i in a:
            url = i.get('href')
            yield Request(url,callback=self.img)

    def img(self,response):
        img_soup = BeautifulSoup(response.text,'lxml')
        print(img_soup)