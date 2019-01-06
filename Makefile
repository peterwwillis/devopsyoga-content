
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

fail-if-gemfile-changed:
	DIFFOUT=$$(git diff Gemfile.lock) ; \
	if [ -n "$$DIFFOUT" ] ; then \
		echo -e "Gemfile.lock has changed! Please commit before running build.\n\n$$DIFFOUT" ; \
		exit 1 ; \
	fi

generate: tools update-deps fail-if-gemfile-changed

build: generate jekyll-build

jekyll-build:
	. $(PWD)/envrc && \
	bundle exec jekyll doctor -t && \
	bundle exec jekyll build -t

serve: generate jekyll-serve

jekyll-serve: envrc
	. $(PWD)/envrc && \
	bundle exec jekyll doctor -t && \
	bundle exec jekyll serve -t

# Run 'make SKIP_BUNDLE_UPDATE=1' to skip this step entirely.
# Run 'make BUNDLE_DEPLOYMENT=1' to use --deployment, which is kind of weird.
# 
# Read more about 'bundle install' weirdness at https://bundler.io/bundle_install.html
update-deps: update-ruby-rvm
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

# To use the latest gems we need a recent ruby.
# This will install it using rvm.
# Right now it's defaulting to compiling it from scratch...
# should probably fix that.
update-ruby-rvm:
	. $(PWD)/envrc && \
	RUBY_WANT_VER=$$(cat $(PWD)/.ruby-version) ; \
	if ! which ruby >/dev/null || ! ruby -v | grep -F $$RUBY_WANT_VER ; then \
		if [ ! -d "rvm/rubies/ruby-$$RUBY_WANT_VER" ] ; then \
			echo "Upgrading ruby! Hold on to your butts..." ; \
			if [ ! -d "rvm.sh" ] ; then \
				curl -sSL https://get.rvm.io > rvm.sh ; \
			fi ; \
			chmod 755 rvm.sh && \
			./rvm.sh --path $(PWD)/rvm --ignore-dotfiles && \
			./rvm/bin/rvm autolibs disable && \
			./rvm/bin/rvm install $$RUBY_WANT_VER && \
			"./rvm/rubies/ruby-$$RUBY_WANT_VER/bin/ruby" -v >/dev/null && \
			./rvm/bin/rvm cleanup all ; \
		fi ; \
	fi

clean-ruby-rvm:
	rm -rf rvm/

clean-deps:
	rm -rf vendor/ .bundle

docker:
	. $(PWD)/envrc && \
	docker run -d --rm -v "$(PWD)":/usr/src/app -p "4000:4000" starefossen/github-pages
