# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TrunksItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class CarItem(scrapy.Item):
    title = scrapy.Field()
    price = scrapy.Field()
    info = scrapy.Field()

class LianjiaItem(scrapy.Item):
    gms_title = scrapy.Field()
    gms_info = scrapy.Field()
    gms_price = scrapy.Field()
    gms_city = scrapy.Field()

class AutoItem(scrapy.Item):
    t1 = scrapy.Field()
    t2 = scrapy.Field()
    t3 = scrapy.Field()

class Auto2Item(scrapy.Item):
    t1 = scrapy.Field()
    t2 = scrapy.Field()
    t3 = scrapy.Field()

class Auto3Item(scrapy.Item):
    t1 = scrapy.Field()
    t2 = scrapy.Field()
    t3 = scrapy.Field()

class RenrencheItem(scrapy.Item):
    t1 = scrapy.Field()
    t2 = scrapy.Field()
    t3 = scrapy.Field()

class PageItem(scrapy.Item):
    rank = scrapy.Field()
    title = scrapy.Field()
    link = scrapy.Field()
    rate = scrapy.Field()
    quote = scrapy.Field()
