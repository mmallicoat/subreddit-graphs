import networkx as nx
import matplotlib as mpl
import json
import pdb


def main():
    mpl.use('TkAgg')  # set back-end

    with open('out.json') as f:
        docs = json.load(f)

    G = nx.Graph()

    for doc in docs[0:80]:
        G.add_node(doc['subreddit'])
        for link in doc['links']:
            if doc['subreddit'] != link:
                G.add_edge(doc['subreddit'], link)

    nx.draw(G, with_labels=True)
    mpl.pyplot.show()

    pdb.set_trace()


if __name__ == '__main__':
    main()
