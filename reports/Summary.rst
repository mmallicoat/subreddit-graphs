Analyzing Subreddit Networks
============================

Introduction
------------

The popular website reddit.com contains numerous messageboards
(called "subreddits"), each dedicated to a particular subject,
such as a hobby or topic of interest. Often the users of these
subreddits will place links to related subreddits on the sidebar
of the webpage. In this way, these linked subreddits form a
network of related online communities. By following these links
programmatically, we can quickly collect the data which represents
these network, which we can then use to visualize and analyze
them.

These human-curated lists of links give high-quality indicators of
related topics and communities.

Scrape the Data
---------------

I wrote simple web scraper using the Python library ``scrapy`` to
collect the list of links nad other information from each
subreddit page. Starting from an initial subreddit, the scraper
searches the sidebar on the page for any related subreddits that
have been linked there. The scraper then follows those links and
iteratively searches for more links. The name of each subreddit is
collected, along with its description, number of subscribers, and
the list of links to other subreddits.

From these data, it is possible to construct the network of
subreddits centered at the initial page. In this network (or
graph), each node is a subreddit and each edge is a hyperlink
between them. For simplicity, I decided to build a non-directed
graph, treating a hyperlink from subreddit A to B in the same
manner as a hyperlink from subreddit B to A.

The spider uses CSS selectors to locate the desired elements on
each webpage. Here is a code snippet with the selectors:

.. code:: python

    for sidebar in response.css('div.s1s8pi67-0'):
        sub_count = subscriber_conversion(
                        sidebar.css('p.s34nhbn-12::text').extract_first()
                    )  # convert from string to numeric
        links = list()
        for link in response.css('div.s1s8pi67-0 a::attr(href)').re(r'/r/\w+'):
            links.append(link.lower())
        yield {
          'subreddit': re.search(r'/r/\w+', response.request.url).group().lower(),
          'description': sidebar.css('p.s34nhbn-14::text').extract_first(),
          'links': links,
          'subscribers': sub_count
        }

The sidebar on the page is idenitified using the method
``response.css('div.s1s8pi67-0')`` where ``response`` is the
object representing the returned webpage. The string
``s1s8pi67-0`` is the unique class attribute (?) of the ``div``
element containing the sidebar. [#selectors]_ The name of the subreddit, the
subreddit's description, the list of links in the sidebar, and the
number of subscribers are returned by the spider.

I chose two subreddits to use as the starting points to crawl
through related pages: ``/r/programming`` and
``/r/financialindependence``. Both of these have a fair number of
subreddits listed in their sidebars, which should lead to larger,
more complex networks.

.. [#selectors] (Using these seemingly random class attributes (?) for the
    selectors is less than ideal: they are non-semantic and they seem
    to change fairly frequently, possibly with each build of the
    website. A refinement to find a more robust selector. I think it
    would be possible to use an xpath selector to find the text
    ``/r/[subreddit name]`` that appears in the sidebar, and then
    select the element contianing this a few steps up the hierarchy.)

Visualizations
--------------

After collecting the network data, we can use the library
``networkx`` to analyze and visualize the networks. Quickly, I
made a couple plots using ``matplotlib`` to visualize the graphs.

.. figure:: ./figures/prog-graph.png
   :scale: 75 %
   :alt: network centered as /r/programming
   :align: center

   Plot of the network centered at the subreddit /r/programming

Unfortunately, these were difficult to read and not very useful
for exploring the networks. To remedy this, I decided to instead
use the visualization library ``d3`` (written in Javascript) to
make some interactive plots.

Click on the images below to view the interactive plots.

The relative number of subscribers to each subreddit is
represented by the radius of the node in this chart (using a
log-scale).

One of the most salient features is the "spoke-and-hub" pattern: a
larger subreddit links to many smaller subreddits, which are often
dedicated to a more specific topic. For example,
/r/financialindependence is linked to country-specific subreddits
for Canada (/r/canadaFIRE ?), UK (/r/ukfire), and so on.

It is sensible to group clusters of nodes into larger structures:
the closely related group of a subreddits surrounding /r/collapse
(?) are all dedicated to the topic of societal and economic
collapse.

Analysis
--------

Using ``networkx``, we can also calculate metrics which helps us
to better understand the network. One of the foremost metrics is
[centrality???]: this expresses the XXX of each node with respect
to the larger network. The values calculated are:

[table]

Not surprisingly, the XXX node(s) have the largest values.

Conclusion
----------

A more extensive network could be constructed by crawling the
actual posts on each messageboard and collecting hyperlinks given
there. The number of links to each subreddit could be tabulated in
order to measure the *strength* of each link in the network.
