import scrapy
import re
import pdb


class QuotesSpider(scrapy.Spider):
    name = 'subspider'
    start_urls = [
        'https://www.reddit.com/r/programming',
        # 'https://www.reddit.com/r/financialindependence',
    ]

    def parse(self, response):

        # CSS classes of div's in sidebar change frequently!
        for sidebar in response.css('div.s1s8pi67-0'):
            sub_count = subscriber_conversion(
                            sidebar.css('p.s34nhbn-12::text').extract_first()
                        )
            links = list()
            for link in response.css('div.s1s8pi67-0 a::attr(href)').re('/r/\w+'):
                links.append(link.lower())
            yield {
              'subreddit': re.search(r'/r/\w+', response.request.url).group().lower(),
              'description': sidebar.css('p.s34nhbn-14::text').extract_first(),
              'links': links,
              'subscribers': sub_count
            }

        # List is of relative urls to subreddits, e.g., u'/r/foobar/'
        for sub in response.css('div.s1s8pi67-0 a::attr(href)').re('/r/\w+'):
            yield response.follow(sub.lower(), callback=self.parse)

def subscriber_conversion(subscriber_string):
    # pdb.set_trace()
    number = float(re.search(r'[0-9\.]+', subscriber_string).group())
    if subscriber_string[-1] == 'k':
        subscriber_numeric = number * 1000
    elif subscriber_string[-1] == 'm':    
        subscriber_numeric = number * 1000000
    else:
        subscriber_numeric = number
    return subscriber_numeric
