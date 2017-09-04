# -*- coding: utf-8 -*-
import scrapy
from gis.items import Firm
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class FirmsSpider(CrawlSpider):
    name = 'firms'
    allowed_domains = ['2gis.ru']
    start_urls = ['https://2gis.ru/moscow/rubrics']

    rules = (
        Rule(LinkExtractor(allow=('/firm/')), callback='parse_item'),
        Rule(LinkExtractor(allow=('/subrubrics/'))),
        Rule(LinkExtractor(allow=('/rubricId/'))),
    )


    def parse_item(self, response):
        name = response.css('h1::text').extract_first()
        phones = response.css('bdo.contact__phonesItemLinkNumber::text').extract()[1:]
        
        address_tag = response.css('address')[0]
        address = ''.join(address_tag.css('a::text').extract())

        url_last_part = response.url.split('/')[-1]
        firm_id = url_last_part.split('?')[0]

        item = Firm()
        item['name'] = name
        item['phones'] = phones
        item['address'] = address
        item['firm_id'] = firm_id
        
        yield item

