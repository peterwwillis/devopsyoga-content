
# Make sure to create a file called 'envrc' which contains the following 
# entries:
#
#   PAGES_REPO_NWO=<username>/<reponame>
#   JEKYLL_GITHUB_TOKEN=<a github token with public repo scope>

.PHONY: tools clean

all: build

tools:
	make -C tools $*

clean:
	make -C tools clean
	jekyll clean

build: tools update-deps jekyll-build

jekyll-build:
	. $(PWD)/envrc && \
	jekyll doctor -t && \
	jekyll build -t

serve: tools update-deps jekyll-serve

jekyll-serve: envrc
	. $(PWD)/envrc && \
	jekyll doctor -t && \
	jekyll serve -t

# Run 'make SKIP_BUNDLE_UPDATE=1' to skip this step
update-deps:
	if [ -z "$$SKIP_BUNDLE_UPDATE" ] ; then bundle update github-pages ; fi

docker:
	. $(PWD)/envrc && \
	docker run -d --rm -v "$PWD":/usr/src/app -p "4000:4000" starefossen/github-pages
