data: data/processed/fin-data-link.json data/processed/prog-data-link.json

analysis: models/fin-stats.txt models/fin-centrality.csv models/fin-clustering.csv models/prog-stats.txt models/prog-centrality.csv models/prog-clustering.csv

plots: reports/figures/fin-graph.png reports/figures/prog-graph.png

data/processed/fin-data-link.json:
	python src/data/format_data.py data/raw/fin_2hop.json data/processed/fin-data-link.json

data/processed/prog-data-link.json:
	python src/data/format_data.py data/raw/prog_2hop.json data/processed/prog-data-link.json

models/fin-stats.txt models/fin-centrality.csv models/fin-clustering.csv: data/processed/fin-data-link.json
	python src/models/graph_analysis.py data/processed/fin-data-link.json models

models/prog-stats.txt models/prog-centrality.csv models/prog-clustering.csv: data/processed/prog-data-link.json
	python src/models/graph_analysis.py data/processed/prog-data-link.json models

reports/figures/fin-graph.png: data/processed/fin-data-link.json
	python src/visualization/plots.py data/processed/fin-data-link.json reports/figures

reports/figures/prog-graph.png: data/processed/prog-data-link.json
	python src/visualization/plots.py data/processed/prog-data-link.json reports/figures
