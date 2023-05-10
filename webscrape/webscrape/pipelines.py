# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3

class PipelineOne:

    def process_item(self, item, spider):

        #Connecting to the database
        connect = sqlite3.connect('database/data.db')

        curs = connect.cursor()

        curs.execute("""INSERT INTO Result 
                        VALUES (NULL, ?, ?, ?, ?)""",(item.get('itemName'), item.get('itemPrice'), item.get('itemWeight'), item.get('storeName')))
        
        connect.commit()
        #print("Pipeline one") === Testing pipeline 1
        return item
    
class PipelineTwo:
    def process_item(self, item, spider):
        connect = sqlite3.connect('database/data.db')

        curs = connect.cursor()

        weightToPut = None

        if item.get('itemMeasurement') == '100ml':
            calculateWeight = (item.get('itemPrice') / item.get('itemPricePerWeight')) * 100

            calculateWeight = round(calculateWeight)

            weightToPut = str(calculateWeight) + "ml"

        if item.get('itemMeasurement') == '100g':
            calculateWeight = (item.get('itemPrice') / item.get('itemPricePerWeight')) * 100

            calculateWeight = round(calculateWeight)

            weightToPut = str(calculateWeight) + "g"

        curs.execute("""INSERT INTO Result 
                        VALUES (NULL, ?, ?, ?, ?)""",(item.get('itemName'), item.get('itemPrice'), weightToPut, item.get('storeName')))

        connect.commit()
        #print("Pipeline two")
        return item
