from __future__ import absolute_import

from scrapy import Request
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from scrapy.loader.processors import Identity
from scrapy.spiders import Rule

from ..utils.spiders import BasePortiaSpider
from ..utils.starturls import FeedGenerator, FragmentGenerator
from ..utils.processors import Item, Field, Text, Number, Price, Date, Url, Image, Regex
from ..items import PortiaItem


class ProvidenciaCrawler(BasePortiaSpider):
    name = "providencia_crawler"
    allowed_domains = [
        u'www.portalinmobiliario.com',
        u'www.portalinmobiliario.com']
    start_urls = [u'https://www.portalinmobiliario.com/venta/departamento/providencia-metropolitana?tp=2&op=1&ca=2&ts=1&dd=0&dh=6&bd=0&bh=6&or=&mn=2&sf=0&sp=0']
    rules = [
        Rule(
            LinkExtractor(
                allow=(u'/venta/departamento/providencia-metropolitana'),
                deny=()
            ),
            callback='parse_item',
            follow=True
        )
    ]
    items = [
        [
            Item(
                PortiaItem,
                None,
                u'.product-item',
                [
                    Field(
                        u'thumbnail',
                        '.col-sm-3 > a > img::attr(src)',
                        []),
                    Field(
                        u'type',
                        '.col-sm-9 > .row > .col-sm-6 > p:nth-child(1) *::text',
                        []),
                    Field(
                        u'url_path',
                        '.col-sm-9 > .row > .col-sm-6 > h4 > a::attr(href)',
                        [],
                        True),
                    Field(
                        u'name',
                        '.col-sm-9 > .row > .col-sm-6 > h4 > a *::text',
                        []),
                    Field(
                        u'code',
                        '.col-sm-9 > .row > .col-sm-6 > p:nth-child(3) *::text',
                        []),
                    Field(
                        u'dorm/bath',
                        '.col-sm-9 > .row > .col-sm-6 > p:nth-child(4) > .label *::text',
                        []),
                    Field(
                        u'price_to',
                        '.col-sm-9 > .row > div:nth-child(2) > .product-property > .product-property-value *::text',
                        []),
                    Field(
                        u'area',
                        '.col-sm-9 > .row > div:nth-child(3) > .product-property > .product-property-value *::text',
                        [])])]]
