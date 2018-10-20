data: src/data/fin-data-link.json src/data/prog-data-link.json

src/data/fin-data-link.json:
	python src/data/format_data.py data/raw/fin_2hop.json data/processed/fin-data-link.json

src/data/prog-data-link.json:
	python src/data/format_data.py data/raw/prog_2hop.json data/processed/prog-data-link.json
