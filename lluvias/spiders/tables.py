# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy.spider import BaseSpider
from lluvias.items import LluviasItem

class TablesSpider(scrapy.Spider):
	name = 'tables'
	allowed_domains = ['senamhi.gob.pe']
	start_urls = ['http://senamhi.gob.pe/']

	def __init__(self, *args, **kwargs):
		super(TablesSpider, self).__init__(*args, **kwargs)

	def start_requests(self):
		#Cajamarca
		codes = [line.rstrip('\n') for line in open('../full.csv')]
		
		for code in codes:
			_c = code.split(",")[4]
			t_e = code.split(",")[3]
			tipo = code.split(",")[10] 
			for year in range(1901, 2018):
				for month in range(1, 13):
					url = 'http://www.senamhi.gob.pe/include_mapas/_dat_esta_tipo02.php?CBOFiltro=%s%s&estaciones=%s&tipo=%s&t_e=%s' % (year, month, _c, tipo, t_e)
					yield scrapy.Request(url, callback=self.parse,meta={'id': _c, 'values':code})

	def parse(self, response):
		#["date","max_temp","min_temp","temp_seco","temp_hum","precip","dir_viento","vel_viento"]
		table = response.xpath("//table")
		for row in table.xpath("//tr"):
			tds = row.xpath("td")
			if len(tds) >= 13:
				item = LluviasItem()
				code = response.meta.get('id')
				_v = response.meta.get('values').split(",")
				item['estacionid'] = code
				item['distrito'] = _v[5]
				item['provincia'] = _v[6]
				item['departamento'] = _v[7]
				item['lng'] = _v[0]
				item['lat'] = _v[1]
				item['tipo'] = _v[9]
				item['tipo2'] = _v[8]
				item['tipocode'] = _v[10]
				item['t_e'] = _v[3]
				item['_v'] = _v[2]
				item["date"] = row.xpath("td[1]//text()").extract();
				item["max_temp"] = row.xpath("td[2]//text()").extract();
				item["min_temp"] = row.xpath("td[3]//text()").extract();
				item["temp_seco"] = row.xpath("td[4]//text()").extract();
				item["temp_hum"] = row.xpath("td[5]//text()").extract();
				item["precip"] = row.xpath("td[6]//text()").extract();
				item["dir_viento"] = row.xpath("td[7]//text()").extract();
				item["vel_viento"] = row.xpath("td[8]//text()").extract();
				yield item

			#,"max_temp","min_temp","min_temp","temp_hum","precip","dir_viento","dir_viento"


    #pass
