<p>This page attempts to document some of the values & principles behind DevOps. These are important concepts to understand, but they're also not enough to get started. To begin putting them into practice, skip to the next sections.</p> <br />

# Values
Values are a set of beliefs, and they vary from culture to culture. DevOps values start with Agile and Lean values, and then add some of their own.

## Agile Values
DevOps and Agile have [things in common, and differences][2]. DevOps evolved while Agile was already being widely practiced (and as a result, it was originally called "Agile Infrastructure"). Because of this, it inheritied Agile's 4 values:

 * **Individuals and Interactions over Processes and Tools**
   - People are the cause of all business needs, and drive all development work. If processes and tools are prioritized over the human element, the team will soon be less responsive to change and be ineffective at providing for customer needs. For example, communication is usually easier when done directly between people, and more difficult when done through a tool or process.

 * **Working software over comprehensive documentation**
   - You can create a fully-documented plan to build some software, or you can create a Minimum Viable Product. The documentation may not reflect the real-world operation of the software, but the MVP is it's own documentation. User Stories are a leaner form of a plan or documentation that a developer can use to build an MVP, faster than going though multiple rounds of formal documentation, planning, and approvals.

 * **Customer collaboration over contract negotiation**
   - This emphasizes collaboration between the customer and development of the product, rather than negotiating the terms of a contract and disappearing. End users should see demos regularly.

 * **Responding to change over following a plan**
   - When projects refuse to change because they are against a pre-defined plan, change later becomes even more expensive. Try to "shift left" expensive parts of the product into the beginning phases of development, and embrace change at any point. Make the thing work well now.

## Lean Values
## DevOps Values
As a way to codify some of the central focus of DevOps in a typical organization, Damon Edwards, John Willis and Jez Humble came up with an acronym [CALMS][3] \[[8][8]\] \[[9][9]\]

 * **Culture** - A culture of cross-functional collaboration must be developed that embraces change and experimentation.

 * **Automation**
   * Continuous delivery
   * Infrastructure as code

 * **Lean**
   * Focus on producing value for the end user
   * Small batch sizes

 * **Measurement**
   * Measure everything
   * Show the improvement

 * **Sharing**
   * Open information sharing
   * Collaboration and communication

<br />
# Principles
Principles are often seen as rules or laws, but in Agile and DevOps, principles are still more like guidelines or goals to strive for.

## [Agile Principles][4] \[[5][5]\]
Agile has its "12 principles", which we can apply to more than just pure software development. You may note that some of the principles tend to repeat themselves.

From [SmartSheet's Twelve Agile Manifesto Principles][https://www.smartsheet.com/comprehensive-guide-values-principles-agile-manifesto] (slightly modified):

<!-- todo: add a quotation box here -->
 1. **Customer happiness through early and continuous delivery** <br />
   Make the customer happy by giving working updates on a frequent basis. Note the key word *delivery*, which almost always involves more than just writing and testing software.

 2. **Accommodate changing requirements throughout the development process** <br />
   Avoiding delays when a requirement or feature request changes.

 3. **Frequent delivery of working software** <br />
   This is really the first principle in more detail.

 4. **Daily collaboration between business stakeholders and developers throughout the project** <br />
   The business should be informing development and vice versa. But this should also be expanded to include "operations", and anyone else who has a hand in ensuring the project's success.

 5. **Support, trust, enable, and motivate the people involved** <br />
    This one is pretty simple: happy, motivated people are more productive. But you should also give them the resources and access they need, and then step back and let them do the job. To do this [you need trust][7], and to have trust you're probably gonna need really good hiring, and training.

 6. **Enable face-to-face interactions** \[[6][6]\] <br />
    The closer people are to each other, the easier and more frequently they'll communicate. If you can't keep people close together, you'll need to work hard to improve their communication.

 7. **Working software is the primary measure of progress** <br />

 8. **Agile processes to support a consistent development pace** <br />

 9. **Attention to technical detail and design enhances agility** <br />

 10. **Simplicity** <br />

 11. **Self-organizing teams encourage great architectures, requirements, and designs** <br />

 12. **Regular reflections on how to become more effective** <br />
    

 * **Holistic solutions to problems**
   Not every problem that *can* be solved with software, *should* be solved with software. When trying to solve a problem, we should look at the whole system and pick a solution that best fits with the entire system in consideration.

## Lean Principles

## DevOps Principles

DevOps methodology doesn't have many hard-and-fast principles, but there are a few that best practices has shown to be incredibly helpful, such as:

 - [Immutability][] : The idea that something does not change once it is created. This helps make the following more predictable:
   - Changes to infrastructure, policies, software, etc
   - Feature development
   - Operation of a product
   - Application stability


---



You can think of DevOps as widening Agile principles to encompass the systems and operations needed to maintain reliable, quality products for customers at scale.

---

## Valuing Cross-team Collaboration

DevOps isn't just focused on software. Many of the principles of DevOps come from a perspective of having multiple teams learn from and providing feedback to one another. Some of these principles include the following:

 * Deep, constant communication between software development and IT operational groups
 * Automated deployment processes
 * Constant feedback on the health of running software/products

Not only should Operations be getting constant feedback of the health of the products, but this feedback should go directly back into the development of the product. By informing development of how the product is working, it can help improve the quality of the product, and surfaces problems before they become an issue later on.

---


DevOps also inherits principles from [Lean manufacturing], such as the [Toyota Kata system].


[1]: https://www.informationweek.com/devops/agile-vs-devops-10-ways-theyre-different/d/d-id/1326121
[2]: https://www.guru99.com/agile-vs-devops.html
[3]: https://www.red-gate.com/blog/calms-relates-database-devops
[4]: http://agilemanifesto.org/principles.html
[5]: https://www.smartsheet.com/comprehensive-guide-values-principles-agile-manifesto
[6]: https://coachlankford.com/2018/10/07/agile-leader-pattern-4-for-building-awesome-teams-enable-face-to-face-interaction/
[7]: https://www.amazon.com/SPEED-TRUST-Thing-Changes-Everything/dp/1416549005
[8]: https://devops.com/using-calms-to-assess-organizations-devops/
[9]: https://www.atlassian.com/devops
