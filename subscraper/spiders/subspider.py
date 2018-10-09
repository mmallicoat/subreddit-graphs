import scrapy
import re


class QuotesSpider(scrapy.Spider):
    name = 'subspider'
    start_urls = [
        'https://www.reddit.com/r/financialindependence',
    ]

    def parse(self, response):
        for sidebar in response.css('div.venmmj-0'):
            yield {
              'subreddit': re.search(r'/r/\w+', response.request.url).group(),
              'description': sidebar.css('p.s1smssg-14::text').extract_first(),
              # TODO: change link strings to lowercase to match subreddit names
              'links': response.css('div.venmmj-0 a::attr(href)').re('/r/\w+'),
              'subscribers': subscriber_conversion(
                             sidebar.css('p.s1smssg-12::text').extract_first(),
                             )
            }

        # List is of relative urls to subreddits, e.g., u'/r/foobar/'
        for sub in response.css('div.venmmj-0 a::attr(href)').re('/r/\w+'):
            yield response.follow(sub, callback=self.parse)

def subscriber_conversion(subscriber_string):
    number = float(re.search(r'[0-9\.]+', subscriber_string))
    if subscriber_string[-1] == 'k':
        subscriber_numeric = number * 1000
    elif subscriber_string[-1] == 'm':    
        subscriber_numeric = number * 1000000
    else:
        subscriber_numeric = number
    return subscriber_numeric
