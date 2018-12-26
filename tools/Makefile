.PHONY: tool_chest

all: tool_chest make_cat_pages
	
tool_chest:
	make -C tool_chest $*

make_cat_pages:
	./make_cat_pages.sh ../_data/tools/categories.json

clean:
	make -C tool_chest clean $*
