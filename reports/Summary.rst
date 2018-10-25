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
make some interactive plots. (We convert the network data into the
"data-link" format using ``networkx`` since this format can be
easily read in by ``d3``.)

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

Density
```````

The two networks have a low average degree [TODO: define] per
node, both around 1.3.

The graph *density* is also low. [Define.]


Centrality
``````````

Using ``networkx``, we can also calculate metrics which helps us
to better understand the network. One property of nodes in a
network that we are interested in is their centrality. The metric
of *betweenness centrality* is one way of calculating this.
The betweenness centrality of a node is the proportion of
shortness paths between any (other?) two nodes that pass through
it. Spoke nodes will have low values and hubs high values.

The most central nodes in the financial network are:

============================    =========================
Subreddit                	Betweenness Centrality
============================    =========================
/r/frugal			0.63
/r/buildapc			0.48
/r/collapse			0.31
/r/gamedeals			0.29
/r/simpleliving			0.26
/r/canadianhardwareswap		0.24
/r/zerowaste			0.19
/r/meditation			0.17
/r/steam			0.14
/r/buildapcsales		0.12
/r/financialindependence	0.12
============================    =========================

/r/frugal and /r/buildapc are central because they act as a bridge
between the financial branch of the network and the PC/gaming
branch. Because of this, many shortest paths must pass through
them. /r/frugal also unites the main hubs in the financial branch,
/r/collapse, /r/zerowaste, /r/simpleliving, and
/r/financialindependence.

/r/collapse is the hub of many small subreddits that are not
linked to any other nodes.

/r/gamedeals is a bridge from the PC-building sub-branch and the
gaming sub-branch.

Clustering
``````````

Another metric for network analysis is the *clustering
coefficient.*

The *degree* of a node is the number of nodes it is connected to.
Suppose there is a node *u* with degree *n*. A *triangle* is a
sub-graph of three nodes that are each connected to each other.
The maximum possible of triangles including *u* is *n* choose 2,
or *n \* (n - 1) / 2*. The number of existing triangles including
node *u* is divided by this maximum number. So, the clustering
coefficient will always be between 0 and 1. It can be interpretted
as the [appropriateness of grouping the node with the others it is
connected to].

Any node that is only connected to a single other node will always
have a clustering coefficient of 0. If all of a node's neighboring
nodes are connected, then the node will have a clustering
coefficient of 1.

Most of the nodes in our two networks are spokes only connected to
a single hub node and will have a clustering cofficient of 0.
Nodes with coefficients much larger than 0 are more rare.  This is
perhaps not surprising given that these are sparse graphs.

The nodes in the programming network with the highest clustering
coefficients are:

=============================   =========================
Subreddit			Clustering Coefficient
=============================   =========================
/r/programmerhumor		1.00
/r/cseducation			1.00
/r/computerscience		1.00
/r/cryptocurrencymemes		1.00
/r/compsci			1.00
/r/freelance			1.00
/r/cs_questions			1.00
/r/resumes			1.00
/r/coding			1.00
/r/javascript			1.00
/r/experienceddevs		1.00
/r/learnprogramming		0.67
=============================   =========================

[Maybe add a column for the degree of each node to get a better
picture?]

Many of these have very few neighbors, such as /r/programmerhumor.

/r/cseducation, /r/computerscience, and /r/cs_questions are share
the same two neighbors: /r/csmajors and /r/cscareerquestions.
These are all concerned with educational and career concerns.

Conclusion
----------

There is much room for expansion on this sort of anlysis. A more
extensive network could be constructed by crawling the actual
posts on each messageboard and collecting hyperlinks given there.
Links to webpages outside of reddit.com could also be crawled.
The number of links between webpages could be tabulated in order
to measure the *strength* of each link in the network. Instead of
an undirected graph, the direction of the links could be
incorporated into the model.

Network anlysis can give insights into the organization of a
network...

