# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
from twisted.enterprise import adbapi
import pymysql.cursors

class BestbuyPipeline(object):

    def __init__(self, dbpool):
        self.dbpool = dbpool
        # 从配置中获取信息

    @classmethod
    def from_settings(cls, settings):
        dbparms = dict(
            host=settings["MYSQL_HOST"],
            db=settings['MYSQL_DBNAME'],
            user=settings['MYSQL_USER'],
            passwd=settings['MYSQL_PASSWORD'],
            charset='utf8',
            cursorclass=pymysql.cursors.DictCursor,
            use_unicode=True
        )
        dbpool = adbapi.ConnectionPool("pymysql", **dbparms)
        return cls(dbpool)

    def process_item(self, items, spider):
        # 使用twisted将mysql插入编程异步执行
        # 第一个参数是我们定义的函数
        query = self.dbpool.runInteraction(self.do_insert, items)
        # 错误处理
        # query.addErrorback(self.handle_error)

    # 错误处理函数
    def handle_error(self, falure):
        print(falure)

    def do_insert(self, cursor, items):
        # 执行具体的插入
        name = items['name']
        categoryName = items['categoryName']
        regularPrice = items['regularPrice']
        salePrice = items['salePrice']
        customerRating = items['customerRating']
        customerRatingCount = items['customerRatingCount']
        customerReviewCount = items['customerReviewCount']
        isOnlineOnly = items['isOnlineOnly']
        isInStoreOnly = items['isInStoreOnly']
        photoLink = items['photoLink']
        seller = items['seller']
        saleEndDate = items['saleEndDate']
        discripition = items['discripiton']
        link = items['link']
        insert_sql = """
                       insert into goods(name,categoryName,regularPrice,salePrice,customerRating,customerRatingCount,customerReviewCount,isOnlineOnly,isInStoreOnly,photo_link,seller,saleEndDate,discripition,link)
                       VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                       """
        cursor.execute(insert_sql, (name,categoryName,regularPrice,salePrice,customerRating,customerRatingCount,customerReviewCount,isOnlineOnly,isInStoreOnly,photoLink,seller,saleEndDate,discripition,link))
