# DevOps Practices

DevOps encompasses engineering, business, and cultural practices. These practices should result in measurably more stable products that can be delivered quicker than more traditional methods.

---

## Continuous Feedback & Improvement
A focus on feedback and improvement is a key aspect in DevOps practices. This cornerstone of DevOps should be practiced early on with development teams, and later with other teams related to a product. This is referred to as **DevOps [Kaizen][5]**. \[[1]\] \[[2]\] \[[4]\]

### Monitoring the Metrics of DevOps
In order to continuously improve the organization, one must track how well it's doing at its methods and processes by [using metrics to monitor the processes][3]. Some common metrics to track include number of new incidents, Mean Time to Detect (MTTD), Mean Time to Repair/Resolve (MTTR), [Lead time], deployment frequency, and other process metrics, like the use of an [Andon cord].

### Continuous Integration, Build, Test, & Delivery
Also known as CI/CD because of how often both of these different systems are run in parallel. This is often what people imagine when they think "DevOps", even though it's more of a software development practice that's been carried into DevOps.

See the [Continuous Integration & Delivery](./ci-cd.md) page for more detail.

### Blameless Postmortems
[Blameless Postmortems at Etsy][7].

### Customer Feedback

### Automated release management
[Release management features of XebiaLabs' XL-Release][6].

---

## Immutable, version-controlled state
Immutability in DevOps refers to the idea that once we create something new, it should never be changed; instead, something new should replace it. In addition, each of these creations should be versioned, so we can easily manage them. This is an incredibly powerful paradigm that solves many old problems, such as unexpected errors from tiny changes over time, and simplifying upgrade, rollback, and failover.

[A paper from 2002](http://www.infrastructures.org/papers/turing/turing.html) explains why this is true, and why we should adopt this practice.

### Automated provisioning of infrastructure
Using [Infrastructure as Code](./infrastructure.md), the provision of new infrastructure should happen automatically as it is needed. This helps drive down cost, gives the ability to scale with dynamic workloads, reduces human error, and speeds up development.

### Congruent environments
Whenever possible, if multiple people or products use a particular kind of environment, they should be congruent (meaning always the same). For example, it should be possible to test and deploy new products directly into the environment used for production services. Another example is enabling everyone to use the exact same development environment, with the same tools, versions, and infrastructure. This congruence reduces conflicts over incompatibility, and speeds development.

---

## Service requirements
In order to run services properly, DevOps has a series of [typical requirements for production services](./services.md).

### Self-service configuration
Whenever possible, users (such as developers) should be able to build and control much of the system themselves. This often includes being able to stand up new infrastructure, build new deployment pipelines, and view monitoring and metrics of running services.

---

## Agile software development
As DevOps members develop their own software and products, they should ideally follow Agile methods. Frequent integration, testing, and deployment of code will result in faster, less error-prone software.


[1]: https://biztechmagazine.com/article/2016/06/kaizen-and-continuous-improvement-through-devops
[2]: https://www.slideshare.net/dev2ops/dev-ops-kaizen-damon-edwards
[3]: https://biztechmagazine.com/article/2016/06/metrics-businesses-need-know-adopting-devops
[4]: https://www.developer.com/mgmt/a-kaizen-approach-for-devops-how-to-help-teams-find-and-fix-their-own-problems.html
[5]: https://en.wikipedia.org/wiki/Kaizen
[6]: https://xebialabs.com/products/xl-release/features/
[7]: https://codeascraft.com/2012/05/22/blameless-postmortems/
