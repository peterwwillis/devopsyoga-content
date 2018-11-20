# Writing End User Documentation

### Who is this documentation for?
   - anyone who isn't deeply familiar with your work
   - people who need to learn how to access & use something you provide

### Why is it important?
   - quickly consuming a service reduces toil, or muda
     - _toil_:
       "manual, repetitive, automatable, tactical, devoid of enduring value,
        and that scales linearly as a service grows"
     - _muda_: waste. in this case:
       - motion muda, or waste of unnecessary downtime
       - waiting muda
       - confusion muda
   - excess time learning means less time doing
   - lean principles
     - eliminate waste
     - amplify learning
     - deliver as fast as possible
     - empower the team / individual agency
     - improve integrity
   - iterating over documents improves quality of resulting work & processes
   - actually painful to have to work hard to learn simple things
   - creating good docs exposes weaknesses in on-boarding


### Types of docs

 * ##### FAQs
   - first docs a user should see
   - read your Slack chat and email and write down every question a user asks
   - put the question in your FAQ
   - ask yourself what you need to use the product
     - what information do i need about my account or organization
     - what account access do i need
     - what network access do i need
     - what information does the user need to provide to you
     - what parts of the product are non-obvious, non-intuitive or hidden
     - what would a five year old need to know to use your product?
   - if longer than a few pages, split up into multiple FAQs

 * ##### quick-start docs
   - second docs a user should see
   - basically a runbook
   - learn by doing
   - should be 90% commands to run
   - minimize prerequisites as much as possible

 * ##### on-boarding workflows
   - third docs a user should see
   - assume the user knows nothing and has nothing set up
   - provide steps, screenshots, videos
   - specify prerequisites
     - provide all prerequisites to the user
     - provide a link that explains how to set each prerequiste up
   - actually sit with user and go through onboarding
     - document the steps that have problems
     - fix them manually for the user
     - create a ticket/issue to go back later and fix the problem step
     - commit documentation to version control

 * ##### on-boarding workflows - part 2
   - break up a section to keep it from getting too long! keep it readable
   - onboarding can take days/weeks
   - if a user has problems:
     - create a ticket to track a user's onboarding
     - document in the ticket the problems found by user and solutions provided
     - ask user if their problem is solved before closing ticket
     - include chat logs + email in ticket
     - add tags to the ticket: 'onboarding, faq'
     - add the problem+solution to FAQ
       - can make an independent page for issue, link to it from FAQ question

 * ##### technical docs
   - last docs a user should see
   - used for:
     - building the fine details/implementation
     - troubleshooting
   - organize into categories & sections
   - explain everything someone would need to troubleshoot their own problem
   - one line of code may need four lines of documentation
   - if a component such as a data type/format is used,
     provide link to the format's docs


### Organization

 * ##### organizing information in a doc
   - put prerequisites at the top of each document
   - shuffle where information lives in the doc as you edit it

 * ##### organizing docs
   - hierarchy is useful
   - have a TOC (see below: "table of contents") in the root that includes
     all sub-docs

 * ##### linking docs
   - link pages and major sections from your table of contents
   - link to other pages/docs for prerequisites covered in other parts of docs



## Writing the docs


### Structure

 * ##### table of contents
   - create a TOC hierarchy for each doc
     (see above: "Organization" / "organizing docs")
   - TOC at the base of all docs; the more comprehensive the better

 * ##### the document content

 * ##### examples
   - just show the code/config/commands
   - provide one config file with all config options and defaults
   - provide examples & configs for different use cases
   - commands that you can actually run
   - highlight the example with a different background, font style, size

 * ##### demos
   - in lieu of documentation, a __BRIEF__ recorded demo is appropriate
   - helps show flow of steps in a UI
   - provide in a format that can be paused, rather than as a .gif

 * ##### linked guides
   - in lieu of documentation, a concise blog entry can be helpful
   - will not replace the experience of the user for your product

 * ##### index
   - keyword tags
   - list of words/phrases/concepts and link to each page

 * ##### glossary
   - provide in addition to index
   - put all acronyms in glossary
   - put any words/phrases which may have multiple interpretations


### Editing

 * ##### formats
   - Markdown is simple, widely available, can be converted to many formats
   - ASCII is the most compatible thing in the world
     - Monospace font size 12

 * ##### versioning
   - version control and collaboration
     - git
       - make sure the repo is public
       - allow people to submit PRs
       - put the link to the docs repo in the doc!
     - wiki

 * ##### making it readable / skimmable
   - break document up into multiple heading sizes/styles
   - indent each part of document
   - break up steps with bulleted or numbered lists
   - when necessary, number each section and sub-section


### After the docs are written

 * ##### feedback loop
   - provide _easy_ mechanism to allow users to give feedback on the docs, including
     - the author
     - the team
     - slack, email, ticket queue
   - incorporate feedback into docs


### Tips

 * ##### help the user get help
   - always provide the user a way to find help if something goes wrong
   - provide links to support outside the scope of your team
     - password problem? provide links to password reset tools
     - network connectivity problem? provide link to network team support
     - reduces muda/toil by not requiring user to find these elsewhere

 * ##### don't:
   - assume they have accounts, an environment, firewall access, etc
   - assume they have used X technology before
     - provide enough simple steps that somebody with zero knowledge can get
       the thing up and running

 * ##### do:
   - assume they just joined the company and have no idea where anything is

