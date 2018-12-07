# Continuous Integration & Delivery

These two subjects, often referred to as "CI-CD", are similar yet separate concerns. They often use the same tools to accomplish different tasks.

## Continuous Integration

The general idea of [Continuous Integration] is to add quality control to changes to source code before it is accepted into the main code tree. As long as proper testing is done, changes to code can be accepted more quickly. As the quality of the tests improve, so does the code, and improved code quality improves the reliability of the result.

The ideas behind [Continuous Integration] come from the [Extreme Programming] software development method. In that method, [Test Driven Development] would require software tests to be written and pass before the code in question would be accepted. Once the code is already passing tests, it can be "integrated" into the mainline code tree, potentially with [Feature Flags] to prevent them being used immediately.

It is not required to use [Test Driven Development] to use [Continuous Integration]. Instead one can merely run a server which runs all software tests before a piece of code is accepted into the mainline code tree. Since DevOps also practices [Infrastructure as Code], this means even changing infrastructure requires a series of tests to pass before changes can be integrated into the mainline tree.

If working code changes are introduced back into the mainline tree frequently, they will have less drastic changes, and cause less problems with other code changes. If code changes are merged in after long periods of development, more chances for conflict occur.

The result of [Continuous Integration] should be that every successful commit begins a build process, and that build process should have sufficient tests to ensure the softwware works properly.

### [CI Best Practices]
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


## Continuous Delivery


[Continuous Integration]: https://en.wikipedia.org/wiki/Continuous_integration
[CI Best Practices]: https://en.wikipedia.org/wiki/Continuous_integration#Best_practices
[Multi-stage Continuous Integration]: https://en.wikipedia.org/wiki/Multi-stage_continuous_integration
