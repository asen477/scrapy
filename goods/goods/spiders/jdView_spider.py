#!/usr/bin/python
#coding=utf-8
'''
Created on 2020年08月01日
@author: Trunks(GaoMing)
'''
import scrapy
from goods.items import JdViewItem
from scrapy.spiders import CrawlSpider
import MySQLdb
import MySQLdb.cursors
import json
from datetime import datetime
import json
#import numpy as np

class JdViewSpider(CrawlSpider):
    # 自定义配置 加载个人管道
    custom_settings = {
        'ITEM_PIPELINES': {
            #'goods.pipelines.ImgViewPipeLine': 700,
            #'goods.pipelines.JdViewPipeline': 800,
        }
    }
    offset = 0
    name = "jd_view"
    allowed_domains = ["jd.com"]
    # 查询所有数据结果
    # 打开数据库连接
    conn = MySQLdb.connect(host="127.0.0.1",user="root",passwd="root",db="analysis",charset="utf8")
    cursor = conn.cursor()
    cursor.execute("select url from spider_jd_data ")
    row = cursor.fetchall()
    arr_list = []
    for i in range(len(row)):
        for j in range(len(row[i])):
            #print("row[%d][%d]"%(i,j))
            arr_list += [row[i][j].replace('#comment', '')]
    # scrapy list
    print(arr_list)
    start_urls = arr_list

    # 数据抓去部分
    def parse(self, response):
        for sel in response.xpath('//div[@class="p-parameter"]'):
            item = JdViewItem()
            # 商品信息
            # 过滤掉json信息
            lst = sel.xpath('ul[@class="parameter2 p-parameter-list"]/li/text()').extract()
            # keys = [str(x) for x in np.arange(len(lst))]
            # list_json = dict(zip(keys, lst))
            # str_json = json.dumps(list_json, indent=2, ensure_ascii=False)  # json转为string
            item['gms_info'] = lst
            for sel2 in response.xpath('//div[@class="spec-list"]'):
                # 图片集合
                images = sel2.xpath('div[@class="spec-items"]/ul/li/img/@data-url').extract()
                images_list = []
                # 新增图片域名
                for img in images:
                    images_list.append('https://img10.360buyimg.com/n1/' + img)
                item['gms_src'] = images_list
            for sel3 in response.xpath('//div[@class="itemInfo-wrap"]'):
                # 标题
                item['gms_title'] = sel3.xpath('div[@class="sku-name"]/text()').extract()
            item['gms_price'] = 1
            yield item