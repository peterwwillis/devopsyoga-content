.PHONY: tool_chest

#CAT_FILE_LIST := ./make_cat_pages.sh --list

all: tool_chest make_cat_pages
	
tool_chest:
	make -C tool_chest $*

make_cat_pages: clean_cat_pages
	./make_cat_pages.sh --write ../_data/tools/categories.json

clean_cat_pages:
	./make_cat_pages.sh --clean ../_data/tools/categories.json

clean: clean_cat_pages
	make -C tool_chest clean $*
