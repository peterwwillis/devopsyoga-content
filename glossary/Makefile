all: build

build: venv
	for d in * ; do [ -d "$$d" ] && make -C "$$d" $* ; done

venv:
	virtualenv -p python3 venv
	./venv/bin/pip install -r requirements.txt

clean:
	rm -rf venv
