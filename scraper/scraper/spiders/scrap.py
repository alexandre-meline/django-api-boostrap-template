from scrapy.spiders import CrawlSpider
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst
from scrapy.http import Request
from scrapy_selenium import SeleniumRequest

from scraper.scraper.items import SpacyTextItem
from app.models import SpacyModel



class ScrapSpider(CrawlSpider):
    name = 'scrap'

    def __init__(self, foreign_key = int, *args, **kwargs):
        super(ScrapSpider, self).__init__(*args, **kwargs)
        self.start_urls = ['https://www.clairedahan.fr/confinement-et-charge-mentale/']
        self.model_id = foreign_key


    def start_requests(self):
        for url in self.start_urls:
            yield SeleniumRequest(url=url, callback=self.parse_item)

    def parse_item(self, response):
        text_loader = ItemLoader(item=SpacyTextItem(), response=response)
        text_loader.default_output_processor = TakeFirst()

        text_loader.add_value('spacy_model', SpacyModel.objects.get(id=self.model_id))
        text_loader.add_css('text', 'p')

        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        yield text_loader.load_item()
