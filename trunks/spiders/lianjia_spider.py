#!/usr/bin/python
#coding=utf-8
'''
Created on 2016年10月20日
@author: Trunks(GaoMing)
'''
import scrapy
from trunks.items import LianjiaItem
from scrapy.spiders import CrawlSpider

class LianjiaSpider(CrawlSpider):
    # 自定义配置 加载个人管道
    custom_settings = {
        'ITEM_PIPELINES': {
            'trunks.pipelines.JsonWriterHousePipeline': 333,
            'trunks.pipelines.MysqldblianjiaPipeline': 500,
        }
    }
    name = "lianjia"
    allowed_domains = ["lianjia.com"]
    start_urls = [
        "http://sy.fang.lianjia.com/loupan/",
        "http://sy.fang.lianjia.com/loupan/pg2/",
        "http://sy.fang.lianjia.com/loupan/pg3/",
        "http://sy.fang.lianjia.com/loupan/pg4/",
        "http://sy.fang.lianjia.com/loupan/pg5/",
        "http://sy.fang.lianjia.com/loupan/pg6/",
        "http://sy.fang.lianjia.com/loupan/pg7/",
        "http://sy.fang.lianjia.com/loupan/pg8/",
        "http://sy.fang.lianjia.com/loupan/pg9/",
        "http://sy.fang.lianjia.com/loupan/pg10/",
        "http://sy.fang.lianjia.com/loupan/pg11/",
        "http://sy.fang.lianjia.com/loupan/pg12/",
        "http://sy.fang.lianjia.com/loupan/pg13/",
        "http://sy.fang.lianjia.com/loupan/pg14/",
        "http://sy.fang.lianjia.com/loupan/pg15/",
        "http://sy.fang.lianjia.com/loupan/pg16/",
        "http://sy.fang.lianjia.com/loupan/pg17/",
        "http://sy.fang.lianjia.com/loupan/pg18/",
        "http://sy.fang.lianjia.com/loupan/pg19/",
        "http://sy.fang.lianjia.com/loupan/pg20/",
        "http://sy.fang.lianjia.com/loupan/pg21/",
        "http://sy.fang.lianjia.com/loupan/pg22/",
        "http://sy.fang.lianjia.com/loupan/pg23/",
        "http://sy.fang.lianjia.com/loupan/pg24/",
        "http://sy.fang.lianjia.com/loupan/pg25/",
        "http://sy.fang.lianjia.com/loupan/pg26/",
        "http://sy.fang.lianjia.com/loupan/pg27/",
        "http://sy.fang.lianjia.com/loupan/pg28/",
        "http://sy.fang.lianjia.com/loupan/pg29/",
        "http://sy.fang.lianjia.com/loupan/pg30/",
        "http://sy.fang.lianjia.com/loupan/pg31/",
        "http://sy.fang.lianjia.com/loupan/pg32/",
        "http://sy.fang.lianjia.com/loupan/pg33/",
        "http://sy.fang.lianjia.com/loupan/pg34/",
        "http://sy.fang.lianjia.com/loupan/pg35/",
        "http://sy.fang.lianjia.com/loupan/pg36/",
        "http://sy.fang.lianjia.com/loupan/pg37/",
        "http://sy.fang.lianjia.com/loupan/pg38/",
        "http://sy.fang.lianjia.com/loupan/pg39/",
        "http://sy.fang.lianjia.com/loupan/pg40/",
        "http://sy.fang.lianjia.com/loupan/pg41/",
        "http://sy.fang.lianjia.com/loupan/pg42/",
        "http://sy.fang.lianjia.com/loupan/pg43/",
        "http://sy.fang.lianjia.com/loupan/pg44/",
        "http://sy.fang.lianjia.com/loupan/pg45/",
        "http://sy.fang.lianjia.com/loupan/pg46/",
        "http://sy.fang.lianjia.com/loupan/pg47/",
        "http://sy.fang.lianjia.com/loupan/pg48/",
        "http://sy.fang.lianjia.com/loupan/pg49/",
        "http://sy.fang.lianjia.com/loupan/pg50/",
        "http://sy.fang.lianjia.com/loupan/pg51/",
        "http://sy.fang.lianjia.com/loupan/pg52/",
        "http://sy.fang.lianjia.com/loupan/pg53/",
        "http://sy.fang.lianjia.com/loupan/pg54/",
        "http://sy.fang.lianjia.com/loupan/pg55/",
        "http://sy.fang.lianjia.com/loupan/pg56/",
        "http://sy.fang.lianjia.com/loupan/pg57/",
        "http://sy.fang.lianjia.com/loupan/pg58/",
         ]

    # 数据抓去部分
    def parse(self, response):
        for sel in response.xpath('//div[@class="info-panel"]'):
            item = LianjiaItem()
            # 楼盘名
            gms_scrapy_1 = sel.xpath('div/h2/a/text()').extract()
            # 楼盘信息
            gms_scrapy_2 = sel.xpath('div[@class="col-1"]/div/span/text()').extract()
            # 楼盘价格
            gms_scrapy_3 = sel.xpath('div/div/div/span/text()').extract()
            item['gms_title'] = gms_scrapy_1
            item['gms_info'] = gms_scrapy_2
            item['gms_price'] = gms_scrapy_3
            yield item

