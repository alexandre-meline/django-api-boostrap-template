# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html


from scrapy_djangoitem import DjangoItem
from app.models import SpacyText


class SpacyTextItem(DjangoItem):
    django_model = SpacyText