# Containerisation  :whale:

**Contents**
- [x] [What is containerisation?](#what-is-containerisation)
- [x] [DevOps and Containerisation](#devops-and-containerisation)
- [x] [Adopting new technologies](#adopting-new-tech-in-devops)
- [x] [Docker - How is it improving workflow?](#how-does-it-improve-workflow)
- [x] [Containerisation Technologies](#containerisation-tools)
- [x] [Containerisation vs Virtualisaiton](#containerisation-vs-virtualisation)
- [x] [Choosing between VMs Containers](#choosing-vm-vs-containers)
- [x] [What is a Daemon?](#-what-is-daemon)
- [x] [What are the challenges of Docker?](#what-are-the-challenges-of-adopting-docker)

> - [Setting up Docker](docker_basic.md) :whale:
> - [Spinning up multiple Docker containers with Docker-Compose](https://github.com/naistangz/Docker_demo)

## What is containerisation?
- Packing up software code and all its dependencies (node package manager, programming languages) so that it can run uniformly and consistently on any infrastructure or operating system.
- Containerisation allows developers to create and deploy applications faster and securely.

## Devops and Containerisation 
- Containerisation is key to reducing bottlenecks in the software pipeline.
- Increases 'velocity', by improving workflow because containers immediately solve application conflicts between different environments
- Eliminates 'it works on my machine' aphorism
- Containers and Docker bring developers and IT ops together, making it easier to collaborate because they simplify the build/test/deploy pipelines
- Ops and IT are collaborating through Docker, the devs own the container contents, its operating environment and dependencies. Ops can then use built images and run them in their orchestration system and deploy them with greater ease.
- No need to perform complex configuration tasks for every sprint
- **Cost optimisation** - Containers maximise resource utilisation within their own isolated virtualised environments. Organisations can accurately plan for infrastructure capacity and consumption.
- **Infrastructure agnostic** - Containers run on any OS, organisation can easily move workloads from on premise machine to virtualised environments to cloud infrastructure easily
- **Time optimisation** - Docker allows multiple applications to run on a single operating system rather than using a hypervisor which is time consuming to spin up multiple virtual machines.

## Adopting new tech in DevOps
- **Looking at current environment** - Analysing apps, reviewing what environment is best
- **Experimenting** - Trialing with new ways of working and tools to optimise work flow
- **Education** - Embracing new technology and investing in certifications to dedicate time to learning new tools.

## How does it improve workflow?
- Standardise development environments so you can run from the same starting point every time, reducing need to deal with inconsistent development environments. This increase onboarding and development productivity
- No need for manual configuration 
- Docker automatically builds and can be integrated with GitHub to automatically build images from source code and automatically push them to Docker Hub repo instead of manually building them
- Automated tests, improving code quality, and integrating source code on each pull request
- Webhooks, allowing Docker to integrate with API-based automated HTTP callbacks
- No need to scale underlying infrastructure because it's cloud managed
- Supports the Continuous Integration/Continuous Delivery pipeline


<img src="https://docs.microsoft.com/en-us/dotnet/architecture/containerized-lifecycle/docker-application-lifecycle/media/containers-foundation-for-devops-collaboration/persona-workloads-docker-container-lifecycle.png" alt="devops_and_containerisation">


## Containerisation Tools 
````bash
Docker 
Kubernetes
AWS ECS/EKS
Azure Container Service 
RedHat openShift
Google Container Engine
````

## Containerisation vs Virtualisation
- Both are two ways to deploy multiple, isolated services on a single platform
- Virtual Machines includes applications, the necessary binaries and libraries that would exist on the OS, the entire guest OS to interact with them
- VMs run software on top of physical servers to emulate a hardware system (e.g. Linux)
- A hypervisor or Virtual machine monitor is software that creates and runs VMs and sits between hardware and VM, and necessary to virtualise the server.
- Containers include the application and its dependencies and shares the kernel with other containers
- Containers are not tied to any specific infrastructure other than having the Docker Engine installed on its host 

Container|VM
---|---
Creates abstraction at OS level, use same physical resources|Emulates physical hardware, runs on top hypervisor
Hold microservice or app and everything it needs to run|Uses hypervisor to separate resources from physical machine so they can be partitioned and dedicated to VMs
Everything in container preserved on image e.g libraries and dependencies|VMs act like physical services, which can multiply the drawbacks of application dependencies and large OS footprints, not needed to run a single app
Light-weight. Rather than spinning up an entire virtual machine, they package everything to run a small piece of software|Hypervisor creates abstraction layer over hardware, allows hardware elements of single computer to be divided into multiple virtual computers
Containers are portable, they don't virtualise underlying hardware, virtualise OS meaning they can leverage features and resources of the host OS  |Virtualises physical hardware, each VM contains a guest OS, a virtual copy of hardware, an app and its libraries and dependencies
Improve CPU and memory utilisation|Improve CPU and memory utilisation
Uses kernel of host OS, host's kernel limits use of other OS|Guest machine aka VM, completely isolated from host OS, you can install multiple system environments 


## Choosing VM vs Containers
VM|Containers
---|---
Manage a variety of OS|Maximising the number of apps running on a server
Manage multiple apps on single server|Deploy multiple instances of a single application
Run an app that requires all the resources and functionalities of OS|Lightweight that quickly starts
Ensures full isolation because it is virtualising the hardware so that each virtual machine has its own operating system|Develop an application that runs on any underlying infrastructure
Better security| 
|Running more workloads the same hardware
|Docker uses a client-server architecture. The docker client or local host talks to the Docker *daemon*, which does the heavy lifting of building, running and distributing your Docker containers. Docker client and daemon communicate using a `REST API`

**Virtual machines are used for** demanding applications, network infrastructure, and apps that will consume most of the resources of the VM.

**Containers are used for** web, applications, caching services, network daemons (background processes - file transfers, dormant when not required) and small databases.

<img src="https://blog.netapp.com/wp-content/uploads/2016/03/Screen-Shot-2018-03-20-at-9.24.09-AM.png" alt="docker_vs_virtualisation">

## What is a container?
- Instances of an image, like a printout of the Docker image.
- Packaged software into units for development, shipment and deployment
- Containers package up code and its dependencies so the application runs quickly and reliably from one computing environment to another
- Containers are runnable instances of an image. You can `create`, `start`, `stop`, `move` or `delete` using the Docker API or CLI.
- A container image http://0.0.0.0:4000is lightweight, standalone, executable package of software that includes everything needed to run an application:
```bash
Code
Runtime
System Tools
System Libraries
Settings
```

## What is an image?
- A template with instructions for creating a Docker container
- An image is *based* on another image, with some additional customisation.
- For example, you may build an image which is based on the `ubuntu` image, but installs the Nginx web server and your application and configuration details needed to make your application run.
- You can create your own images or use those created by others
- Inability to change (immutability) is powerful tool. Meaning consistency and allows developers to try out additions on your environment or new software packages and can be sure that you are not breaking your working instance.
- Images are shareable, once you've created an image, that person can use the image and every developer a team will have the exact same development instance.
- Because systems are identical, you don't need to spend time troubleshotting issues that only exist in one environment.

## What is Docker?
- Applications are often developed and tested on one machine 
- This leads to problem of 'works on my machine', where the developer does not know why or how the application does not work on a different machine
- Docker shares the resources of an OS 
- Different part of a system may change over time, leading to application not working
- Changes can be anything:
    - Operating system update
    - Changes in dependencies and version updates
    - Hardware changes 
- Docker combines the application and its dependencies into an image that can then be run on any machine, provided it can run containerisation tools such as Docker
- Docker contains three things:
    - An image
    - An execution environment
    - A standard set of instructions
- From OOP world, you can use analogy of classes and objects, container is object, the class is a Docker image

## How does docker work?
- Packages and runs an application in an isolated environment called a container
- The isolation and security allow us to run containers simultaneously on a client/local host.
- They are lightweight because they don't need a hypervisor and run directly within the host machine's kernel.
- This means you can run more containers on hardware than if you were using virtual machines.
- Docker uses client-server architecture, where local host or client communicates to a docker daemon with RESTful API. If local host does not have the image, Docker communicates with the Docker registry to pull the image from the remote server so that it can run locally.

## Docker Engine and Components
- *Docker Engine* is a client-server application with these components:
    - A `server` which a type of long-running program called a `daemon` process. The `dockerd` command
    - A `REST API` which specifies interfaces that programs can use to talk to the daemon and instruct it what to do.
    - A command line interface `cli` client (the `docker` command).
- The CLI uses the Docker `REST API` to control or interact with the Docker daemon through direct CLI commands.
- The `daemon` creates and manages Docker objects, such as images, containers, networks, and volumes.


## What is Daemon?
- Program that runs continuously and exists for the purpose of handling service requests that a computer system expects to receive
- Daemon program forwards the requests to other programs (or processes).
- `dockerd` listens for Docker API requests and manages Docker objects such as images, containers, networks, and volumes.

## Docker Registries
- Docker registry stores Docker images
- Docker hub is a public registry that anyone can use
- Docker configured to look for images on Docker Hub
- When using `docker pull` or `docker run` commands, the images are pulled from confiured `registry`.

## What are the challenges of adopting Docker
(Containers won't be replacing VMs)
https://www.infoworld.com/article/3310941/why-you-should-use-docker-and-containers.html


