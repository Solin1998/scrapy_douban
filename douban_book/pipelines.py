# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class DoubanBookPipeline(object):
    def process_item(self, item, spider):
        with open("db_top250_book.txt",'a',encoding='utf-8') as f:
            for i in item:
                f.write(item[i]+"\t")
            f.write('\n')

        return item