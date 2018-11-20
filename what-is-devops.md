# What is DevOps?

If you search for "What is DevOps?", you will find hundreds of pages that try to explain the concept. However, there is [broad acceptance of what DevOps means throughout the industry](https://devops.com/surprise-broad-agreement-on-the-definition-of-devops/).

The goal of DevOps is to improve the quality of software while speeding up its delivery and operation. The way this is achieved is through a specific culture, a set of processes and tools, working closely with other teams, and constantly working to review and improve all of these aspects to reduce waste and increase quality, and thus business value.

Another way to think of DevOps is as agile methods, applied throughout an organization, to help a software product succeed.

Implementing DevOps is a big undertaking, but not because the tools or processes are complicated. The biggest challenge is in changing everyone's mindset in order to become comfortable with new ways to work together.[citation needed]

## [What is DevOps Culture?](./devops-culture.md)


## What are DevOps Practices?
At its core, DevOps is just a collection of engineering, business, and cultural practices. When fully implemented, those practices should result in measurably more stable products that can be delivered quicker than using more traditional methods.
<!-- TODO: link to DevOps Practices from here -->

### Agile software development
The development and production of software should follow an Agile software development lifecycle. Frequent integration and deployment of code should result in faster and less error-prone software testing and delivery. Focus should be on testing and deploying small amounts of work frequently in short cycles, rather than trying to ship perfect code over long development cycles.
<!-- TODO: link to agile software development docs here -->

### Continuously improving processes
In every aspect of a product, there should be a focus on repetition and improvement. Frequent repetition of process allows the process not to become stale, and for inefficiencies to be caught early. A review of any inefficiency found should result in an improvement to the process. Examples would be continous integration and testing, but also things like failover recovery, customer service feedback of critical issues, etc.
<!-- TODO: link to continuously changing processes here -->

### Immutable, version-controlled state
Wherever possible, a process should take as input a version controlled object, and produce a version controlled artifact. These artifacts should be immutable, and as little state should change as possible in the use of these artifacts. This prevents changes from causing unexpected errors, and allows for simple recovery in the event of errors.
<!-- TODO: link to philosophies here, such as immutability -->

[1]: https://spectrum.ieee.org/aerospace/robotic-exploration/why-the-mars-probe-went-off-course
