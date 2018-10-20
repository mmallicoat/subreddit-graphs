Notes
=====

Todo
----

* Fix: change format_data.py to take both input and output filenames
  as arguments, and then write directly
* After this, make sure visualizations work
* Write up report, embedding visualizations
* Get scrapy working again
* Do some simple network analyses/metrics


Done
````
* Use regex to covert subscriber numbers to a numeric
* Convert subreddit links to lower case in spider?
* When exporting graph via networkx library, include subscriber
  number as an attribute of each node
* In graph visualizer, add a function so that the subcriber number
  can be used to change the size of the node

d3
--

``d3.json()`` makes an HTTP request to the local directory (?) to
get the data files. When serving the visualization HTML file using
the Python ``SimpleHTTPServer``, I can see the HTTP request and
the JSON file is correctly loaded. I should be able to simply put
the data on the web server with the HTML page with the
visualization and have it displayed correctly. (The d3 Javascript
code is also queried by an HTTP request.)

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

-   `Tutorial <https://doc.scrapy.org/en/latest/intro/tutorial.html>`__
-   Structure of project from `here
    <https://drivendata.github.io/cookiecutter-data-science/#directory-structure>`__.

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
- Code for `tidy tree
  <https://gist.github.com/mbostock/4339184>`__ previous,
  or maybe from `here <https://gist.github.com/mbostock/912735>`__.
- Tools at `Observable <https://beta.observablehq.com/>`__

Documentation

- `d3-force library <https://github.com/d3/d3-force>`__
- networkx can `exports to JSON
  <https://networkx.github.io/documentation/networkx-1.10/reference/readwrite.json_graph.html>`__
  in format suitable for d3 visualizations

Selectors
---------

- Xpath has more features than CSS selectors, but may be slower.
  It is perhaps better to use CSS unless a more sophisticated selector is needed.

Graph Analysis
--------------

Can use the library ``nethworkx`` for graph analysis and plots.

