all: build

build: ../venv/bin/activate index.html index.json

index.json:
	. ../venv/bin/activate && ./html2json.py index.html > index.json

index.html:
	curl -sL https://medium.com/@DZoneInc/48-devops-terms-you-should-know-a-devops-glossary-37e60fd23752 > index.html

clean:
	rm -f index.html index.json
