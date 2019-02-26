
all: venv gitlogs.json install

install: gitlogs.json
	mkdir -p ../../_data/_paginate
	cp -f gitlogs.json ../../_data/_paginate/gitlogs.json
	mkdir -p ../../gitlogs
	./paginate.py gitlogs.json ../../gitlogs gitlogs

gitlogs.json:
	./venv/bin/git2json | ./venv/bin/python parse.py > gitlogs.json

venv:
	virtualenv -p python3 venv && \
	./venv/bin/pip install -r requirements.txt

clean:
	rm -f gitlogs.json venv
