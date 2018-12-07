# Deployment
The process of deployment can include building infrastructure, copying files, changing security rules, and opening network paths for application traffic. If these changes are not removed when they no longer become necessary, various problems emerge. Wasteful use of resources, security vulnerabilities, and overall confusion over legacy configurations can result.

# Undeployment
Undeployment processes effectively reverse the deployment process. As a practical tool, they can be one part of a rollback procedure, and as another, help shut down resources no longer in use. They are also useful to reduce waste.


# Deployment Models
There are many different models for deployment. You may choose one, or mix and match several, depending on your requirements.

## Simple Short
A simple short deployment model involves taking build artifacts, putting them in some remote place, and performing some steps to make the new build artifacts live. It happens immediately and there are no other considerations.

## Complicated Long
A complicated long deployment model takes the simple short model and extends it to support large, customer-facing, potentially volatile situations. It may have multiple dependencies and require orchestration of multiple components. It may need to be paused, resumed, or aborted. It may need to have tests run at each phase before continuing.

## Dependency-driven deployment
Dependency-driven deployment involves deploying using a hierarchy of dependencies. Dependencies that have already been deployed successfully may be skipped to save time.

## Blue/Green deployment
In this model, two environments exist: one with an old version of your app, and one with a new one. By switching traffic from one environment to the other you can fall back quickly in the event of a problem with the deploy or issues experienced after deploy.

Potential pitfalls:
 - Long-running transactions in the old environment need to be phased out safely
 - If you use separate databases for these environments, you may need to migrate data from one to the other.
 - If you use the same database for these environments, you may have problems in the new environment that affect the old one.
 - If you use a database service that supports snapshots, definitely use them.

## Blue/Turqoise/Green deployment
This is the same as Blue/Green deployment, but with an extra step to handle moving applications on a shared data store.

When switching apps that are using a shared database, the database may need to be modified to support the new app code, which would break the old application. This normally requires a maintenance outage. To avoid that outage, "Turquoise" is an intermediate environment with the old application, and with a database that supports both the old and new application. Blue is switched to Turquoise, where the Blue app keeps running, but on a Green-compatible database. Then you switch to the Green stack, which is both the new app and the new database.

Links:
 - https://www.digitalocean.com/community/tutorials/how-to-use-blue-green-deployments-to-release-software-safely
 - http://blog.dixo.net/2015/02/blue-turquoise-green-deployment/
https://www.slideshare.net/mikebrittain/mbrittain-continuous-deploymentalm3public/50

## Canary deployment
Canary deployment is similar to Blue/Green deployment except it is not an all-or-nothing cutover. Instead, a small percentage of users will use the new environment, and the rate increases as confidence grows, until the new environment gets 100% of traffic. The old environment can then be removed.

## Continuous deployment
Links:
 - https://www.slideshare.net/mikebrittain/mbrittain-continuous-deploymentalm3public/

