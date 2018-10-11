# Setting Up Docker on Linux

This guide sets up Docker Machine (a virtual machine with Docker installed) in order to control Docker in a pre-built environment.

### Pros
 - No need to set up and maintain a Docker installation on your host.
 - Break down or build up multiple Docker environments easily, and even maintain them on remote hosting providers.
 - Seamlessly integrates with Docker Swarm, allowing you to horizontally scale the number of virtual machines you can run containers on.
 - If you already plan on running containers on disposable virtual machines, this gives you a simple tool to do just that.
### Cons
 - Requires the ability to run virtual machines on your host. Most mostern laptops and desktops have this capability, but embedded devices and older computers may not.
 - More host overhead than simply running containers directly on an existing host.

## Step 1. Download Docker Machine

## Step 2. Download and Install VirtualBox

## Step 3. Create a Docker Machine

Create a new docker machine called *dev*.

```bash
~$ docker-machine create dev
Running pre-create checks...
(dev) Default Boot2Docker ISO is out-of-date, downloading the latest release...
(dev) Latest release for github.com/boot2docker/boot2docker is v18.06.1-ce
(dev) Downloading /home/psypete/.docker/machine/cache/boot2docker.iso from https://github.com/boot2docker/boot2docker/releases/download/v18.06.1-ce/boot2docker.iso...
(dev) 0%....10%....20%....30%....40%....50%....60%....70%....80%....90%....100%
Creating machine...
(dev) Copying /home/psypete/.docker/machine/cache/boot2docker.iso to /home/psypete/.docker/machine/machines/dev/boot2docker.iso...
(dev) Creating VirtualBox VM...
(dev) Creating SSH key...
^@^@(dev) Starting the VM...
(dev) Check network to re-create if needed...
(dev) Waiting for an IP...
Waiting for machine to be running, this may take a few minutes...
Detecting operating system of created instance...
Waiting for SSH to be available...
Detecting the provisioner...
Provisioning with boot2docker...
Copying certs to the local machine directory...
Copying certs to the remote machine...
Setting Docker configuration on the remote daemon...
Checking connection to Docker...
Docker is up and running!
To see how to connect your Docker Client to the Docker Engine running on this virtual machine, run: docker-machine env dev
```

## Step 4. Use the docker machine

For Docker to use this new Docker machine, you must load some environment variables into your shell.

However, if you load the environment variables into your current shell, it may be cumbersome to re-set the variables without exiting your shell, something you may not want to do yet.

To work around this, first run a new instance of your shell, and then load the environment variables.
```bash
~$ bash
~$ eval $(docker-machine env dev)
~$ 
```

Now when you use the `docker` command, it will actually control the Docker instance in your new dev machine.
For example, the following command will show that the OS that Docker is connected to is "Boot2Docker":
```bash
~$ docker info | grep 'Operating System'
Operating System: Boot2Docker 18.06.1-ce (TCL 8.2.1); HEAD : c7e5c3e - Wed Aug 22 16:27:42 UTC 2018
```

To reset the Docker Machine variables, simply `exit` from the new bash instance you started. You will go back to your old shell and the variables will be gone.
```bash
~$ exit
exit
~$ set | grep DOCKER
~$ 
```

## Step 5. Easier loading of the dev machine

To prevent having to type 'bash' and 'eval' as above, run [this bash script](./load-machine.sh) instead. It will drop you into a new shell with the 'dev' machine loaded, and modify your prompt to signify you are using this new machine. Just run `exit` to drop back into your previous shell.

