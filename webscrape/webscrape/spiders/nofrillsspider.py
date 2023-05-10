import scrapy
from scrapy_playwright.page import PageMethod
from webscrape.items import NofrillsItem
from scrapy.loader import ItemLoader

#Spider class for Nofrills
class NofrillsspiderSpider(scrapy.Spider):
    name = "nofrillsspider"
    custom_settings = {
        'ITEM_PIPELINES' : {
            'webscrape.pipelines.PipelineTwo' : 300,
        }
    }
    allowed_domains = ["nofrills.ca"]
    #start_urls = ["http://nofrills.ca/"]

    def __init__(self, domain, *args, **kwargs):
        super(NofrillsspiderSpider, self).__init__(*args, **kwargs)
        self.start_urls = [f'https://www.nofrills.ca/search?search-bar={domain}'] if domain else []

    #Request to open the page
    def start_requests(self):
        #url = 'https://www.nofrills.ca/search?search-bar=fish' #MODIFY LATER FOR USER INPUT ===========
        url = self.start_urls[0]

        #Wait for the page to load
        yield scrapy.Request(url, meta=dict(
            playwright = True,
            playwright_include_page = True,
            playwright_page_methods = [
                PageMethod('wait_for_selector', 'div.product-tile__details__info')
            ],
            errback = self.errback
        ))

    #Parsing the data
    def parse(self, response):
        items = response.css('div.product-tile__details__info')

        for item in items:
            brandName = item.css('span.product-name__item.product-name__item--brand::text').get()
            productName = item.css('span.product-name__item.product-name__item--name::text').get()

            if brandName is None:
                outputName = str(productName)
            else:
                outputName = str(brandName) + ", " + str(productName)

            #Putting the data
            load = ItemLoader(item = NofrillsItem(), selector=item)

            load.add_value('itemName', outputName)
            load.add_css('itemPrice', 'span.price__value.selling-price-list__item__price.selling-price-list__item__price--now-price__value::text')
            load.add_css('itemPricePerWeight', 'span.price__value.comparison-price-list__item__price__value::text')
            load.add_css('itemMeasurement', 'span.price__unit.comparison-price-list__item__price__unit::text')
            load.add_value('storeName','Nofrills')

            yield load.load_item()


    #Error response
    async def errback(self, failure):
        page = failure.request.meta["playwright_page"]
        await page.close()
