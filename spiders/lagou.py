# -*- coding: utf-8 -*-
import scrapy

class LagouSpider(scrapy.Spider):
	name = "lagou"
	start_urls=(
		'https://www.lagou.com/zhaopin//',
	)

	def parse(self,response):
		fp = open('1.html','w')
		fp.write(response.body)
		fp.close()
		print response.body
