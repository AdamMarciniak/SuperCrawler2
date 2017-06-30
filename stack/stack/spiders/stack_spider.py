from scrapy import Spider
from scrapy.selector import Selector

from stack.items import StackItem


with open(r'C:\Users\amarciniak\AppData\Local\Programs\Python\Python35-32\Scripts\stack\stack\spiders\links.txt') as f:
    linkList = f.read().splitlines()
    



class StackSpider(Spider):
    name = "stack"
    allowed_domains = ["realcanadiansuperstore.ca"]
    start_urls = linkList

    def parse(self, response):
        
        name = Selector(response)
        calories = Selector(response)

        
        item = StackItem()
        item['ItemName'] = name.xpath('//h1/text()').extract()[1].strip(';\n\t ')
        itemTempCal =calories.xpath('//*[@id="nutrition"]/div/div[1]/div/div[1]/div[4]/span[2]/text()').extract()
        item['Length']= len(itemTempCal)
        tempLength = len(itemTempCal)


        item['Calories'] = ('').join(itemTempCal).strip(';\n\t ')
            
        
        
        yield item



