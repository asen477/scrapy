#!/usr/bin/python
#coding=utf-8
'''
Created on 2016年10月26日
@author: Trunks(GaoMing)
'''
import scrapy
import MySQLdb
from trunks.items import Auto2Item
from scrapy.spiders import CrawlSpider

class Auto2Spider(CrawlSpider):
    # 自定义配置 加载个人管道
    custom_settings = {
        'ITEM_PIPELINES': {
            'trunks.pipelines.JsonWriterAuto2Pipeline': 335,
            'trunks.pipelines.MysqldbautofirmsPipeline': 502,
        }
    }
    name = "auto2"
    allowed_domains = ["autohome.com.cn"]
    conn = MySQLdb.connect(host="localhost", user="root", passwd="root", db="analysis", charset="utf8")
    cursor = conn.cursor()
    sql = "select title from spider_autohome_brand"
    count = cursor.execute(sql)
    results = cursor.fetchall()
    arr_list = []
    for row in results:
        arr_list += ['http:' + row[0]]
    cursor.close()
    conn.commit()
    conn.close()
    start_urls = arr_list
    # print("::::::::::",start_urls,"::::::::::::::::")
    def parse(self, response):
        for sel in response.xpath('//li[@class="tab-content-item current"]'):
            item = Auto2Item()
            gms_t1 = sel.xpath('div/dl[@class="fn-clear filter-brand"]/dd/a/text()').extract()  # brand ID
            gms_t2 = sel.xpath('div/dl/dt/a/text()').extract()
            gms_t3 = sel.xpath('div/dl/dt/a/@href').extract()  # brand ID
            item['t1'] = gms_t1[1]
            item['t2'] = gms_t2
            item['t3'] = gms_t3
            yield item




