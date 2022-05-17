from scrapy.spiders import CrawlSpider
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst
from scrapy_selenium import SeleniumRequest

from scraper.scraper.items import SpacyTextItem
# Foreign key model
from app.models import SpacySujet



class TextSpider(CrawlSpider):
    name = 'text_spider'

    output_data = []

    def __init__(self, foreign_key = int, url = str,
                 *args, **kwargs):
        super(TextSpider, self).__init__(*args, **kwargs)
        # Parametres depuis management/commands/crawl.py
        self.start_urls = url
        self.model_id = foreign_key

    def start_requests(self):
        yield SeleniumRequest(url=self.start_urls, callback=self.parse_urls_news)

    def parse_urls_news(self, response):

        # ______________ Parsing Google Alerte  ______________
            import re
            reg_results_urls = re.compile('\<link\shref=.*?\;url=(.*?)&amp;.*?><\/link>')
            # Recuperation titre d'Alerte (Basket)
            reg_title_results = re.compile(':\s(.*?)</title>')
            self.title_results = re.findall(reg_title_results, str(response.body))[0]

            # Recuperation des urls
            parse_urls_results_list = re.findall(reg_results_urls, str(response.body))
            for url in parse_urls_results_list:
                yield SeleniumRequest(url=url, callback=self.parse_text)

    def parse_text(self, response):
        p_texts = response.xpath('//p/text()').getall()
        text_loader = ItemLoader(item=SpacyTextItem(), response=response)
        text_loader.default_output_processor = TakeFirst()
        for text in p_texts:
            text_loader.add_value('spacy_sujet', SpacySujet.objects.get(id=self.model_id))
            text_loader.add_value('text', text)
            yield text_loader.load_item()
