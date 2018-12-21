---
title: DevOps Practices
description: 
---
# DevOps Practices

DevOps encompasses engineering, business, and cultural practices. These practices should result in measurably more stable products that can be delivered quicker than using more traditional methods.

## Continuous Feedback & Improvement
There should always be a focus on feedback and improvement in DevOps processes. This is one of the cornerstones of DevOps, and should be practiced early on with development teams, and later with other teams related to a product.

Some examples of these practices:
 - [Continuous Integration & Delivery](./ci-cd.md) (also known as CI-CD)
 - Blameless Postmortems
 - Customer Feedback

## Immutable, version-controlled state
Immutability in DevOps refers to the idea that once we create something new, it should never be changed; instead, something new should replace it. In addition, each of these creations should be versioned, so we can easily manage them. This is an incredibly powerful paradigm that solves many old problems, such as unexpected errors from tiny changes over time, and simplifying upgrade, rollback, and failover.

[A paper from 2002](http://www.infrastructures.org/papers/turing/turing.html) explains why this is true, and why we should adopt this practice.

Some examples of these practices:
 - [Infrastructure as Code](./infrastructure.md)

### Congruent environments
This is part of the Immutable practice above, with a slight twist. Each environment should be the same as the others. This means that, if at all possible, you should just test and deploy in your production environment. Everyone should have the same development environment, with the same tools, at the same versions. Once this is done, there's less conflicts over incompatibilities.

## Service requirements
In order to run services properly, DevOps has a series of [typical requirements for production services](./services.md).


## Agile software development
As DevOps members develop their own software and products, they should ideally follow Agile methods. Frequent integration, testing, and deployment of code will result in faster, less error-prone software.


