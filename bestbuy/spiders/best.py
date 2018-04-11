# -*- coding: utf-8 -*-
import scrapy
import json
from bestbuy.items import BestbuyItem
import time
class BestSpider(scrapy.Spider):
    name = 'best'
    allowed_domains = ['bestbuy.ca']
    start_urls = ['https://www.bestbuy.ca/api/v2/json/search?lang=en&include=facets,resources,relatedcategories,relatedqueries,promotions,redirects&query=&page=1&pageSize=32&sortBy=relevance&sortDir=desc&path=category%3ATV%20%26%20Home%20Theatre%3Bcurrentoffers0enrchstring%3AOn%20Sale',]
    search_url='https://www.bestbuy.ca/api/v2/json/search?lang=en&include=facets,resources,relatedcategories,relatedqueries,promotions,redirects&query=&page={0}&pageSize=32&sortBy=relevance&sortDir=desc&path=category%3ATV%20%26%20Home%20Theatre%3Bcurrentoffers0enrchstring%3AOn%20Sale'


    def parse(self,response):
        data_org = response.body.decode('utf-8')
        data = json.loads(data_org)
        Total_PAGE = data['totalPages']
        print(response.status)
        print('******************Total Page******************************')
        print(Total_PAGE)
        i=1
        # for i in range(Total_PAGE):
        # for i in range(1, 101):
        for i in range(1,int(Total_PAGE)+1):
            url=self.search_url.format((str(i)))
            yield scrapy.Request(url,callback=self.parse_item)


    def parse_item(self, response):
        data_org=response.body.decode('utf-8')
        data=json.loads(data_org)
        # Total_PAGE=data['totalPages']
        goods_nums=len(data['products'])
        for i in range (goods_nums):
            items=BestbuyItem();
            items['name']=data['products'][i]['name']
            items['categoryName']=data['products'][i]['categoryName']
            items['regularPrice']=data['products'][i]['regularPrice']
            items['salePrice'] =data['products'][i]['salePrice']
            items['customerRating'] =data['products'][i]['customerRating']
            items['customerRatingCount'] =data['products'][i]['customerRatingCount']
            items['customerReviewCount'] =data['products'][i]['customerReviewCount']
            items['isOnlineOnly'] =data['products'][i]['isOnlineOnly']
            items['isInStoreOnly'] =data['products'][i]['isInStoreOnly']
            photo_link=data['products'][i]['highResImage']
            if photo_link=='https://multimedia.bbycastatic.ca/images/common/pictures/noimage1500x1500.jpg':
                items['photoLink'] = data['products'][i]['thumbnailImage']
            else:
                items['photoLink']=data['products'][i]['highResImage']
            seller = data['products'][i]['seller']
            if seller==None:
                items['seller'] ='BestBuy'
            else:
                items['seller'] =data['products'][i]['seller']['name']
            end_time=data['products'][i]['saleEndDate']
            if end_time==None:
                items['saleEndDate'] ="forever"
            else:
                ww = time.localtime(end_time/1000)
                dt = time.strftime("%Y-%m-%d-%H:%M:%S", ww)
                items['saleEndDate'] =dt
            # items['saleEndDate']=end_time
            items['discripiton']=data['products'][i]['shortDescription']
            items['link']='https://www.bestbuy.ca'+data['products'][i]['productUrl']
            yield items

