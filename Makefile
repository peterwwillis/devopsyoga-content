
# Make sure to create a file called 'envrc' which contains the following 
# entries:
#
#   PAGES_REPO_NWO=<username>/<reponame>
#   JEKYLL_GITHUB_TOKEN=<a github token with public repo scope>

.PHONY: tools clean

all: tools

tools:
	make -C tools $*

clean:
	make -C tools clean

dev: all update-deps jekyll-serve

# Set SKIP_BUNDLE_UPDATE=1 in 'make' command to skip this step
update-deps:
	if [ -z "$$SKIP_BUNDLE_UPDATE" ] ; then bundle update github-pages ; fi

jekyll-serve: envrc
	jekyll serve

docker:
	docker run -d --rm -v "$PWD":/usr/src/app -p "4000:4000" starefossen/github-pages
