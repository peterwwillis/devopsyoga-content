all: build

build: ../venv/bin/activate index.html index.json

index.json:
	. ../venv/bin/activate && ./html2json.py index.html > index.json

index.html:
	curl -sL $$(cat link.txt) > index.html

clean:
	rm -f index.html index.json
