data: data/processed/fin-node-link.json data/processed/prog-node-link.json

analysis: models/fin-stats.txt models/fin-centrality.csv models/fin-clustering.csv models/prog-stats.txt models/prog-centrality.csv models/prog-clustering.csv

plots: reports/figures/fin-graph.png reports/figures/prog-graph.png

data/processed/fin-node-link.json:
	python src/data/format_data.py data/raw/fin_2hop.json data/processed/fin-node-link.json

data/processed/prog-node-link.json:
	python src/data/format_data.py data/raw/prog_2hop.json data/processed/prog-node-link.json

models/fin-stats.txt models/fin-centrality.csv models/fin-clustering.csv: data/processed/fin-node-link.json
	python src/models/graph_analysis.py data/processed/fin-node-link.json models

models/prog-stats.txt models/prog-centrality.csv models/prog-clustering.csv: data/processed/prog-node-link.json
	python src/models/graph_analysis.py data/processed/prog-node-link.json models

reports/figures/fin-graph.png: data/processed/fin-node-link.json
	python src/visualization/plots.py data/processed/fin-node-link.json reports/figures

reports/figures/prog-graph.png: data/processed/prog-node-link.json
	python src/visualization/plots.py data/processed/prog-node-link.json reports/figures
