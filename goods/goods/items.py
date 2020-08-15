# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class GoodsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class JdItem(scrapy.Item):
    gms_title = scrapy.Field()
    gms_info = scrapy.Field()
    gms_price = scrapy.Field()
    gms_src = scrapy.Field()
    gms_sku = scrapy.Field()

class JdViewItem(scrapy.Item):
    gms_title = scrapy.Field()
    gms_info = scrapy.Field()
    gms_price = scrapy.Field()
    gms_src = scrapy.Field()
    gms_sku = scrapy.Field()