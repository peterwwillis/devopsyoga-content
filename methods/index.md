# DevOps Methods

Though DevOps shares some values & principles with Agile, its methods actually differ quite a bit. DevOps does not specify any particular Agile methodology. In fact, some Agile methods can be incompatible with DevOps work.

---

## Common Patterns

Several patterns of implementing DevOps practices are common in the industry.

---

### The Three Ways

[The Three ways][24] are principles that many DevOps patterns are based on, and are referred to in The DevOps Handbook and The Phoenix Project.

#### The first way: [Systems Thinking][2]

From Gene Kim:

> The First Way emphasizes the performance of the entire system, as opposed to the performance of a specific silo of work or department ? this as can be as large a division (e.g., Development or IT Operations) or as small as an individual contributor (e.g., a developer, system administrator).
> 
> The focus is on all business value streams that are enabled by IT. In other words, it begins when requirements are identified (e.g., by the business or IT), are built in Development, and then transitioned into IT Operations, where the value is then delivered to the customer as a form of a service.
> 
> The outcomes of putting the First Way into practice include never passing a known defect to downstream work centers, never allowing local optimization to create global degradation, always seeking to increase flow, and always seeking to achieve profound understanding of the system (as per Deming).

Summarised: Patterns of applying DevOps principles to yield high performance outcomes. Also known as "left to right" thinking or "the pipeline".

Three principles:
1. Create increased "velocity" by accelerating each of the process components in the pipeline.
  - Use Docker and/or Vagrant to speed developer workflow
  - Use [Continuous Integration] to speed build flow
  - Use Blue/Green [Deployment] models to speed application deployment
  - Reduce variation in deployments by using [immutable delivery]
2. Decrease "variation" by eliminating wasteful or time consuming sub processes in the pipeline.
3. Elevate the processes by bounded context (isolating the functionality) therefore better visualizing and understanding the global flow (i.e., seeing the system).

#### The second way: [Amplifying Feedback Loops][3]

From Gene Kim:

> The Second Way is about creating the right to left feedback loops. The goal of almost any process improvement initiative is to shorten and amplify feedback loops so necessary corrections can be continually made.
> 
> The outcomes of the Second Way include understanding and responding to all customers, internal and external, shortening and amplifying all feedback loops, and embedding knowledge where we need it.

Summarised: Amplifying and shortening feedback loops such that corrections can be made fast and continuously. Also known as the "right to left" flow.

Three principles:
1. Velocity of a correction in the flow is essential.
  - Detect defects fast
  - Correct defects quickly
  - Must work in all flow directions
2. Complexity of the infrastructure where the defect has been identified needs to be simpler so that it requires less time to detect.
  - Reduce complexity of software artifacts, infrastructure
  - Create immutable artifacts early on and make sure their use does not vary throughout a pipeline
3. Software artifacts need to be elevated and bounded (i.e., visual) to their source (e.g., source code, source code repository) in order to be able to decrease the overall Lead Time of a service delivered.
  - Add metadata to built artifacts (e.g. Docker containers) to expose what it is, where it came from, how to monitor/maintain it, etc

#### The third way: [Culture of Continuous Learning and Experimentation][4]

From Gene Kim:
> The Third Way is about creating a culture that fosters two things: continual experimentation, taking risks and learning from failure; and understanding that repetition and practice is the prerequisite to mastery.
> 
> We need both of these equally. Experimentation and taking risks are what ensures that we keep pushing to improve, even if it means going deeper into the danger zone than we?ve ever gone. And we need mastery of the skills that can help us retreat out of the danger zone when we?ve gone too far.
> 
> The outcomes of the Third Way include allocating time for the improvement of daily work, creating rituals that reward the team for taking risks, and introducing faults into the system to increase resilience.

Summarized: Using [Kaizen][5] to build knowledge and learn experimentally. Not unlike the retrospective after a scrum sprint. The general idea here is to experiment with how you do something, learn from it quickly, and then do it better. It's a very Lean/Agile way of moving development forward. By leveraging the past two methods, continuous learning is even faster.

Ideally, as lessons are learned, they would be contributed back to an organizational knowledge base. In the absence of such a thing, you can just contribute what you've learned to this Wiki :-)

---

### Patrick Debois' [The Four Areas][21]

#### Extend Delivery to Production
 - This is where dev and ops collaborate to improve anything on delivering the project to production.
#### Extend Operation to Project
 - All information from production is radiated back to the project.
#### Embed Project(Dev) into Operations
 - When the project takes co-ownership of everything that happens in production.
#### Embed Production(Ops) into Project
 - When operations are involved from the beginning of the project.


---

### Lean Manufacturing-inspired methods

Some methods of DevOps come from the world of Lean Manufacturing and Lean Startups.

#### Andon cords
This is more interperative, but similar to Toyota's TPS system and its Andon cord, DevOps organizations implement their own forms of Andon cords. [This article](https://itrevolution.com/kata/) explains a bit.

#### [Autonomation][8]
Automation that detects an error and stops a process so a human can intervene. This can include CI/CD processes that stop a deployment when a test fails and waits for a user to fix the test. Another example is [ChatOps][22], using a chat bot to interact with automated tools with [a variety of uses][23]. This is considered pre-automation, as opposed to full-automation, which is where a process resolves its own problems.

#### Value Stream Mapping
VSM is a useful way to visualize the entire chain of events involved with a product, from the first idea to a delivered product. [The intent][10] is to identify what parts provide value, and what parts are merely wasteful.

This may start with [identifying the type of value stream][11], then [identifying the teams that support it, and documenting the work done][12].

One example of making a value stream map [is here][14], and [here][15] are some tips.


---

### Veering away from Agile
DevOps does *not* require values specific to software development, as you can take any product and apply DevOps to it.

For example, the following values **are not required** by DevOps, and at times may be counter to it:

 * Rapid, frequent deployment
 * Short sprints of work with working products at the end
 * Every member of the team can do every other member's job
 * Daily stand-ups of work completed, blockers found
 * Informal design decisions
 * Lack of documentation

In contrast to typical Agile methods, the following are suggested to be applied in DevOps, in addition to Agile (or other) methods:

#### Constant inter-team communication
DevOps requires that development and operations coordinate their work on a regular basis. The reason is due to the specialized knowledge of how the application works that must be used by operations to keep the product working smoothly.

The communication can be impersonal or official, but most of all it should be frequent, so knowledge is disseminated in time to respond to changes quickly.

#### Reliance on specialized knowledge
Not all aspects of DevOps will be able to be fulfilled by a single team. Sometimes a particular team will specialize in functionality that DevOps needs, such as monitoring & metrics, CI/CD, compute & storage, networking, etc.

In many cases it is perfectly acceptable for DevOps to rely on outside teams to help fulfill the purpose of delivering and maintaining quality software products. These teams should be accessible to all the other teams and work closely with them.

#### Formal documentation
Building, running, and maintaining a product often requires more strict coordination of work and product knowledge. To properly design the system, knowledge of how the application works must be documented.

To correct the application under different failure conditions, run-books must be recorded, to later become auto-healing automation. Monitoring an application also requires knowledge of how to test its behavior. If documentation does not exist, it can be very difficult to keep an application operating nominally.

#### Adapting to the product [team]
Often, DevOps members are allocated vertically throughout horizontal product teams. Different products may need to be developed in different ways, so the DevOps members working on them should align themselves with each product team's particular methods.

 It's not unusual for one DevOps member to support multiple products using both Scrum and Waterfall, and to use different tools to accomplish similar tasks.

#### Schedules aligned with project goals
Short sprints don't always align with DevOps goals. Many tasks can't be completed in the way software tasks are (using Scrum, for example). Instead, schedules are set based on the goal, which may be short-term or long-term, or which may be defined by another team's own deadlines.

Compared to software developers, DevOps members may have tasks with higher priority introduced at random, putting timelines in constant flux. The work completed first should always be the most urgent to keep a product operating smoothly, so tasks of lesser importance may have missed deadlines if they are not realistically set. For example, an unexpected maintenance window may take precedence over delivering a feature on time, or automation to solve a recurring problem may be more urgent than building new functionality.

#### Shift Left
This refers to shifting aspects normally on the "right side" of the product lifecycle (design-> build-> test-> operate) [to the left side, earlier in the development process][17]. More generally, it means implementing operational considerations earlier in the development process.

This includes earlier implementation of monitoring/metrics, automated testing, continuous integration and delivery, and [security analysis][18], to identify problems before they reach production. A report by IBM found that fixing these problems during requirements & design is [about 100x less expensive][19] than fixing it in production.

Some of the processes of "shift left" include:
 * Demand Planning
 * Static Testing
 * A Unified Test Strategy
 * Risk Based Analysis

One example of "Shift Left" that Microsoft uses is for as much testing to be done in a Pull Request as possible, during code review. 

---

## Beginning to implement DevOps Methods
[This Link][7] provides some guidance on how to begin implementing the methods.

### On [Team Organization][13]
Often there is a tendency to produce functionally-oriented team structure (vertically-aligned organizational structure - think silos of sysadmins, network admins, dbadmins, etc) to minimize and centralize the amount of technical specialization. But this can often lead to long lead times for finishing tasks, which adds delays.

Instead, by using market-oriented teams (horizontally-aligned - think product teams of testing, securing, deployment, support, etc), team members are more available to address tasks specific to a product as the task is needed to be solved. This provides more of a Lean-style of pulling new work items when they are needed, rather having to push work somewhere and wait for it to be completed. This of course also depends on a high amount of independence, cross-functional skills, and automation.

These teams work better with reliable estimates of expected lead time for new tasks. Tracking metrics of work completion (as part of a value stream map above, for example) can help make these workflows more efficient.

### Incremental Adoption
For mid to large size organizations, some recommend [an incremental approach][16] to adopting DevOps, using six steps:
1. Select a suitable, small-scale application
2. Consider short and mid-length solutions
3. Evaluate tools that both fit the enterprise and the project
4. Develop a pre-production proof of concept
5. Pilot the proof of concept into production
6. Iterate on the pilot

### Assessments
[Microsoft DevOps Assessment][20]


[1]: https://www.bmc.com/blogs/devops-vs-agile-whats-the-difference-and-how-are-they-related/
[2]: https://blog.docker.com/2015/05/docker-three-ways-devops/
[3]: https://blog.docker.com/2015/06/docker-three-ways-devops-2/
[4]: https://blog.docker.com/2015/07/docker-three-ways-devops-3/
[5]: https://en.wikipedia.org/wiki/Kaizen
[6]: https://caylent.com/devops-handbook-part-1-the-three-ways-cont/
[7]: https://caylent.com/devops-handbook-part-2-devops-methodology/
[8]: https://en.wikipedia.org/wiki/Autonomation
[9]: https://caylent.com/devops-handbook-part-1-the-three-ways-2/
[10]: https://www.enov8.com/blog/devops-void-value-stream-mapping/
[11]: https://itrevolution.com/starting-devops-value-stream/
[12]: https://itrevolution.com/improve-flow-devops-value-stream/
[13]: https://itrevolution.com/conways-law/
[14]: https://www.xeridia.co.uk/blog/how-use-value-stream-mapping-devops-environment
[15]: https://dzone.com/articles/value-stream-mapping-and-devops
[16]: http://cdn.inedo.com/documents/Inedo-Incremental-DevOps.pdf
[17]: https://www.quali.com/blog/what-do-devops-organizations-need-to-do-to-shift-left/
[18]: https://www.itbusinessedge.com/articles/the-shift-left-approach-to-devops-security.html
[19]: https://www.bmc.com/blogs/what-is-shift-left-shift-left-testing-explained/
[20]: https://www.devopsassessment.net/
[21]: http://www.jedi.be/blog/2012/05/12/codifying-devops-area-practices/
[22]: https://www.pagerduty.com/blog/what-is-chatops/
[23]: https://techbeacon.com/chatops-essential-guide-basics-benefits-challenges
[24]: https://itrevolution.com/the-three-ways-principles-underpinning-devops/
