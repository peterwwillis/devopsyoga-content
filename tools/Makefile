
all: parse-tool do-tool-chest.html

parse-tool:
	virtualenv parse-tool && \
	. parse-tool/bin/activate && \
	./parse-tool/bin/pip install -r parse-tool.requirements.txt

do-tool-chest.html:
	./get-tools-xebialabs.sh
