# DevOps Infrastructure

'Infrastructure', with respect to DevOps, refers to the hardware and software resources that are used to provide services to end users. It includes everything from the networks connecting the internet together, to datacenters and physical servers, and the virtual servers and software running on them.

Every piece of infrastructure is considered a dynamic element in DevOps. It may need to grow or change from moment to moment, and must be tracked and changed with software tools, and those changes managed in version control.

## [Infrastructure as Code]
This term just means managing your infrastructure in version-controlled files. This could be as simple as keeping hostnames and IPs in a text file in Git, but modern best practice is to use tools that interpret standard configuration files and execute changes.

The first tools used for IaC were [Configuration Management] tools like [Puppet] and [Chef], as well as orchestration like [AWS CloudFormation]. Modern [Continuous Configuration Automation] systems manage both the configuration and deployment of datacenter equipment, and are referred to as "orchestration" tools.

Examples:
 - Orchestration / Continuous Configuration Automation
   - Terraform, AWS CloudFormation, Ansible Tower, Otter (orchestration)
 - Configuration Management
   - Ansible, Puppet, Chef, SaltStack (configuration management)

## Immutable Infrastructure 
The term 'immutable' means something cannot be modified after it is created. This is very useful for both software and infrastructure, as it allows us to simplify the method of resolving problems and avoid dangerous use patterns.

If infrastructure is 'mutable', it may often change in subtle ways, which then become complex changes over time, introducing bugs. By keeping systems from changing over time, we reduce this eventuality.

All immutable infrastructure must be created through a standard automated process, be version controlled, and pass a series of tests. This ensures that all changes are known and repeatable, and allows for simple roll-back in the event of problems.

The benefits are immense. No more wrestling with a configuration management tool, connecting to all of your hosts, updating their software patches, taking out time to fix one or two which didn't update properly, trying to figure out who edited a file on one host one time three years ago, or trying to re-install an old server or package which nobody knows how to do anymore. Simply start a brand new instance from the version-controlled image, and disable/delete the old one when you are finished. To roll back, do the same procedure with a different version of the image.

Examples:
 - Docker containers
 - Packer-created system images
 - AWS EC2 AMIs

Links:
 - [What is Immutable Infrastructure?](https://www.digitalocean.com/community/tutorials/what-is-immutable-infrastructure)
 - https://www.sumologic.com/devops/devops-as-a-service/understanding-mutable-and-immutable-infrastructure/

## Pets vs Cattle



## Requirements for Running Production Services

### Bootstrapping
 - Preparing infrastructure or its tools.

   Before infrastructure can be provisioned, there almost always needs to be some
   work done ahead of time. Usually this involves downloading software and
   configuring it, to use for the following provisioning and other requirements.

   Bootstrapping is something that always has to be done, but is often done by
   hand. This can lead to problems down the road, from lack of version control,
   to using compromised files, to incompatible files used by different people or
   for different tasks. Bootstrapping is a good example of [Yak Shaving].

   The more automated bootstrapping is, the less likely this component will cause
   problems for you in production (and problems do happen due to lack of
   automated bootstrapping).

### Configuration
 - Configuring some aspect of infrastructure (or its tools) before use.

   Often there is a need to configure software right before you start
   running it. This may include things like telling some software to set some
   variable before it runs, or what file path to use, what user to run as, what
   port number to use, what access control permissions to grant or deny, etc.

   This configuration information needs to be passed along somehow, but it also needs to
   be stored somehow.
#### Service Configuration
   - Configuring a service.
     - [Example of Consul for Service Configuration]
     - [Example 2 of Consul for Service Configuration]

### Provisioning
 - The act of acquiring some infrastructure to work on a particular task.

   Sometimes this is done only once very occasionally, such as provisioning a
   large, persistent virtual machine for use as a database server. Sometimes this
   is done very frequently, such as provisioning a new resource for complex
   end-to-end testing, and then removing the infrastructure after the test
   completes. Some managed cloud services automatically provision and
   de-provision infrastructure in the background for you, and sometimes you may
   need to implement your own custom solution that does something similar.

### Deployment
 - Installing or updating a stable application or service onto infrastructure.

### Security
### Monitoring
### Logging
### Backup/Restore
### Networking
### Availability
### Scalability
### Performance
### Cost
### Documentation
### Testing
### Maintenance

[Example of Consul for Service Configuration]: https://codeblog.dotsandbrackets.com/consul-key-value-store-configuration/
[Example 2 of Consul for Service Configuration]: https://awmanoj.github.io/tech/2016/08/27/service-discovery-configuration-management-with-consul/
[Infrastructure as Code]: https://en.wikipedia.org/wiki/Infrastructure_as_code
[Continuous Configuration Automation]: https://en.wikipedia.org/wiki/Continuous_configuration_automation
