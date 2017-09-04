# -*- coding: utf-8 -*-
import json
import os

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class SaveJson(object):
    def open_spider(self, spider):
        savedir = 'data'
        if not os.path.isdir(savedir):
            os.mkdir(savedir)
    
    def process_item(self, item, spider):
        firm_dict = dict(item)
        firm_dict.pop('firm_id')
        
        with open('data/{}.json'.format(item['firm_id']), 'w', encoding='utf-8') as outfile:
            json.dump(firm_dict, outfile, ensure_ascii=False, indent=4)

        return item
