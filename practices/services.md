# Services

DevOps is dedicated to running software products, typically as a service for end users (often called "customers"). It's common for a service to require a variety of elements to be operated properly in a production environment.

The following are some of the requirements for running production services:

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


