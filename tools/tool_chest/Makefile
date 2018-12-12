
DATA_DIR := ../../_data

# I'm pretty sure I can get this out of a Make env variable, but anyway...
MY_DIR := tool_chest

all: $(MY_DIR).venv do-tool-chest.html categories.md $(DATA_DIR)/tools/categories.json

$(MY_DIR).venv:
	virtualenv $(MY_DIR).venv && \
	. $(MY_DIR).venv/bin/activate && \
	./$(MY_DIR).venv/bin/pip install -r parse-tool.requirements.txt

do-tool-chest.html:
	./get-tools-xebialabs.sh

categories.md:
	./categories.sh html > categories.md

$(DATA_DIR)/tools/categories.json:
	[ -d $(DATA_DIR)/tools ] || mkdir -p $(DATA_DIR)/tools
	./categories.sh > $(DATA_DIR)/tools/categories.json

clean: clean-local

clean-local:
	rm -f $(DATA_DIR)/tools/categories.json categories.md *.pyc

clean-all: clean-local
	rm -rf do-tool-chest.html $(MY_DIR).venv
