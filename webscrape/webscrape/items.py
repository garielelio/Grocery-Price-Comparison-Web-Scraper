# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import TakeFirst, MapCompose
from price_parser import Price

def currencyChange(inpt):
    price = Price.fromstring(inpt)
    return price.amount_float

def cleanWeight(inpt):
    return inpt.replace('/','').strip()


class WebscrapeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class LongosItem(scrapy.Item):
    itemName = scrapy.Field(output_processor = TakeFirst())
    itemPrice = scrapy.Field(input_processor = MapCompose(currencyChange), output_processor = TakeFirst())
    itemWeight = scrapy.Field(input_processor = MapCompose(cleanWeight), output_processor = TakeFirst())
    storeName = scrapy.Field(output_processor = TakeFirst())

class ZehrsItem(scrapy.Item):
    itemName = scrapy.Field()
    itemPrice = scrapy.Field()
    itemWeight = scrapy.Field()
    storeName = scrapy.Field()
