import networkx as nx
import json
import pdb
import os
import sys
import pandas as pd

def main(argv):
    
    graphfile = os.path.abspath(argv[1])
    statsdir = os.path.abspath(argv[2])

    # Load data-link data and build graph
    graphdata = json.load(open(graphfile, 'r'))
    G = nx.node_link_graph(graphdata)

    # Get model name
    stem = os.path.basename(graphfile)
    model = stem.split('-')[0]

    # Crude statistics
    N, K = G.order(), G.size()
    avg_deg = float(K) / N
    density = 2 * float(K) / (N * (N - 1))
    with open(os.path.join(statsdir, model + '-stats.txt'), 'w') as f:
        f.write("Nodes: %s\n" % N)
        f.write("Edges: %s\n" % K)
        f.write("Average degree: %s\n" % round(avg_deg, 2))
        f.write("Graph density: %s\n" % round(density, 2))
        f.close()

    # Clustering coefficient
    nodes = nx.clustering(G)
    df = pd.DataFrame.from_dict(nodes, orient='index', columns=['coeff'])
    df.sort_values(by='coeff', inplace=True, ascending=False)
    df['coeff'] = df['coeff'].apply(lambda x: round(x, 2))  # round values
    df.to_csv(os.path.join(statsdir, model + '-clustering.csv'),
              index_label='subreddit')

    # Betweenness centrality
    nodes = nx.betweenness_centrality(G)
    df = pd.DataFrame.from_dict(nodes, orient='index', columns=['centrality'])
    df.sort_values(by='centrality', inplace=True, ascending=False)
    df['centrality'] = df['centrality'].apply(lambda x: round(x, 2))
    df.to_csv(os.path.join(statsdir, model + '-centrality.csv'),
              index_label='subreddit')
    
if __name__ == '__main__':
    main(sys.argv)
