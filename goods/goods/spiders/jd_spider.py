#!/usr/bin/python
#coding=utf-8
'''
Created on 2020年07月30日
@author: Trunks(GaoMing)
'''
import scrapy
from goods.items import JdItem
from scrapy.spiders import CrawlSpider

class JdSpider(CrawlSpider):
    # 自定义配置 加载个人管道
    custom_settings = {
        'ITEM_PIPELINES': {
            'goods.pipelines.GoodsPipeline': 300,
           # 'goods.pipelines.CrawlimagesPipeline': 400,
            'goods.pipelines.ImgPipeLine': 500,
            'goods.pipelines.DbJdPipeline': 600,
        }
    }
    offset = 0
    name = "jd"
    allowed_domains = ["jd.com"]
    # 分类
    # list_brand = ['华为','小米','小熊','美的','兰蔻','雅诗兰黛','米家','苏泊尔','荣耀','oppo','vivo']#
    list_brand = ['vivo']
    arr_list = []
    for item in list_brand:
        arr_list += ['https://search.jd.com/Search?keyword=' + item]
        # 计算分页数量
        if item == '小熊' or item == '美的':
            # 执行160记录，4页，一页30条
            i, j = 1, 4
            while i < j:
                arr_list += ['https://search.jd.com/Search?keyword=' + item + '&page=' + str(i)]
                i += 1
        else:
            i, j = 1, 2
            while i < j:
                arr_list += ['https://search.jd.com/Search?keyword=' + item + '&page=' + str(i)]
                i += 1
    # scrapy list
    print('项目列表：')
    print(arr_list)
    start_urls = arr_list
    url = 'https://search.jd.com/Search?keyword='

    # 数据抓去部分
    def parse(self, response):
        i = 0
        for sel in response.xpath('//div[@class="gl-i-wrap"]'):
            str_title = ''
            item = JdItem()
            # 商品标题
            gms_scrapy_1 = sel.xpath('div[@class="p-name p-name-type-3"]/a/em/text()').extract()
            if not gms_scrapy_1:
                gms_scrapy_1 = sel.xpath('div[@class="p-name p-name-type-2"]/a/em/text()').extract()
            for title in gms_scrapy_1:
                str_title = str_title + title
            # 商品价格
            gms_scrapy_2 = sel.xpath('div[@class="p-price"]/strong/i/text()').extract()
            # 商品信息sky
            gms_scrapy_3 = sel.xpath('div[@class="p-commit"]/strong/a/@href').extract()
            #
            gms_scrapy_4 = sel.xpath('div[@class="p-img"]/a/img/@src').extract()

            item['gms_title'] = str_title
            item['gms_price'] = gms_scrapy_2[0]
            item['gms_info'] = gms_scrapy_3
            item['gms_src'] = ['https:' + gms_scrapy_4[0]]
            item['gms_sku'] = ['https:' + gms_scrapy_3[0]]
            i += 1
            yield item
        # if self.offset < 1680:
        #     self.offset += 10
        # yield scrapy.Request(self.url + str(self.offset), callback=self.parse)