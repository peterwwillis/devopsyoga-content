# Declarative Programming of Infrastructure

Declarative programming is a programming paradigm used to describe *what* a program must accomplish, rather than *how* to accomplish it. This form of programming is used to build cloud infrastructure, with solutions such as AWS CloudFormation, and HashiCorp Terraform.

## Benefits of Declarative Infrastructure
<!-- TODO --> I need content, please edit me!

## Problems of Declarative Infrastructure

### Non-idempotence
Not all resources used by your infrastructure are idempotent - that is, they cannot be applied multiple times without changing the initial result. Therefore, declarative infrastructure cannot be said to be fully idempotent. You will have to write tests and workarounds to ensure your result is as expected.

### Making specific changes is hard
You know you want to modify job C that runs on server type A, but you don't want to change job C on server type B. You will probably have to copy the job and make a new one with the change, and make it run only on server type A. Or, even more complicated, add specific logic to job C to behave differently only on server type A. These kinds of divergent changes make your code more complex over time, and thus harder to manage.

