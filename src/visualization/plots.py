import networkx as nx
import matplotlib as mpl
import json
import os
import sys

def main(argv):

    graphfile = os.path.abspath(argv[1])
    outputdir = os.path.abspath(argv[2])

    # Load data-link data and build graph
    graphdata = json.load(open(graphfile, 'r'))
    G = nx.node_link_graph(graphdata)

    # Get model name
    stem = os.path.basename(graphfile)
    model = stem.split('-')[0]

    # Plot graph
    mpl.use('TkAgg')  # set back-end
    nx.draw(G, with_labels=True)
    # mpl.pyplot.show()  # use to show graphs in interactive mode

    # Save graph images
    mpl.pyplot.savefig(os.path.join(outputdir, model + '-graph.png'))

if __name__ == '__main__':
    main(sys.argv)
