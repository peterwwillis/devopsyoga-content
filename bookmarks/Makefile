all: build

build: venv index.json

# Note: if you don't source ../envrc, processing bookmarks may die due to
# invalid character set parsing.

index.json: bookmarks.json
	. ../envrc && . ./venv/bin/activate && ./extractjson.py bookmarks.json DevOps > index.json

bookmarks.json: bookmarks.html
	. ../envrc && . ./venv/bin/activate && ./bookmarks.py bookmarks.html > bookmarks.json

clean:
	rm -f index.html index.json

venv:
	virtualenv -p python3 venv
	./venv/bin/pip install -r requirements.txt

clean-venv:
	rm -rf venv
