# -*- coding: utf-8 -*-

# 定义管道：定义项目后期处理
# @author: Trunks(GaoMing)
# @Date:2016-10-18

from scrapy import signals
import json
import codecs
from twisted.enterprise import adbapi
from datetime import datetime
from hashlib import md5
import MySQLdb
import MySQLdb.cursors

# 过滤 json 格式，返回一个json 文件
class JsonWriterCarPipeline(object):
    def __init__(self):
       self.file = open('car.json', 'wb' )

    def process_item(self, item, spider):
        rep_item = item
        line = json.dumps(dict(rep_item)).replace('\n', '')
        self.file.write(line.replace(' ', '') + "\n")
        return item

class JsonWriterHousePipeline(object):
    def __init__(self):
       self.file = open('house.json', 'wb' )

    def process_item(self, item, spider):
        rep_item = item
        line = json.dumps(dict(rep_item)).replace('\n', '')
        self.file.write(line.replace(' ', '') + "\n")
        return item

class JsonWriterAtuoPipeline(object):
    def __init__(self):
       self.file = open('auto.json', 'wb' )

    def process_item(self, item, spider):
        rep_item = item
        line = json.dumps(dict(rep_item)).replace('\n', '')
        self.file.write(line.replace(' ', '') + "\n")
        return item

class JsonWriterAuto2Pipeline(object):
    def __init__(self):
       self.file = open('auto2.json', 'wb' )

    def process_item(self, item, spider):
        rep_item = item
        line = json.dumps(dict(rep_item)).replace('\n', '')
        self.file.write(line.replace(' ', '') + "\n")
        return item

class JsonWriterAuto3Pipeline(object):
    def __init__(self):
       self.file = open('auto3.json', 'wb' )

    def process_item(self, item, spider):
        rep_item = item
        line = json.dumps(dict(rep_item)).replace('\n', '')
        self.file.write(line.replace(' ', '') + "\n")
        return item

class PretreatmentPipeline(object):
    def process_item(self, item, spider):
        return item


class MysqldbPipeline(object):

    def __init__(self):
        # 打开数据库连接
        self.conn = MySQLdb.connect(host="localhost",user="root",passwd="root",db="analysislts",charset="utf8")
        self.cursor = self.conn.cursor()
        # 清空表
        # self.cursor.execute('truncate table spider_car_data;')
        # self.conn.commit()

    def process_item(self, item, spider):
       # now = datetime.utcnow().replace(microsecond=0).isoformat(' ')
        now = datetime.now().replace(microsecond=0).isoformat(' ')
        #self.cursor.execute("INSERT INTO spider_car_data (name) VALUES (1)")
        name = item['title']
        price1 = item['price'][0].replace('\n', '').replace(' ', '')
        price2 = item['price'][1].replace('\n', '').replace(' ', '')
        price3 = 1
        desc = item['info'][0]
        content = item['info'][1]
        self.cursor.execute("""
        		insert IGNORE into spider_car_data(name, price1, price2, price3, describes, content, datetime)
        		values(%s, %s, %s, %s, %s, %s, %s)
        	    """, (name,price1 , price2 , price3 , desc, content , now))
        self.conn.commit()
        return item

class MysqldblianjiaPipeline(object):

    def __init__(self):
        # 打开数据库连接
        self.conn = MySQLdb.connect(host="localhost",user="root",passwd="root",db="analysislts",charset="utf8")
        self.cursor = self.conn.cursor()
        # 清空表
        self.cursor.execute('truncate table spider_lianjia_data;')
        self.conn.commit()

    def process_item(self, item, spider):
        now = datetime.now().replace(microsecond=0).isoformat(' ')
        name = item['gms_title']
        price1 = item['gms_price'][0]
        price2 = item['gms_price'][1]
        self.cursor.execute("""
        		insert IGNORE into spider_lianjia_data(name,price1,price2,datetime)
        		values(%s, %s, %s, %s)
        	    """, (name,price1,price2,now))
        self.conn.commit()
        return item

class MysqldbautoPipeline(object):
    def __init__(self):
        # 打开数据库连接
        self.conn = MySQLdb.connect(host="localhost",user="root",passwd="root",db="analysislts",charset="utf8")
        self.cursor = self.conn.cursor()
        # 清空表
        self.cursor.execute('truncate table spider_autohome_brand;')
        self.conn.commit()

    def process_item(self, item, spider):
        now = datetime.now().replace(microsecond=0).isoformat(' ')
        str_count = len(item['t1'])
        i = 0
        src = ''
        while i < str_count:
            src = item['t2'][i]
            name = item['t1'][i]
            self.cursor.execute("""
            		insert IGNORE into spider_autohome_brand(name,src,datetime)
            		values(%s, %s, %s)
            	    """, (name, src, now))
            self.conn.commit()
            i += 1
        return item

# 厂商数据 #
class MysqldbautofirmsPipeline(object):
    def __init__(self):
        # 打开数据库连接
        self.conn = MySQLdb.connect(host="localhost",user="root",passwd="root",db="analysislts",charset="utf8")
        self.cursor = self.conn.cursor()
        # 清空表
        self.cursor.execute('truncate table spider_autohome_firms;')
        self.conn.commit()

    def process_item(self, item, spider):
        now = datetime.now().replace(microsecond=0).isoformat(' ')
        str_count = len(item['t2'])
        i = 0
        print "gaoming:::::::::::"
        print "bid::::::::::::::"
        filter = unicode("进入旗舰店", "UTF-8")
        while i < str_count:
            name = item['t2'][i]
            type = item['t1']
            # 标签过滤
            src = item['t3'][i].replace("999999", "210100")
            print filter,name,":::::::::::"
            if name != filter :
                variable = [item['t1']]
                sql = "select id from spider_autohome_brand  where name = %s "
                count = self.cursor.execute(sql, variable)
                bid = self.cursor.fetchall()
                self.conn.commit()
                self.cursor.execute("""
                        insert IGNORE into spider_autohome_firms(bid,name,type,src,datetime)
                        values(%s, %s, %s, %s, %s)
                        """, (bid, name, type, src,now))
                self.conn.commit()
            i += 1
        return item

# 车系数据 #
class MysqldbautovehiclesPipeline(object):
    def __init__(self):
        # 打开数据库连接
        self.conn = MySQLdb.connect(host="localhost", user="root", passwd="root", db="analysislts", charset="utf8")
        self.cursor = self.conn.cursor()
        # 清空表
        self.cursor.execute('truncate table spider_autohome_vehicles;')
        self.conn.commit()

    def process_item(self, item, spider):
        now = datetime.now().replace(microsecond=0).isoformat(' ')
        str_count = len(item['t2'])
        i = 0
        print "gaoming:::::::::::"
        print "bid::::::::::::::"
        #filter = unicode("进入旗舰店", "UTF-8")
        while i < str_count:
            name = item['t2'][i]
            src = item['t1']
            variable = [item['t1']]
            sql = "select id from spider_autohome_firms where name = %s "
            count = self.cursor.execute(sql, variable)
            fid = self.cursor.fetchall()
            self.conn.commit()
            self.cursor.execute("""
                    insert IGNORE into spider_autohome_vehicles(fid,name,src,datetime)
                    values(%s, %s, %s, %s)
                    """, (fid, name, src, now))
            self.conn.commit()
            i += 1
        return item
