---
title: DevOps Practices
description: 
---

# What are DevOps Practices?
At its core, DevOps is just a collection of engineering, business, and cultural practices. When fully implemented, those practices should result in measurably more stable products that can be delivered quicker than using more traditional methods.
<!-- TODO: link to DevOps Practices from here -->

   - [Site Reliability Engineering]

## Agile Software Development
The development and production of software should follow an Agile software development lifecycle. Frequent integration and deployment of code should result in faster and less error-prone software testing and delivery. Focus should be on testing and deploying small amounts of work frequently in short cycles, rather than trying to ship perfect code over long development cycles.
<!-- TODO: link to agile software development docs here -->

## Continuous Improvement
In every aspect of a product, there should be a focus on repetition and improvement, preferably in small increments. Frequent repetition of process allows the process not to become stale, and for inefficiencies to be caught early. A review of inefficiency can be used to improve the process.

Examples:
 - [Continuous Integration & Delivery] (also known as CI-CD)
 - Failover Recovery
 - Customer Service Feedback

## Immutable, Version-Controlled State
Wherever possible, a process should take as input a version controlled object, and produce a version controlled artifact. These artifacts should be immutable, and as little state should change as possible in the use of these artifacts. This prevents changes from causing unexpected errors, and allows for simple recovery in the event of errors.

Examples:
 - [Immutable, Automated Infrastructure as Code]


[Immutable, Automated Infrastructure as Code]: ./infrastructure.md
[Continuous Integration & Delivery]: ./ci-cd.md
