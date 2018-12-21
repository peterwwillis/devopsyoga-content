# Continuous Integration & Delivery


These two subjects, often referred to as "CI-CD", are similar yet separate concerns. They often use the same tools to accomplish different tasks.

## Continuous Integration

The general idea of [Continuous Integration] is to use quality control before code changes are accepted into the main code tree. As long as proper testing is done, changes to code can be accepted more quickly. As the quality of the tests improve, so does trust that the code changes will work. This improves code quality, which improves reliability.

The principle behind this is simple: the longer a change takes it to get from a developer's working copy into the main code branch, the more time there is for conflicting code to have been merged by someone else. By shortening the time to integrate code into the main line, there are less chances for conflicting changes. Adding tests for the code, and verifying them before merging, increases the trust that these frequent commits will produce working software.

The result of [Continuous Integration] should be that every successful commit begins a build process, and that build process should have sufficient tests to ensure the software works properly. Integration commits should happen very frequently in order to obtain the best results.

Though [Continuous Integration] comes from [Extreme Programming], it is not required to use [Test Driven Development] to use [Continuous Integration]. Instead one can merely run a server which runs all software tests before a piece of code is accepted into the mainline code tree. Since DevOps also practices [Infrastructure as Code], this means infrastructure changes also require tests to pass before they are accepted. Because of this, regression testing is very important, or important changes may not function.


### [CI Common Practices]
 - Maintain a code repository
 - Automate the build
 - Make the build self-testing
 - Everyone commits to the baseline every day
 - Every commit (to baseline) should be built
 - Keep the build fast
 - Test in a clone of the production environment
 - Make it easy to get the latest deliverables
 - Everyone can see the results of the latest build
 - Automate deployment

### CI Notes
 - Beware large monolithic projects. The bigger they get, the more tests there are, and the harder it is to have a successful build as different parts of it constantly change. Segment your project or split it off if it's getting too difficult to keep the builds clean.
 - Use [Multi-stage Continuous Integration] to better manage large projects. 


## Continuous Delivery / Deployment
You should probably just [read this book](https://continuousdelivery.com/).

### Immutable Delivery
CD should, ideally, take a page out of [Infrastructure as Code]'s playbook, and implement **immutable delivery**. This is when you deploy artifacts that are immutable, such as Docker containers with built application artifacts. If all of the components throughout a delivery pipeline are version-controlled and immutable, you can deliver reliable, immutable software to any environment.

[Continuous Integration]: https://en.wikipedia.org/wiki/Continuous_integration
[CI Common Practices]: https://en.wikipedia.org/wiki/Continuous_integration#Common_practices
[Multi-stage Continuous Integration]: https://en.wikipedia.org/wiki/Multi-stage_continuous_integration
[Infrastructure as Code]: ./infrastructure.md
[Deployment]: ./deployment.md
[1]: https://www.nginx.com/blog/devops-and-immutable-delivery/
