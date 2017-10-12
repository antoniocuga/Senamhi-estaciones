# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LluviasItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field() 
    estacionid = scrapy.Field()
    distrito = scrapy.Field()
    provincia = scrapy.Field()
    departamento = scrapy.Field()
    lng = scrapy.Field()
    lat = scrapy.Field()
    tipo = scrapy.Field()
    tipo2 = scrapy.Field()
    tipocode = scrapy.Field()
    t_e = scrapy.Field()
    _v = scrapy.Field()
    date = scrapy.Field()
    max_temp = scrapy.Field()
    min_temp = scrapy.Field()
    temp_seco = scrapy.Field()
    temp_hum = scrapy.Field()
    precip = scrapy.Field()
    dir_viento = scrapy.Field()
    vel_viento = scrapy.Field()
    pass
