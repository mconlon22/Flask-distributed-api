import pandas as pd
import scrapy
import json
import time
from scraper_api import ScraperAPIClient


class QuotesSpider(scrapy.Spider):
    client = ScraperAPIClient('12e5579c431ab5190b3b5cade3a29380')
    result = client.get(url = 'http://httpbin.org/ip').text
    print(result);
    name = "quotes"
    locations=[]
    
    def start_requests(self):
        data = pd.read_csv("PPR-ALL.csv", engine='python') 
        addresses = data["Address"]
        for i in range(0,10):
            baseUrl='https://nominatim.openstreetmap.org/search?q='
            endURL='&format=json&polygon=1&addressdetails=1'
            address=addresses[i]
            time.sleep(1)
            yield scrapy.Request(url=baseUrl+address+endURL,  callback=self.parse, headers={"User-Agent": "My UserAgent"}, 
                        meta={"proxy": "http://178.165.44.122:1080"} )

    def parse(self, response):

         jsonresponse = json.loads(response.text)[0]
         location=[jsonresponse["lat"]   ,jsonresponse["lon"] ]     
         print(location)
         locations.append(location)
    print(locations)