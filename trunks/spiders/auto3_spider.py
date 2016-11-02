#!/usr/bin/python
#coding=utf-8
'''
Created on 2016年10月26日
@author: Trunks(GaoMing)
'''
import scrapy
import MySQLdb
from trunks.items import Auto3Item
from scrapy.spiders import CrawlSpider

class Auto3Spider(CrawlSpider):
    # 自定义配置 加载个人管道
    custom_settings = {
        'ITEM_PIPELINES': {
            'trunks.pipelines.JsonWriterAuto3Pipeline': 336,
            'trunks.pipelines.MysqldbautovehiclesPipeline': 503,
        }
    }
    name = "auto3"
    allowed_domains = ["autohome.com.cn"]
    conn = MySQLdb.connect(host="localhost", user="root", passwd="root", db="analysis", charset="utf8")
    cursor = conn.cursor()
    sql = "select title from spider_autohome_firms "
    count = cursor.execute(sql)
    results = cursor.fetchall()
    arr_list = []
    for row in results:
        arr_list += ['http://mall.autohome.com.cn' + row[0]]
    cursor.close()
    conn.commit()
    conn.close()
    start_urls = arr_list

    def parse(self, response):
        for sel in response.xpath('//div[@class="filter-pop fn-hide"]'):
            item = Auto3Item()
            #gms_t1 = sel.xpath('dl[@class="fn-clear"]/dd/a/text()').extract()  # brand ID
            gms_t1 = sel.xpath('dl/dt/a/text()').extract()  # brand ID
            gms_t2 = sel.xpath('dl/dd/a/text()').extract()  # brand ID
            item['t1'] = gms_t1
            item['t2'] = gms_t2
            yield item