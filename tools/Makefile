
all: tools.venv do-tool-chest.html categories.md ../_data/tools/categories.json

tools.venv:
	virtualenv tools.venv && \
	. tools.venv/bin/activate && \
	./tools.venv/bin/pip install -r parse-tool.requirements.txt

do-tool-chest.html:
	./get-tools-xebialabs.sh

categories.md:
	./categories.sh html > categories.md

../_data/tools/categories.json:
	[ -d ../_data/tools ] || mkdir -p ../_data/tools
	./categories.sh > ../_data/tools/categories.json

clean: clean-local

clean-local:
	rm -f ../_data/tools/categories.json categories.md

clean-all: clean-local
	rm -rf do-tool-chest.html tools.venv
