# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class XlcjItem(scrapy.Item):
    # define the fields for your item here like:
    plate = scrapy.Field()
    firm_num = scrapy.Field()
    avg_price = scrapy.Field()
    as_the_forehead = scrapy.Field()
    fall_or = scrapy.Field()
    total_volume = scrapy.Field()
    gross_turnover = scrapy.Field()
    led = scrapy.Field()
    fall_or1 = scrapy.Field()
    now_price = scrapy.Field()
    as_the_forehead1 = scrapy.Field()

