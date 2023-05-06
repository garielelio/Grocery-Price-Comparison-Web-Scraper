import scrapy
from webscrape.items import LongosItem
from scrapy.loader import ItemLoader


#Spider class for Longos
class LongosspiderSpider(scrapy.Spider):
    name = "longosspider"
    allowed_domains = ["longos.com"]
    start_urls = ["http://longos.com/"]

    #Request to open the webpage
    def start_requests(self):
        url = 'https://www.longos.com/search/fish?q=fish' #MODIFY LATER FOR USER INPUT ========
        yield scrapy.Request(url, meta={'playwright': True})

    #Parsing the webpage
    def parse(self, response):

        #Getting the content
        items = response.css('div.d-flex.flex-column.flex-grow-1.card-xs-right')

        #For loop to get and return the items
        for item in items:

            outputPrice = item.css('strong.price::text').get() + "." + item.css('sup.cents::text').get()
            outputWeight = item.css('span.unit::text').get()

            load = ItemLoader(item=LongosItem(), selector=item)

            load.add_css('itemName', 'div.d-flex.flex-column.flex-grow-1.card-xs-right div a h5.card-title.mb-0::text')
            load.add_value('itemPrice', outputPrice)
            load.add_value('itemWeight', outputWeight)
            load.add_value('storeName', 'Longos')

            yield load.load_item()
