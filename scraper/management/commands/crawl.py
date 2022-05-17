from django.core.management.base import BaseCommand
from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings

from scraper.scraper import settings as my_settings
from scraper.scraper.spiders.scrap import ScrapSpider
from scraper.scraper.spiders.texts_spider import TextSpider

# Tutoriel d'integration
# https://medium.com/analytics-vidhya/web-scraping-with-scrapy-and-django-94a77386ac1b
class Command(BaseCommand):
    help = 'Release spider'

    def add_arguments(self, parser):
        parser.add_argument('-s', '--spider', type=str, help='Define a spider', )
        parser.add_argument('-fk', '--foreign_key', type=int, help='Define a foreign key', )
        parser.add_argument('-u', '--url', type=str, help='Define a url for start scrap', )

    def handle(self, *args, **options):
        crawler_settings = Settings()
        crawler_settings.setmodule(my_settings)

        if options['spider'] == "ScrapSpider":
            process = CrawlerProcess(settings=crawler_settings)
            process.crawl(ScrapSpider,
                          foreign_key=options['foreign_key'])
            process.start()
        elif options['spider'] == "TextSpider":
            process = CrawlerProcess(settings=crawler_settings)
            process.crawl(TextSpider,
                          foreign_key=options['foreign_key'],
                          url= options['url'])
            process.start()
        else:
            pass