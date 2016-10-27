#!/usr/bin/python
#coding=utf-8
'''
Created on 2016年10月25日
@author: Trunks(GaoMing)
'''
import scrapy
from trunks.items import AutoItem
from scrapy.spiders import CrawlSpider

#class CarSpider(scrapy.spiders.Spider):
class AutoSpider(CrawlSpider):
    # 自定义配置 加载个人管道
    custom_settings = {
        'ITEM_PIPELINES': {
            'trunks.pipelines.JsonWriterAtuoPipeline': 334,
            'trunks.pipelines.MysqldbautoPipeline': 501,
        }
    }
    name = "auto"
    allowed_domains = ["autohome.com.cn"]
    start_urls = [
        "http://mall.autohome.com.cn/",
         ]

    def parse(self, response):
        for sel in response.xpath('//div[@class="nav-list-pop-main-half"]'):
            item = AutoItem()
            gms_t1 = sel.xpath('dl/dd/a/text()').extract()
            gms_t2 = sel.xpath('dl/dd/a/@href').extract()
            item['t1'] = gms_t1
            item['t2'] = gms_t2
            yield item

