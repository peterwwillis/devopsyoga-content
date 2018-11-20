# What is DevOps?

If you search for "What is DevOps?", you will find hundreds of pages that try to explain the concept. However, there is [broad acceptance of what DevOps means throughout the industry](https://devops.com/surprise-broad-agreement-on-the-definition-of-devops/).

The goal of DevOps is to improve the quality of software while speeding up its delivery and operation. The way this is achieved is through a specific culture, a set of processes and tools, working closely with other teams, and constantly working to review and improve all of these aspects to reduce waste and increase quality, and thus business value.

Another way to think of DevOps is as agile methods, applied throughout an organization, to help a software product succeed.

Implementing DevOps is a big undertaking, but not because the tools or processes are complicated. The biggest challenge is in changing everyone's mindset in order to become comfortable with new ways to work together.[citation needed]


## What is DevOps Culture?
At its core, DevOps culture is inspired by the Agile Manifesto. DevOps was even sometimes referred to as "agile infrastructure" [citation needed]. But as DevOps encompasses many different roles and responsibilities, it doesn't strictly follow only agile methods [citation needed].


### Lack of Silos
<!-- TODO: may want to break out into its own section -->
Most companies tend to organize their employees into teams based on common functions. Those teams can end up being siloed from one another, making progress difficult when it requires working across teams. In a DevOps culture, all teams that work on a product should be closely integrated.

One example is in the way problems are addressed. In a traditional organization, if a software development team needed some infrastructure allocated, they may have to go through a time-consuming, complicated process. They may require multiple levels of approval, and then need to wait on someone to provide them their resources.

In a DevOps culture, the teams work together to find the least painful, most efficient way to accomplish the intended goals of both groups. This would ideally involve reviewing these requests often, removing approvals where they make no sense, and automating the building of infrastructure.

### Integrated Teams
<!-- TODO: may want to break into section on integrating teams -->
A piece of software can't run in a vacuum. That is to say, eventually someone is going to be running that software, and it won't be the developers. In order to prevent problems down the road, it's best to have both software developers and operations engineers working on the same team.

When some infrastructure needs to be prepared or changed, the conversation is already happening as the developers are beginning to write their code. The infrastructure changes can be tracked and discussed in a team scrum while development is taking place.

Another aspect of DevOps is how one team can influence the other to improve their processes. If operations engineers are using DevOps best practices in their own work, they can help software developers modify their own work to be aligned with the same process.

Even more teams can be integrated into the software development process. Quality assurance and software teams can be brought into the software development, and both learn how they will need to use or examine the software, and provide valuable feedback to improve the software at earlier stages.

### Agile Culture
<!-- TODO: may want to break out into its own section -->
The Agile manifesto emphasizes "*individuals and interactions* over *processes and tools*.

One example of this may have been the Mars Climate Orbiter. The multi-million-dollar project burned up in Mars' atmosphere due to an error made by one team that was then not corrected by a different team. The error was actually noticed, but was never fixed, partly due to over-reliance on formal process.[[1]] Quote from Wikipedia:

    The discrepancy between calculated and measured position, resulting in the discrepancy
    between desired and actual orbit insertion altitude, had been noticed earlier by at
    least two navigators, whose concerns were dismissed because they "did not follow the
    rules about filling out [the] form to document their concerns". A meeting of
    trajectory software engineers, trajectory software operators (navigators), propulsion
    engineers and managers, was convened to consider the possibility of executing
    Trajectory Correction Maneuver-5, which was in the schedule. Attendees of the meeting
    recall an agreement to conduct TCM-5, but it was ultimately not done.

Ultimately, it's clear from the results that the different organizations involved (Lockeed Martin, JPL, and NASA) in the product launch were not tightly integrated, and communication and decision-making was bogged down. Over-reliance on what people hoped would happen, combined with a lack of insight, and mis-matching work processes, led ultimately to a costly mistake.

Similar situations happen to products all over the world, all the time. An agile culture won't solve these problems, but it will facilitate teamwork, which often leads to better outcomes.


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
