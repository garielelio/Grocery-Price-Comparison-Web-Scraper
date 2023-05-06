import scrapy
from scrapy_playwright.page import PageMethod
from webscrape.items import ZehrsItem
from scrapy.loader import ItemLoader

#Spider class for Zehrs
class ZehrsspiderSpider(scrapy.Spider):
    name = "zehrsspider"
    allowed_domains = ["zehrs.ca"]
    start_urls = ["http://zehrs.ca/"]

    #Request to open the webpage
    def start_requests(self):
        url = 'https://www.zehrs.ca/search?search-bar=fish' #MODIFY LATER FOR USER INPUT ========
        yield scrapy.Request(url, meta=dict(
            playwright = True,
            playwright_include_page = True,
            playwright_page_methods = [
                PageMethod('wait_for_selector', 'div.product-tile__details__info')
            ],
            errback = self.errback
        ))

    def parse(self, response):
        
        items = response.css('div.product-tile__details__info')

        # print(items)

        for item in items:
            
            brandName = item.css('span.product-name__item.product-name__item--brand::text').get()
            productName = item.css('span.product-name__item.product-name__item--name::text').get()

            if brandName is None:
                outputName = str(productName)
            else:
                outputName = str(brandName) + ", " + str(productName)

            print('Name: ' + str(outputName))
            print('Price: ' + str(item.css('span.price__value.selling-price-list__item__price.selling-price-list__item__price--now-price__value::text').get()))
            print('Price per: ' + str(item.css('span.price__value.comparison-price-list__item__price__value::text').get()))
            print('Weight: ' + str(item.css('span.price__unit.comparison-price-list__item__price__unit::text').get()))

            # visitPage = item.css('h3.text.text--small4.text--left.text--default-color.product-tile__details__info__name a::attr(href)').get()

            # pageUrl = 'https://www.zehrs.ca' + visitPage

            # print('********************')
            # print(pageUrl)

            # yield scrapy.Request(pageUrl, meta=dict(
            #     playwright = True,
            #     playwright_include_page = True,
            #     playwright_page_methods = [
            #         PageMethod('wait_for_selector', 'div.product-details-page-details__visibility-sensor')
            #     ],
            #     errback = self.errback,
            #     callback = self.parsePage
            # ))

    # def parsePage(self, response):
    #     brandName = response.css('span.product-name__item.product-name__item--brand::text')
    #     productName = response.css('h1.product-name__item.product-name__item--name::text')

    #     if brandName is None:
    #         outputName = productName
    #     else:
    #         outputName = brandName + ", " + productName

    #     print(outputName)
    #     print(response.css('span.price__value.selling-price-list__item__price.selling-price-list__item__price--now-price__value::text'))
    #     print(response.css('span.product-name__item.product-name__item--package-size::text'))
            

    async def errback(self, failure):
         page = failure.request.meta["playwright_page"]
         await page.close()
            
            
            
            
            
            
            
        # outputName = item.css('span.product-name__item product-name__item--brand::text') + ', ' + item.css('span.product-name__item product-name__item--name::text')

        # load = ItemLoader(item=ZehrsItem(), selector=item)

        # load.add_value('itemName', outputName)
        # load.add_css('itemPrice', 'span.price__value.selling-price-list__item__price.selling-price-list__item__price--now-price__value::text')
        # load.add_css()
