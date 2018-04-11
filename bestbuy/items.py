# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BestbuyItem(scrapy.Item):
    # define the fields for your item here like:

    name=scrapy.Field()
    regularPrice = scrapy.Field()
    salePrice = scrapy.Field()
    customerRating = scrapy.Field()
    customerRatingCount = scrapy.Field()
    customerReviewCount = scrapy.Field()
    isOnlineOnly = scrapy.Field()
    isInStoreOnly = scrapy.Field()
    seller = scrapy.Field()
    link = scrapy.Field()
    discripiton = scrapy.Field()
    saleEndDate = scrapy.Field()
    categoryName=scrapy.Field()
    photoLink=scrapy.Field()

    # def get_insert_sql(self):
    #     insert_sql = "insert into goods(name,categoryName,regularPrice,salePrice,customerRating,customerRatingCount,customerReviewCount,isOnlineOnly,isInStoreOnly,photo_link,seller,saleEndDate,discripition,link) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    #     params = (self.name, self.categoryName, self.regularPrice, self.salePrice, self.customerRating, self.customerRatingCount, self.customerReviewCount,
    #               self.isOnlineOnly, self.isInStoreOnly, self.photoLink, self.seller, self.saleEndDate, self.discripition, self.link )
    #     return insert_sql, params
    def get_insert_sql(self):
        insert_sql = """
                INSERT INTO goods(name,categoryName,regularPrice,salePrice,customerRating,customerRatingCount,customerReviewCount,isOnlineOnly,isInStoreOnly,photo_link,seller,saleEndDate,discripition,link)
                VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s, %s,%s,%s, %s,%s)
                     """
        params = (self.name, self.categoryName, self.regularPrice, self.salePrice, self.customerRating, self.customerRatingCount, self.customerReviewCount,
                  self.isOnlineOnly, self.isInStoreOnly, self.photoLink, self.seller,self.saleEndDate,self.discripition, self.link
                 )
        return insert_sql, params
