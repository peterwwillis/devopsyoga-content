# Infrastructure

'Infrastructure', wrt DevOps, refers to the hardware and software that is used to provide network services to end users. It includes everything from the networks connecting the internet together, to datacenters and physical servers, and the virtual servers and software running on them.

Every piece of infrastructure is considered a dynamic element in DevOps. It may need to grow or change from moment to moment, and must be tracked and changed with software tools, and those changes managed in version control.

## [Infrastructure as Code]
This term just means managing your infrastructure in version-controlled files. This could be as simple as writing down hostnames and IP addresses in a text file and saving them to [Git]. But ideally you would actually use modern [Infrastructure Orchestration Tools] to interpret configuration files and execute changes for you.

Commonly IaC is implemented by checking some configuration files into a version control system (such as [Git]).

Modern systems, called [Continuous Configuration Automation] systems, manage both the configuration and deployment of datacenter equipment. These are often referred to as "orchestration" tools.

Older systems are typically [Configuration Management] tools which are used in order to deploy datacenter equipment.

Examples:
 - Terraform, AWS CloudFormation, Ansible Tower, Otter (orchestration)
 - Ansible, Puppet, Chef, SaltStack (configuration management)

## Immutability
Links:
 - [What is Immutable Infrastructure?](https://www.digitalocean.com/community/tutorials/what-is-immutable-infrastructure)


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
