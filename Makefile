fin-data-link.json: src/data/format_data.py
	python src/data/format_data.py data/raw/fin_2hop.json > data/processed/fin-data-link.json

prog-data-link.json: src/data/format_data.py
	python src/data/format_data.py data/raw/prog_2hop.json > data/processed/prog-data-link.json
