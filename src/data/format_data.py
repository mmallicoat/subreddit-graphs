import networkx as nx
from networkx.readwrite import json_graph
import json
import os
import sys

def main(argv):

    # Find project root directory
    inputfile = os.path.abspath(argv[1])
    outputfile = os.path.abspath(argv[2])
        
    # Read in raw graph data
    with open(inputfile) as f:
        docs = json.load(f)
        f.close()

    # Build graph
    G = nx.Graph()
    for doc in docs:
        G.add_node(doc['subreddit'], subscribers=doc['subscribers'])
        for link in doc['links']:
            if doc['subreddit'] != link:  # exclude links to itself
                edge = (doc['subreddit'], link)
                if edge not in list(G.edges):  # don't duplicate edges
                    G.add_edge(*edge)

    # Export graph in JSON node-link format
    link_data = json_graph.node_link_data(G)
    
    # Export JSON
    with open(outputfile, 'w') as f:
        json.dump(link_data, f)
        f.close()

if __name__ == '__main__':
    main(sys.argv)
