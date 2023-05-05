import scrapy

#Spider class for Longgos
class LongosspiderSpider(scrapy.Spider):
    name = "longosspider"
    allowed_domains = ["longos.com"]
    start_urls = ["http://longos.com/"]

    #Request to open the webpage
    def start_requests(self):
        url = 'https://www.longos.com/search/fish?q=fish'
        yield scrapy.Request(url, meta={'playwright': True})

    #Parsing the webpage
    def parse(self, response):

        #Getting the content
        items = response.css('div.d-flex.flex-column.flex-grow-1.card-xs-right')

        #For loop to get and return the items
        for item in items:
            outputPrice = item.css('strong.price::text').get() + "." + item.css('sup.cents::text').get()
            outputWeight = item.css('span.unit::text').get()
            outputWeight = outputWeight.replace('/', '')

            yield{
                'itemName': item.css('div.d-flex.flex-column.flex-grow-1.card-xs-right div a h5.card-title.mb-0::text').get(),
                'itemPrice': outputPrice.strip(),
                'itemWeight': outputWeight.strip()
            }
