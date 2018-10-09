Notes
=====

Todo
----

* Use regex to covert subscriber numbers to a numeric
* Convert subreddit links to lower case in spider?
* Use subscriber number to determine size of node in graph plot

Scrapy
------

.. code:: bash

    # Use shell to explore a website
    scrapy shell 'http://quotes.toscrape.com'

    # Run spider, dumping results to terminal
    scrapy crawl my_spider

    # Run spider, exporting results to json file
    scrapy crawl my_spider -o out.json

    # Run spider, exporting to csv
    scrapy crawl my_spider -o out.csv -t csv

References
----------

- `Tutorial <https://doc.scrapy.org/en/latest/intro/tutorial.html>`__

Features
---------

- Scrapy does not vist a URL that it has already scraped,
  so you don't have to worry about duplicates

Visualization
-------------

Examples using the Node.JS `d3-hierarchy library <https://github.com/d3/d3-hierarchy>`__:

- Interactive `force-directed graph <https://bl.ocks.org/mbostock/4062045>`__
- `Adjacency matrix <https://bost.ocks.org/mike/miserables/>`__
- Very nice `radial tree <https://bl.ocks.org/mbostock/4063550>`__

Selectors
---------

- Xpath has more features than CSS selectors, but may be slower.
  It is perhaps better to use CSS unless a more sophisticated selector is needed.

Graph Analysis
--------------

Can use the library ``nethworkx`` for graph analysis and plots.

