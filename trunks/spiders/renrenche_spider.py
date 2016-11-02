#!/usr/bin/python
#coding=utf-8
'''
Created on 2016年11月01日
@author: Trunks(GaoMing)
'''
import scrapy
from trunks.items import RenrencheItem
from scrapy.spiders import CrawlSpider

class RenrencheSpider(CrawlSpider):
    # 自定义配置 加载个人管道
    custom_settings = {
        'ITEM_PIPELINES': {
            'trunks.pipelines.JsonWriterrenrenchePipeline': 337,
            'trunks.pipelines.MysqldbrenrenchePipeline': 504,
        }
    }
    name = "renrenche"
    allowed_domains = ["renrenche.com"]
    # 计算分页数量
    i, j = 1, 79
    arr_list = []
    while i < j:
        arr_list += ["https://www.renrenche.com/sy/ershouche/p" + str(i)]
        i += 1
    start_urls = arr_list
    def parse(self, response):
        for sel in response.xpath('//li[@class="span6 list-item car-item"]'):
            item = RenrencheItem()
            gms_t1 = sel.xpath('a/@title').extract()
            gms_t2 = sel.xpath('a/div/div[@class="price"]/text()').extract()
            gms_t3 = sel.xpath('a/div/div[@class="new-price"]/span/text()').extract()
            # 人人车信息
            item['t1'] = gms_t1
            # 卖车价格
            item['t2'] = gms_t2
            # 新车价格
            item['t3'] = gms_t3
            yield item

