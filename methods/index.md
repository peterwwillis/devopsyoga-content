# Methods

Though DevOps shares some values & principles with Agile, its methods actually differ quite a bit. DevOps does not specify any particular Agile methodology. In fact, some Agile methods can be incompatible with DevOps work.

## Common Patterns

Several patterns of implementing DevOps practices are common in the industry.

### [Systems Thinking][2]

Patterns of applying DevOps principles to yield high performance outcomes. Also known as "left to right" thinking or "the pipeline".

Three principles:
1. Create increased "velocity" by accelerating each of the process components in the pipeline.
  - Use Docker and/or Vagrant to speed developer workflow
  - Use [Continuous Integration] to speed build flow
  - Use Blue/Green [Deployment] models to speed application deployment
  - Reduce variation in deployments by using [immutable delivery]
2. Decrease "variation" by eliminating wasteful or time consuming sub processes in the pipeline.
3. Elevate the processes by bounded context (isolating the functionality) therefore better visualizing and understanding the global flow (i.e., seeing the system).

### [Amplifying Feedback Loops][3]

Amplifying and shortening feedback loops such that corrections can be made fast and continuously. Also known as the "right to left" flow.

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

### [Continuous Learning][4]

Using [Kaizen][5] to build knowledge and learn experimentally. Not unlike the retrospective after a scrum sprint. The general idea here is to experiment with how you do something, learn from it quickly, and then do it better. It's a very Lean/Agile way of moving development forward. By leveraging the past two methods, continuous learning is even faster.

Ideally, as lessons are learned, they would be contributed back to an organizational knowledge base. In the absence of such a thing, you can just contribute what you've learned to this Wiki :-) (but no proprietary information, please)



## Not Agile-specific
DevOps does *not* require values specific to software development, as you can take any product and apply DevOps to it. As an example, **the following values are not required** by DevOps, and at times may be counter to it:

 * Rapid, frequent deployment
 * Short sprints of work with working products at the end
 * Every member of the team can do every other member's job
 * Daily stand-ups of work completed, blockers found
 * Informal design decisions
 * Lack of documentation

The following methods are suggested to be applied in DevOps, in addition to Agile (or other) methods:

### Constant inter-team communication
DevOps requires that development and operations coordinate their work on a regular basis. The reason is due to the specialized knowledge of how the application works that must be used by operations to keep the product working smoothly. The communication can be impersonal or official, but most of all it should be frequent, so knowledge is disseminated in time to respond to changes quickly.

### Reliance on specialized knowledge
Not all aspects of DevOps will be able to be fulfilled by a single team. Sometimes a particular team will specialize in functionality that DevOps needs, such as monitoring & metrics, CI/CD, compute & storage, networking, etc. In many cases it is perfectly acceptable for DevOps to rely on outside teams to help fulfill the purpose of delivering and maintaining quality software products.

### Formal documentation
The building, running, and maintaining of software products often requires more strict coordination of work and general knowledge. To properly design the system, knowledge of how the application works must be documented. To correct the application under different failure conditions, run-books must be recorded, to later become auto-healing automation. Monitoring an application also requires knowledge of how to test its behavior. If documentation does not exist, it can be very difficult to keep an application operating nominally.

### Adapting to the product [team]
Often, DevOps members are allocated vertically throughout horizontal product teams. Since they are working on different products, they may be developed in different ways, and so the DevOps members should align themselves with the particular methods of the product team they're working with. It's not unusual for one DevOps member to support multiple products using both Scrum and Waterfall, and to use different tools to accomplish similar tasks.

### Schedules aligned with project goals
Short sprints don't always align with DevOps goals. Many tasks can't be completed in the way software tasks are (using Scrum, for example). Instead, schedules are set based on the goal, which may be short-term or long-term, or which may be defined by another team's own deadlines. Compared to software developers, DevOps members may have tasks with higher priority introduced at random, putting timelines in constant flux. The work completed first should always be the most urgent to keep a product operating smoothly, so tasks of lesser importance may have missed deadlines if they are not realistically set. For example, an unexpected maintenance window may take precedence over delivering a feature on time, or automation to solve a recurring problem may be more urgent than building new functionality.

### Quality automation
In order to increase the reliability of products and to speed their deployment, automation should be applied whenever possible. But improperly applied automation can end up becoming inefficient compared to what a human can accomplish. So the quality of automation applied should be high, or else a human should intervene until automation can be improved. The availability and quality of the product being used by the end-user is the highest goal, and not simply the use of automation for automation's sake.


[1]: https://www.bmc.com/blogs/devops-vs-agile-whats-the-difference-and-how-are-they-related/
[2]: https://blog.docker.com/2015/05/docker-three-ways-devops/
[3]: https://blog.docker.com/2015/06/docker-three-ways-devops-2/
[4]: https://blog.docker.com/2015/07/docker-three-ways-devops-3/
[5]: https://en.wikipedia.org/wiki/Kaizen
