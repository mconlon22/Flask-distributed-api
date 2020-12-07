import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        baseUrl='https://nominatim.openstreetmap.org/search?q='
        endURL='&format=json&polygon=1&addressdetails=1'
        address='22 +Fosterbrook+ blackrock +dublin'
        yield scrapy.Request(url=baseUrl+address+endURL,  callback=self.parse)

    def parse(self, response):
        print(response)
        page = response.url.split("/")[-2]
        filename = f'quotes-{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')