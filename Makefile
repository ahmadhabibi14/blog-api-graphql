setup:
	pip install --upgrade pip
	python -m venv .venv
	source .venv/bin/activate
	pip install -r requirements.txt

update-dep:
	pip freeze > requirements.txt

install-dep:
	pip install -r requirements.txt