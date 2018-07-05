import scrapy
import re


class QuotesSpider(scrapy.Spider):
    name = 'sub'
    start_urls = [
        'https://www.reddit.com/r/financialindependence/',
    ]

    def parse(self, response):
        # Below returns a list of relative urls to subreddits from the sidebar
        # response.css('div.venmmj-0 a::attr(href)').re('/r/\w+')
        # Description
        # response.css('div.venmmj-0 p.s1smssg-14::text').extract_first()

        for sidebar in response.css('div.venmmj-0'):
            yield {
              'subreddit': re.search(r'r/\w+', response.request.url).group(),
              'description': sidebar.css('p.s1smssg-14::text').extract_first(),
              # subscriber_count
              # online_count
            }

        # List is of relative urls to subreddits, e.g., u'/r/finance/'
        for sub in response.css('div.venmmj-0 a::attr(href)').re('/r/\w+'):
            yield response.follow(sub, callback=self.parse)
