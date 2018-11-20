# Abstracting Infrastructure

A large amount of the cloud infrastructure we use is built on details which can be abstracted and ignored. Here is a short list of some of those details, and how they can be abstracted.

## Components that are abstracted

## Types of abstraction

### Services
A service is *"A valuable action, deed, or effort performed to satisfy a need or to fulfill a demand."*

There are many things we manage as infrastructure that can be seen as services. AWS and OpenStack provide us the service of running programs and storing & retriveving data. Web servers provide us the service of taking a request and returning a result. Services may often depend on other services, and through automation and layers of abstraction, we simplify the process of supporting these services for our customers.

### Credential management
A credential is *"Evidence of authority, status, rights, or entitlement to privileges."*

Each instance of a service in a cloud system requires its own credentials. By assigning a credential to a service, we can run multiple of the same service to isolate them in independent access control domains, or grant access to them as needed.

Credentials work with an access control system to control what parts of the system, or what users, have particular access to, or perform particular operations on. All services and users in a distributed system require credentials to operate securely.

However, the specific credentials often do not affect the infrastructure directly. As long as they are applied correctly, the infrastructure does not care what your credentials are. Therefore we can easily abstract the credentials away in an automated system.

### Users and Groups
There may be multiple users of your system, and each user may need different access to different services. By managing groups and assigning users to them, we can abstract away the details of users. Furthermore, if we put groups inside of other groups, we can abstract away the entire hierarchy of user access to services.

If we know we will have multiple projects, and that most users will at least be assigned to a single project, we can start by creating one group for every project. In this way we can control the groups of users who have access to entire projects. This is mostly only useful for groups of administrators, but can also be useful to provide read-only access to projects without sensitive data.

### Roles

As we saw above, assigning administrators to a project's group lets us manage who can access all the instances of a project. But if there are multiple projects, we would have to manage those admins on every project. Instead we can create a special group called a 'role', which is made up of all the users who should have a particular kind of access to a project, or across projects, and add that 'role' to the project.

### Customers
Some projects can become large, and the use of the project can vary greatly between users and groups. For this purpose we have created a 'customer' designator, to be a sort of project super-group.

We know our project 'Web' has a group 'Web', but there may be lots of users who need different access to 'Web', with different kinds of access to data. If we can separate groups of users into 'Customer A', 'Customer B', etc, we can split up how the 'Web' project is used, but inherit the shared properties of the 'Web' project.

We can create a group called 'Web-Customer\_A', and assign users 1,2,3 to this group, and assign users 4,5,6 to 'Web-Customer\_B'.

Now we can not only manage the users who have access to all of the 'Web' project, but we can also control which users have what access to what parts of which customer.

(why do we call this designator 'Customer'? Because a customer by definition is "someone who is being served by a business or individual", and we treat our individual groups of users as customers of our service)

In this way, we not only know there is a group that encompasses all of the 'Web' project instances.

### Example: Running Jenkins
For our project 'Web', we have an instance "Web-Customer\_A", where jobs for 'Customer A' are run for the 'Web' project. To start Jenkins for this instance "Web-Customer\_A", we will use credentials called "Web-Customer\_A-Jenkins". This ensures that this instance of Jenkins can only be controlled by a user or service that works with 'Customer A' on the 'Web' project.

We derived the name of the credential from the project, the customer, and the service name. All of this is known by the time we deploy our customer's project, so an automated process can create the credential as well, and assign it as necessary.

