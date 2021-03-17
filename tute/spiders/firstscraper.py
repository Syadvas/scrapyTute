import scrapy
from scrapy import Request
import json


class FirstscraperSpider(scrapy.Spider):
    name = 'firstscraper'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url,callback=self.parse,dont_filter=True)
    
    def parse(self, response):
        title  = response.xpath('//h3/a/@title').extract()
        title = {'title':title}
        print('**********************************')
        print(title)
        with open('titles.json','w') as fl:
            json.dump(title,fl)
        pass

    def parse2(self, response):
        pass
