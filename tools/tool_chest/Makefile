
DATA_DIR := ../../_data

# I'm pretty sure I can get this out of a Make env variable, but anyway...
MY_DIR := tool_chest

all: build-all test
	
build-all: $(MY_DIR).venv do-tool-chest.html $(DATA_DIR)/tools/categories.json $(DATA_DIR)/tools/tool_list.json

$(MY_DIR).venv:
	virtualenv -p python3 $(MY_DIR).venv && \
	. $(MY_DIR).venv/bin/activate && \
	for r in *.requirements.txt ; do \
	    ./$(MY_DIR).venv/bin/pip install -r $$r ; \
	done

do-tool-chest.html:
	./get-tools-xebialabs.sh

$(DATA_DIR)/tools/categories.json:
	[ -d $(DATA_DIR)/tools ] || mkdir -p $(DATA_DIR)/tools
	./tool_chest.sh --categories-more > $(DATA_DIR)/tools/categories.json

$(DATA_DIR)/tools/tool_list.json:
	[ -d $(DATA_DIR)/tools ] || mkdir -p $(DATA_DIR)/tools
	./tool_chest.sh --tools > $(DATA_DIR)/tools/tool_list.json

clean: clean-local clean-py

clean-local:
	rm -f $(DATA_DIR)/tools/categories.json $(DATA_DIR)/tools/tool_list.json

clean-py:
	rm -rf __pycache__ *.pyc

clean-venv:
	rm -rf $(MY_DIR).venv

clean-html:
	rm -f do-tool-chest.html

clean-all: clean clean-venv clean-html

test:
	./func_test.sh >/dev/null
