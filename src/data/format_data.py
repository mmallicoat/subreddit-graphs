import networkx as nx
from networkx.readwrite import json_graph
import json
import os
import sys

def main(inputfile):

    # Find project root directory
    script_dir = os.path.dirname(__file__)
    proj_dir = os.path.abspath(os.path.join(script_dir, '../..'))
    
    # Read in and convert
    graph = convert(os.path.join(proj_dir, inputfile))

    # Export JSON
    return graph
    # with open(os.path.join(proj_dir, outputfile), 'w') as f:
        # json.dump(graph, f)

def convert(filepath):

    # Read raw data
    with open(filepath) as f:
        docs = json.load(f)

    # Build graph
    G = nx.Graph()
    for doc in docs[0:80]:
        G.add_node(doc['subreddit'], subscribers=doc['subscribers'])
        for link in doc['links']:
            if doc['subreddit'] != link:
                G.add_edge(doc['subreddit'], link)

    # Export graph in JSON node-link format
    link_data = json_graph.node_link_data(G)
    return link_data


if __name__ == '__main__':
    inputfile = sys.argv[1]
    main(inputfile)
