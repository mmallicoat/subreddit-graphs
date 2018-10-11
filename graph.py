import networkx as nx
from networkx.readwrite import json_graph
import matplotlib as mpl
import json
import pdb


def main():
    mpl.use('TkAgg')  # set back-end

    with open('./data/fin_2hop_fix.json') as f:
        docs = json.load(f)

    G = nx.Graph()

    for doc in docs[0:80]:
        G.add_node(doc['subreddit'], subscribers=doc['subscribers'])
        for link in doc['links']:
            if doc['subreddit'] != link:
                G.add_edge(doc['subreddit'], link)

    # Plot graph
    # nx.draw(G, with_labels=True)
    # mpl.pyplot.show()

    # Save graph images
    # mpl.pyplot.savefig("graph.png")

    # Export graph in JSON node-link format
    data = json_graph.node_link_data(G)
    with open('./data/fin-data-link.json', 'w') as outfile:
        json.dump(data, outfile)


if __name__ == '__main__':
    main()
