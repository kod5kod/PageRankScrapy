import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader

from pagerankspider.items import FromToItem

# To import it :
from scrapy.exceptions import CloseSpider



class MySpider(scrapy.Spider):
    name = 'pagerank'

    def __init__(self, start=None, domain=None,maxpages=None, *args, **kwargs):
        super(MySpider, self).__init__(*args, **kwargs)
        if maxpages is None:
            self.N = 7000000
        else:
            self.N = int(maxpages)
        self.count = 0
        self.start_urls = []
        self.logger.info(start)
        if start is None:
            self.start_urls.append('https://github.com/')
        else:
            self.start_urls.append(start)
        self.logger.info(self.start_urls)
        self.allowed_domains = []
        if domain is not None:
            self.allowed_domains.append(domain)
        self.logger.info(self.allowed_domains)

    def start_requests(self):
        for url in self.start_urls:
            self.logger.info(url)
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # Return if more than N
        if self.count >= self.N:
            raise CloseSpider(f"\n\nSTUDENT--> SCRAPING SUCESS!! \nScraped {self.N} items. Eject! \nIF YOU SEE THIS MESSAGE, PROBABLY EVERYTHING WENT SMOOTHLY!\n\nIGNORE THE ERROR BELOW - FORCING EXIT")
        # Increment to count by one:
        self.count += 1
        if self.count%50000==0:
            print("Parsed {:,} pages".format(self.count))
        link_extractor = LinkExtractor(allow_domains=self.allowed_domains, unique=False)
        links = link_extractor.extract_links(response)
        loader = ItemLoader(item=FromToItem(), response=response)
        loader.add_value('origin', response.request.url)
        seen = set()
        for link in links:
            url = link.url
            if url in seen or len(url) > 50 or '?' in url or '#' in url or '%' in url:
                continue
            seen.add(url)
            loader.add_value('to', url)
            yield scrapy.Request(url=url, callback=self.parse)
        yield loader.load_item()
