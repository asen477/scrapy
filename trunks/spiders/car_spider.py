#!/usr/bin/python
#coding=utf-8
'''
Created on 2016年10月19日
@author: Trunks(GaoMing)
'''
import scrapy
from trunks.items import CarItem
from scrapy.spiders import CrawlSpider

class CarSpider(CrawlSpider):
    # 自定义配置 加载个人管道
    custom_settings = {
        'ITEM_PIPELINES': {
            'trunks.pipelines.JsonWriterCarPipeline': 300,
            'trunks.pipelines.MysqldbPipeline': 200,
        }
    }
    name = "car"
    allowed_domains = ["guazi.com"]
    start_urls = [
        "http://www.guazi.com/sy/buy/",
        "http://www.guazi.com/sy/buy/o2/",
        "http://www.guazi.com/sy/buy/o3/",
        "http://www.guazi.com/sy/buy/o4/",
        "http://www.guazi.com/sy/buy/o5/",
        "http://www.guazi.com/sy/buy/o6/",
        "http://www.guazi.com/sy/buy/o7/",
        "http://www.guazi.com/sy/buy/o8/",
        "http://www.guazi.com/sy/buy/o9/",
        "http://www.guazi.com/sy/buy/o10/",
        "http://www.guazi.com/sy/buy/o11/",
        "http://www.guazi.com/sy/buy/o12/",
        "http://www.guazi.com/sy/buy/o13/",
        "http://www.guazi.com/sy/buy/o14/",
        "http://www.guazi.com/sy/buy/o15/",
        "http://www.guazi.com/sy/buy/o16/",
        "http://www.guazi.com/sy/buy/o17/",
        "http://www.guazi.com/sy/buy/o18/",
        "http://www.guazi.com/sy/buy/o19/",
        "http://www.guazi.com/sy/buy/o20/",
        "http://www.guazi.com/sy/buy/o21/",
        "http://www.guazi.com/sy/buy/o22/",
        "http://www.guazi.com/sy/buy/o23/",
        "http://www.guazi.com/sy/buy/o24/",
        "http://www.guazi.com/sy/buy/o25/",
        "http://www.guazi.com/sy/buy/o26/",
        "http://www.guazi.com/sy/buy/o27/",
        "http://www.guazi.com/sy/buy/o28/",
        "http://www.guazi.com/sy/buy/o29/",
        "http://www.guazi.com/sy/buy/o30/",
        "http://www.guazi.com/sy/buy/o31/",
        "http://www.guazi.com/sy/buy/o32/",
        "http://www.guazi.com/sy/buy/o33/",
        "http://www.guazi.com/sy/buy/o34/",
        "http://www.guazi.com/sy/buy/o35/",
        "http://www.guazi.com/sy/buy/o36/",
        "http://www.guazi.com/sy/buy/o37/",
        "http://www.guazi.com/sy/buy/o38/",
        "http://www.guazi.com/sy/buy/o39/",
        "http://www.guazi.com/sy/buy/o40/",
        "http://www.guazi.com/sy/buy/o41/",
        "http://www.guazi.com/sy/buy/o42/",
        "http://www.guazi.com/sy/buy/o43/",
        "http://www.guazi.com/sy/buy/o44/",
        "http://www.guazi.com/sy/buy/o45/",
        "http://www.guazi.com/sy/buy/o46/",
        "http://www.guazi.com/sy/buy/o47/",
        "http://www.guazi.com/sy/buy/o48/",
        "http://www.guazi.com/sy/buy/o49/",
        "http://www.guazi.com/sy/buy/o50/",
         ]

    # 数据抓去部分
    def parse(self, response):
        # self.log('+++++++ A response from %s just arrived!+++++' % response.url)
        items = []
        for sel in response.xpath('//div[@class="list-infoBox"]'):
            item = CarItem()
            gms_fc_gray = sel.xpath('p[@class="fc-gray"]/span/text()').extract()
            # 卖价
            gms_priType_1 = sel.xpath('p[@class="priType-s"]/span/i/text()').extract()
            # 原价
            gms_priType_3 = sel.xpath('p[@class="priType-s"]/s/text()').extract()
            # 降价
            gms_priType_2 = sel.xpath('p[@class="priType-s"]/span/text()').extract()
            gms_link = sel.xpath('a/@href').extract()
            gms_title = sel.xpath('a/@title').extract()
            gms_img = sel.xpath('a/img/@src').extract()
            item['price'] = gms_priType_3 + gms_priType_1 + gms_priType_2
            item['title'] = gms_title
            item['info'] = gms_link + gms_img
            yield item