# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LeakedEmail(scrapy.Item):
    title = scrapy.Field()
    sender = scrapy.Field()
    receiver = scrapy.Field()
    content = scrapy.Field()
    time = scrapy.Field()