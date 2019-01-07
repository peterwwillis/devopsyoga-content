all: build

build: ../venv/bin/activate index.html index.json

index.json:
	. ../venv/bin/activate && ./html2json.py index.html > index.json

index.html:
	curl -sL https://itsvit.com/blog/devops-glossary-78-basic-devops-terms-in-simple-words/ > index.html

clean:
	rm -f index.html index.json
