# How to Use This Page

This is where we can keep & organize all the work to do on the site.

If you have a new issue, something you're working on, feature request, bug, whatever, feel free to pop it in here. If you don't know what category it should be in, put it in "Incoming". If you have a really good feeling that your new item should be in a new category, add it. If you're not sure, ask.

Anyone can grab any of these and start working on them. If you start work on something and it'll take longer than a day to finish, just edit it with "WIP", and maybe reference a PR or Issue if you have one. When you finish something, mark it off with an [x].

# Categories of Work

## Incoming
---
 - [ ] Mock up some kind of Git pre/post-push hook to try a build first.
   - [ ] Figure out what to do with Gemfile.lock

## Content
---
 - [ ] Go through and find content which is not linked anywhere (./practices/monitoring\_\* ??)
 - [ ] Start importing and sorting through all the DevOps bookmarks I have
 - [ ] Get a site crawler to find broken links
 - [ ] Go through content and update unlinked [Bracketed] text, possibly automate
 - [ ] Start working on an "implementing devops" category/page thing
   - [ ] Write up the Chef DevOps Kungfu sections (https://www.youtube.com/watch?v=\_DEToXsgrPc, http://chef.github.io/devops-kungfu/#/40)

## Navigation
---
 - [x] Add a major navigation entry to \_data
 - [x] Add some elements to pages to automatically link to the next major nav entry at top/bottom of pages
   - [x] To implement: add front matter that declares previous/next page? Or look into how Jekyll handles it
 - [x] Add major section navigation to right sidebar
 - [ ] Wrap more of sidebar with &lt;nav&gt; tags
 - [ ] Explicitly list all Wiki content below a major section in side-bar (so people know to find iac.md, services.md, etc)
 - [ ] Add a border around sidebar nav stuff
 - [ ] Add a break-out/selectable nav menu with _all_ content (loaded from \_data ?)

## Bikeshedding
---
 - [ ] Add a line-rule after page content's &lt;h1&gt; heading (change CSS)
 - [ ] Add padding to description of tools
 - [ ] Fix toc.html to stop breaking on bad page indentation
 - [ ] Fix 'services.md' Page Sections indentation
 - [ ] In 'Page Sections', add a line break after first &lt;h1&gt; category
 - [ ] Fix page section ordering (currently dots, want numbers)
 - [ ] Go through and find weird, corrupted characters in content, could be utf?

