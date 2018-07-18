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
    # 城市分站
    list_city = ['sy','sh','bj','cd','cq','gz','cs','hz','jn','qd','nj','sz','ty','wh','su']
    arr_list = []
    for item in list_city:
        arr_list += ['https://' + item + '.fang.lianjia.com/loupan/']
        # 计算分页数量
        i, j = 1, 60
        while i < j:
            arr_list += ['https://' + item + '.fang.lianjia.com/loupan/'+str(i)]
            i += 1

    start_urls = arr_list

    # 数据抓去部分
    def parse(self, response):
        for sel in response.xpath('//div[@class="resblock-desc-wrapper"]'):
            item = LianjiaItem()
            # 楼盘名
            gms_scrapy_1 = sel.xpath('div/a/text()').extract()
            # 楼盘信息
            # gms_scrapy_2 = sel.xpath('div[@class="col-1"]/div/span/text()').extract()
            gms_scrapy_2 = sel.xpath('div[@class="resblock-price"]/div/span/text()').extract()
            # 楼盘价格
            gms_scrapy_3 = sel.xpath('div[@class="resblock-price"]/div/text()').extract()
            # 城市区域
            gms_scrapy_4 = sel.xpath('title/text()').extract()

            item['gms_title'] = gms_scrapy_1
            item['gms_info'] = gms_scrapy_2
            item['gms_price'] = gms_scrapy_3
            item['gms_city'] = response.url
            print(item)
            yield item

