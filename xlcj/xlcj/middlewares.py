# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
import time
from scrapy.http import HtmlResponse

class XlcjSpiderMiddleware(object):
    def process_request(self, request, spider):
        if spider.name == 'xl':
            spider.driver.get(request.url)
            spider.driver.implicitly_wait(10)
            return HtmlResponse(url=spider.driver.current_url,body=spider.driver.page_source,encoding='utf-8',request=request)