#coding=utf-8
'''
Created on 2020年07月30日
@author: Trunks(GaoMing)
'''

import os
import requests
import MySQLdb
import MySQLdb.cursors
import time
from goods.settings import IMAGES_STORE
from scrapy.pipelines.images import ImagesPipeline
from scrapy import Request
from datetime import datetime
import json
import numpy as np

class GoodsPipeline(object): #需要在setting.py里设置'coolscrapy.piplines.CoolscrapyPipeline':300

    def __init__(self):
       self.file = open('news.json', 'wb')

    def process_item(self, item, spider):
        # 获取当前工作目录
        base_dir = os.getcwd()
        fiename = base_dir + '/news.txt'
        #从内存以追加的方式打开文件，并写入对应的数据
        with open(fiename, 'a',encoding="utf-8") as f:
            f.write(item['gms_title'] + '\n')
            f.write(item['gms_price'] + '\n')
        return item


class CrawlImagesPipeline(object):

    def process_item(self, item, spider):
        fold_name = "".join(item['gms_src'])
        header = {
            'USER-Agent': 'User-Agent:Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
            'Cookie': 'b963ef2d97e050aaf90fd5fab8e78633',
            #需要查看图片的cookie信息，否则下载的图片无法查看
        }
        images = []
        # 所有图片放在一个文件夹下
        dir_path = '{}'.format(IMAGES_STORE)
        if not os.path.exists(dir_path) and len(item['gms_src']) != 0:
            os.mkdir(dir_path)
        if len(item['gms_src']) == 0:
            with open('..//check.txt', 'a+') as fp:
                fp.write("".join(item['gms_title']) + ":" + "".join(item['gms_src']))
                fp.write("\n")

        for jpg_url, name, num in zip(item['gms_src'], item['gms_title'],range(0,100)):
            file_name = name + str(num)
            file_path = '{}//{}'.format(dir_path, file_name)
            images.append(file_path)
            if os.path.exists(file_path) or os.path.exists(file_name):
                continue

            with open('{}//{}.jpg'.format(dir_path, file_name), 'wb') as f:
                req = requests.get(jpg_url, headers=header)
                f.write(req.content)
        return item



# class ImgPipeLine(ImagesPipeline):
#     def get_media_requests(self, item, info):
#         for image_url in item['gms_src']:
#             yield Request(image_url)

# 下载图片地址，存储本地
class ImgPipeLine(ImagesPipeline):
    def get_media_requests(self, item, info):
        # 循环每一张图片地址下载，若传过来的不是集合则无需循环直接yield
        for image_url in item['gms_src']:
            # meta里面的数据从spider获取，然后通过meta传递给下面的方法 file_path
            yield Request(image_url, meta={'name':item['gms_title']})

    # 重命名，如果不重写该函数，图片名为哈希
    def file_path(self, request, response=None, info=None):
        # 提取url中的图片名称
        image_guid = request.url.split("/")[-1]
        # 接收meta传递过来的文件夹名称
        name = request.meta['name']
        # 过滤windows字符串，不经过这么一个步骤，你会发现有乱码导致无法下载
        #name = re.sub(r'[?\\*|"<>:/]', '', name)
        name = time.strftime('%Y-%m-%d', time.localtime())
        # 分文件存储的关键：{0} 对应name; {1}对应image_guid
        filename = u'{0}/{1}/{2}'.format('list',name, image_guid)
        return filename


class DbJdPipeline(object):
    def __init__(self):
        # 打开数据库连接
        self.conn = MySQLdb.connect(host="127.0.0.1",user="root",passwd="root",db="analysis",charset="utf8")
        self.cursor = self.conn.cursor()
        # 清空表
        #self.cursor.execute('truncate table spider_jd_data;')
        #self.conn.commit()

    def process_item(self, item, spider):
        now = datetime.now().replace(microsecond=0).isoformat(' ')
        name = item['gms_title'].replace('\n', '').replace(' ', '')
        image = item['gms_src'][0].replace('\n', '').replace(' ', '')
        price = item['gms_price']
        url = item['gms_sku'][0]
        self.cursor.execute("""
        		insert IGNORE into spider_jd_data(name,image,url,price,datetime)
        		values(%s, %s, %s, %s, %s)
        	    """, (name,image, url,price,now))
        # 插入的ID
        # goods_id = self.conn.insert_id()
        self.conn.commit()
        return item



# 下载图片地址，存储本地
class ImgViewPipeLine(ImagesPipeline):
    def get_media_requests(self, item, info):
        # 循环每一张图片地址下载，若传过来的不是集合则无需循环直接yield
        for image_url in item['gms_src']:
            # meta里面的数据从spider获取，然后通过meta传递给下面的方法 file_path
            yield Request(image_url, meta={'name':item['gms_price']})


    # # 重命名，如果不重写该函数，图片名为哈希
    def file_path(self, request, response=None, info=None):
        # 提取url中的图片名称
        image_guid = request.url.split("/")[-1]
        # 接收meta传递过来的文件夹名称
        name = request.meta['name']
        # 过滤windows字符串，不经过这么一个步骤，你会发现有乱码导致无法下载
        #name = re.sub(r'[?\\*|"<>:/]', '', name)
        name = time.strftime('%Y-%m-%d', time.localtime())
        # 分文件存储的关键：{0} 对应name; {1}对应image_guid
        filename = u'{0}/{1}/{2}'.format('view',name, image_guid)
        return filename


class JdViewPipeline(object):

    def __init__(self):
        # 打开数据库连接
        self.conn = MySQLdb.connect(host="127.0.0.1",user="root",passwd="root",db="analysis",charset="utf8")
        self.cursor = self.conn.cursor()
        # 清空表
        # self.cursor.execute('truncate table spider_jd_data;')
        # self.conn.commit()

    def process_item(self, item, spider):
        now = datetime.now().replace(microsecond=0).isoformat(' ')
        name_value = ''
        for title in item['gms_title']:
            name_value += title.replace('\n', '').replace(' ', '')
        name = name_value
        # 图片信息
        http_img = 'https://www.trunksit.cn/goods/view/'
        # 首图
        image = http_img + item['gms_src'][0].rsplit("/",1)[1]
        # 图集
        # 新增图片域名
        images_list_arr = []
        for images_list in item['gms_src']:
            images_list_arr.append(http_img + images_list.rsplit("/",1)[1])
        gallery = json.dumps(images_list_arr)

        description = json.dumps(item['gms_info'], indent=2, ensure_ascii=False)

        # 所属品牌
        brand_id = 1
        # 所属商户id，0表示为平台自营
        seller_id = 0
        # 所属的商户分类ID
        seller_cate_id =3
        # 商品状态 0:下架 1:正常，-1:待审核 -2:管理员拒 -3 管理员下架(必须管理员恢复)
        status = -1
        # 最低价格、最高价格
        min_price = 1
        max_price = 100
        service_id = 0
        # 表示配送范围
        depot_id = 10
        freight_id = 10
        # 库存数量
        quantity = 100

        sale_count = 0
        sale_amount = 0
        buy_type = 1
        type = 'goods'
        coupon_type = 0
        coupon_expire_day =0
        coupon_begin_time = now
        coupon_end_time = now
        comment_score = 0
        comment_count = 0
        # 是否首页推荐商品 0 不是 1 是
        is_recommend = 0
        # 直到结算前都可以退款 0 不可以 1  可以
        refund_before_balance = 0
        view_count = 0
        sort = 0
        # 商品的类型归属，默认为shop表示商城商品，可以由不同的模块发布的商品表示商品来源，如score(积分商品),pintuan(拼团商品),supplier(供应商商品),flash_sale(限时抢购),seckill(秒杀),warehouse(商品库)等
        source = 'score'
        created_at = now
        created_date = time.strftime("%Y-%m-%d", time.localtime())
        created_month = time.strftime("%Y-%m-%d", time.localtime())
        created_year = time.strftime("%Y-%m-%d", time.localtime())
        updated_at = time.strftime("%Y-%m-%d", time.localtime())
        updated_date = time.strftime("%Y-%m-%d", time.localtime())
        updated_month = time.strftime("%Y-%m-%d", time.localtime())
        updated_year = time.strftime("%Y-%m-%d", time.localtime())
        supplier_goods_id = 0
        gift_quantity_limit = 0
        thirty_sales = 0
        price_coupon = 'null'
        # 插数据库
        self.cursor.execute("""
        		insert IGNORE into goods(name,brief,description,mobile_description,brand_id,seller_id,seller_cate_id,status,image,gallery,min_price,max_price,service_id,depot_id,freight_id,quantity,sale_count,sale_amount,buy_type,type,coupon_type,coupon_expire_day,coupon_begin_time,coupon_end_time,comment_score,comment_count,is_recommend,refund_before_balance,view_count,sort,source,created_at,created_date,created_month,created_year,updated_at,updated_date,updated_month,updated_year,supplier_goods_id,gift_quantity_limit,thirty_sales,price_coupon)
        		values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        	    """, (name,name,description,description,brand_id,seller_id,seller_cate_id,status,image,gallery,min_price,max_price,service_id,depot_id,freight_id,quantity,sale_count,sale_amount,buy_type,type,coupon_type,coupon_expire_day,coupon_begin_time,coupon_end_time,comment_score,comment_count,is_recommend,refund_before_balance,view_count,sort,source,created_at,created_date,created_month,created_year,updated_at,updated_date,updated_month,updated_year,supplier_goods_id,gift_quantity_limit,thirty_sales,price_coupon))
        goods_id = self.conn.insert_id()

        # 积分表
        score_goods_id = goods_id
        # 积分大分类ID
        score_goods_score_category_id = 1
        # 积分小分类ID
        score_goods_score_score_sub_category_id = 74
        # 用户单次限兑换个数
        score_goods_user_limit_per_time = 999
        # 最小积分
        min_score = 1
        # 最大积分
        max_score = 100
        # 最低积分所需的价格
        min_price = 1
        # 最大积分所需的价格
        max_price = 100
        self.cursor.execute("""
        		insert IGNORE into score_goods(goods_id, score_category_id, score_sub_category_id, user_limit_per_time, min_score, max_score, min_price, max_price)
        		values(%s, %s, %s, %s, %s, %s, %s, %s)
        	    """, (score_goods_id,score_goods_score_category_id, score_goods_score_score_sub_category_id,score_goods_user_limit_per_time,min_score,max_score,min_price,max_price))

        #score_goods
        self.conn.commit()
        return item