# Containerisation 

**Contents**
- [x] [What is containerisation?](#what-is-containerisation)
- [x] [DevOps and Containerisation](#devops-and-containerisation)
- [x] [Adopting new technologies](#adopting-new-tech-in-devops)
- [x] [Docker - How is it improving workflow?](#how-does-it-improve-workflow)
- [x] [Containerisation Technologies](#containerisation-tools)
- [x] [Containerisation vs Virtualisaiton](#containerisation-vs-virtualisation)
- [x] [Choosing between VMs Containers](#choosing-vm-vs-containers)

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
- Containers are not tired to any specific infrastructure other than having the Docker Engine installed on its host 

Container|VM
---|---
Creates abstraction at OS level, use same physical resources|Emulates physical hardware, runs on top hypervisor
Hold microservice or app and everything it needs to run|Uses hypervisor to separate resources from physical machine so they can be partitioned and dedicated to VMs
Everything in container preserved on image e.g libraries and dependencies|VMs act like physical services, which can multiply the drawbacks of application dependencies and large OS footprints, not needed to run a single app
Light-weight. Rather than spinning up an entire virtual machine, they package everything to run a small piece of software|Hypervisor creates abstraction layer over hardware, allows hardware elements of single computer to be divided into multiple virtual computers
Containers are portable, they don't virtualise underlying hardware, virtualise OS meaning they can leverage features and resources of the host OS  |Virtualises physical hardware, each VM contains a guest OS, a virtual copy of hardware, an app and its libraries and dependencies
Improve CPU and memory utilisation|Improve CPU and memory utilisation
Uses kernet of host OS, host's kernel limits use of other OS|Guest machine aka VM, completely isolated from host OS, you can install multiple system environments 


## Choosing VM vs Containers
VM|Containers
---|---
Manage a variety of OS|Maximising the number of apps running on a server
Manage multiple apps on single server|Deploy multiple instances of a single application
Run an app that requires all the resources and functionalities of OS|Lightweight that quickly starts
Ensures full isolation because it is virtualising the hardware so that each virtual machine has its own operating system|Develop an application that runs on any underlying infrastructure
Better security|

**Virtual machines are used for** demanding applications, network infrastructure, and apps that will consume most of the resources of the VM.

**Containers are used for** web, applications, caching services, network daemons (background processes - file transfers, dormant when not required) and small databases.

<img src="https://blog.netapp.com/wp-content/uploads/2016/03/Screen-Shot-2018-03-20-at-9.24.09-AM.png" alt="docker_vs_virtualisation">

## What is a container?
- Packaged software into units for development, shipment and deployment
- Containers package up code and its dependencies so the application runs quickly and reliably from one computing environment to another
- A container image is lightweight, standalone, executable package of software that includes everything needed to run an application:
```bash
Code
Runtime
System Tools
System Libraries
Settings
```

## What is Docker?
- Applications are often developed and tested on one machine 
- This leads to problem of 'works on my machine', where the developer does not know why or how the application does not work on a different machine
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

    


