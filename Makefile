
# Make sure to create a file called 'envrc' which contains the following 
# entries:
#
#   PAGES_REPO_NWO=<username>/<reponame>
#   JEKYLL_GITHUB_TOKEN=<a github token with public repo scope>

all: update-deps jekyll-serve

update-deps:
	bundle update github-pages

jekyll-serve: envrc
	jekyll serve
