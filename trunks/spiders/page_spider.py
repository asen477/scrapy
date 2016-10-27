# -*- coding:utf-8 -*-
import scrapy
from trunks.items import PageItem
class PageSpider(scrapy.Spider):
  # 定义爬虫的名称，主要main方法使用
  name = 'page'
  allowed_domains = ["douban.com"]
  start_urls = [
    "http://movie.douban.com/top250/"
  ]
  # 解析数据
  def parse(self, response):
    items = []
    for info in response.xpath('//div[@class="item"]'):
      item = PageItem()
      item['rank'] = info.xpath('div[@class="pic"]/em/text()').extract()
      item['title'] = info.xpath('div[@class="pic"]/a/img/@alt').extract()
      item['link'] = info.xpath('div[@class="pic"]/a/@href').extract()
      item['rate'] = info.xpath('div[@class="info"]/div[@class="bd"]/div[@class="star"]/span/text()').extract()
      item['quote'] = info.xpath('div[@class="info"]/div[@class="bd"]/p[@class="quote"]/span/text()').extract()
      items.append(item)
      yield item
    # 翻页
    next_page = response.xpath('//span[@class="next"]/a/@href')
    if next_page:
      url = response.urljoin(next_page[0].extract())
      #爬每一页
      yield scrapy.Request(url, self.parse)