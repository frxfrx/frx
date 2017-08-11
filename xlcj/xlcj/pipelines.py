# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class XlcjPipeline(object):
    def __init__(self,user1,host1,port1,password1,db1):
        self.user = user1
        self.host = host1
        self.port = port1
        self.password = password1
        self.db = db1

    def open_spider(self,spider):
        self.con = pymysql.connect(db=self.db,user=self.user,host=self.host,port=self.port,password=self.password,charset='utf8')
        self.cursor = self.con.cursor()
    #
    def close_spider(self,spider):
        self.con.close()

    @classmethod
    def from_crawler(cls,crawler):
        return cls(
            user1=crawler.settings.get('USER'),
            db1=crawler.settings.get('DB'),
            host1=crawler.settings.get('HOST'),
            port1=crawler.settings.get('PORT'),
            password1=crawler.settings.get('PASSWORD'),
        )

    def process_item(self, item, spider):
        sql = "insert into cj(plate,firm_num,avg_price,as_the_forehead,fall_or,total_volume,gross_turnover,led,fall_or1,now_price,as_the_forehead1)" \
              " values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"\
              %(item['plate'],
                item['firm_num'],
                item['avg_price'],
                item['as_the_forehead'],
                item['fall_or'],
                item['total_volume'],
                item['gross_turnover'],
                item['led'],
                item['fall_or1'],
                item['now_price'],
                item['as_the_forehead1']
                )
        self.cursor.execute(sql)
        self.con.commit()
        return item
