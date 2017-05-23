# -*- coding: utf-8 -*-
import scrapy
from datetime import datetime
from datetime import timedelta

class PositionSpider(scrapy.Spider):
    name = 'positionspider'
    start_urls = ['https://ruby-china.org/topics']
    LIMIT_DAYS = -2

    def parse(self, response):
        stop = False
        self.logger.warning("body: %s", response.body)
        for topic in response.css('div.topic'):
            # date = topic.css("div.timeago ::attr(title)").extract_first()
            # datetime_object = datetime.strptime(date, '%Y年%m月%d日')
            # limit_date = datetime.today() + timedelta(days=LIMIT_DAYS)
            # if datetime_object >= limit_date:
            title = topic.css('div.media-heading')
            yield {'title': title.css('a ::attr(title)').extract_first()}
            # else:
            #     stop = True

        # if not stop:
        #     next_page = response.css('ul.pagination > li.next > a ::attr(href)').extract_first()
        #     if next_page:
        #         yield scrapy.Request(response.urljoin(next_page), callback=self.parse)
