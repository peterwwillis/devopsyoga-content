all: build

build: venv build-subdirs index.yaml

build-subdirs:
	for d in * ; do [ -d "$$d" ] && make -C "$$d" $* ; done

install: ../_data/glossary/index.yaml

../_data/glossary/index.yaml: index.yaml
	mkdir -p ../_data/glossary
	cp -f index.yaml ../_data/glossary/index.yaml

index.yaml: venv
	. ../envrc && . ./venv/bin/activate && ./concat.py */index.json > index.yaml

venv:
	virtualenv -p python3 venv
	./venv/bin/pip install -r requirements.txt

clean: clean-subdirs
	rm -rf venv index.yaml

clean-subdirs:
	for d in * ; do [ -d "$$d" ] && make -C "$$d" clean $* ; done
