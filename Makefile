
# Make sure to create a file called 'envrc' which contains the following 
# entries:
#
#   PAGES_REPO_NWO=<username>/<reponame>
#   JEKYLL_GITHUB_TOKEN=<a github token with public repo scope>

.PHONY: tools clean

all: build

tools:
	. $(PWD)/envrc && \
	make -C tools $*

clean:
	. $(PWD)/envrc && \
	make -C tools clean && \
	bundle exec jekyll clean

clean-all: clean-deps
	. $(PWD)/envrc && \
	make -C tools clean-all && \
	bundle exec jekyll clean

build: tools update-deps jekyll-build

jekyll-build:
	. $(PWD)/envrc && \
	bundle exec jekyll doctor -t && \
	bundle exec jekyll build -t

serve: tools update-deps jekyll-serve

jekyll-serve: envrc
	. $(PWD)/envrc && \
	bundle exec jekyll doctor -t && \
	bundle exec jekyll serve -t

# Run 'make SKIP_BUNDLE_UPDATE=1' to skip this step entirely.
# Run 'make BUNDLE_DEPLOYMENT=1' to use --deployment, which is kind of weird.
# 
# Read more about 'bundle install' weirdness at https://bundler.io/bundle_install.html
update-deps:
	. $(PWD)/envrc && \
	if [ -z "$$SKIP_BUNDLE_UPDATE" ] ; then \
		if [ ! -d ".bundle" ] ; then \
			if [ "x$$BUNDLE_DEPLOYMENT" = "x1" ] ; then \
				bundle install --jobs 4 --deployment ; \
			else \
				bundle install --jobs 4 --path vendor/bundle ; \
			fi ; \
		fi ; \
		bundle update --all ; \
	fi

clean-deps:
	rm -rf vendor/ .bundle

docker:
	. $(PWD)/envrc && \
	docker run -d --rm -v "$(PWD)":/usr/src/app -p "4000:4000" starefossen/github-pages
