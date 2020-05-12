clean:
	find . -name "*.pyc" -type f -delete
	find . -name "__pycache__" -type d -delete
	find . -name ".ipynb_checkpoints" -type d -delete

format:
	yapf --verbose --in-place --recursive . --style='{based_on_style: google, indent_width:2, column_limit:80}'
	isort --verbose --force-single-line-imports -y --skip-glob=./__init__.py
	docformatter --in-place --recursive .

test:
	pytest meta
