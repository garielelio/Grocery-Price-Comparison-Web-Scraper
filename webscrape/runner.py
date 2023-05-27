from webscrape.spiders.longosspider import LongosspiderSpider
from webscrape.spiders.nofrillsspider import NofrillsspiderSpider
from webscrape.spiders.zehrsspider import ZehrsspiderSpider
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
import sqlite3
import os

def run():
    settings = get_project_settings()
    process = CrawlerProcess(settings)
    process.crawl(NofrillsspiderSpider, domain='chicken')
    process.crawl(ZehrsspiderSpider, domain='chicken')
    process.crawl(LongosspiderSpider, domain='chicken')
    process.start()

def createDatabase():
    if not os.path.exists('database'):
            os.makedirs('database')

    #Connecting to the database
    connect = sqlite3.connect('database/data.db')
    curs = connect.cursor()

    curs.execute("DROP TABLE IF EXISTS Result")

    curs.execute("""CREATE TABLE IF NOT EXISTS Result(
                            ID_NUM  INTEGER  PRIMARY KEY  AUTOINCREMENT  NOT NULL,
                            NAME    TEXT,
                            PRICE   DECIMAL(6,2),
                            WEIGHT  TEXT,
                            STORE   TEXT)""")
    
    connect.commit()
    connect.close()

if __name__ == '__main__':
    createDatabase()
    run()