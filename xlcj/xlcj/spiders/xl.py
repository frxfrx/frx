# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver
from scrapy import signals
from scrapy.xlib.pydispatch import dispatcher
from xlcj.items import XlcjItem


class XlSpider(scrapy.Spider):
    name = 'xl'
    allowed_domains = ['vip.stock.finance.sina.com']
    start_urls = ['http://finance.sina.com.cn/stock/sl/#concept_1']

    def __init__(self):
        super(XlSpider, self).__init__()
        self.driver = webdriver.PhantomJS()
        dispatcher.connect(self.spider_closed, signals.spider_closed)

    def spider_closed(self, spider):
        self.driver.quit()

    def parse(self, response):
        table = response.css('#datatbl tbody tr')
        for t in table:
            td = t.css('td')
            plate = td[0].css('a::text').extract()[0]
            firm_num = td[1].css('::text').extract()[0]
            avg_price = td[2].css('span::text').extract()[0]
            as_the_forehead = td[3].css('span::text').extract()[0]
            fall_or = td[4].css('span::text').extract()[0]
            total_volume = td[5].css('::text').extract()[0]
            gross_turnover = td[6].css('::text').extract()[0]
            led = td[7].css('::text').extract()[0] + td[7].css('::text').extract()[1]
            fall_or1 = td[8].css('span::text').extract()[0]
            now_price = td[9].css('span::text').extract()[0]
            as_the_forehead1 = td[10].css('span::text').extract()[0]
            item = XlcjItem(plate=plate, firm_num=firm_num, avg_price=avg_price,
                            as_the_forehead=as_the_forehead,
                            fall_or=fall_or,
                            total_volume=total_volume,
                            gross_turnover=gross_turnover,
                            led=led,
                            fall_or1=fall_or1,
                            now_price=now_price,
                            as_the_forehead1=as_the_forehead1)
            yield item
