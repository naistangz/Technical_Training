# Infrastructure as code with Terraform

**Contents**
- [x] [Infrastructure as Code](#infrastructure-as-code)
- [x] [Orchestration and Configuration Management](#what-is-the-difference-between-orchestration-and-configuration-management)
- [x] [Configuration Management Tools](#configuration-management-tools)
- [x] [Orchestration Tools](#orchestration-tools)
- [x] [What is Terraform](#what-is-terraform)
- [x] [Why Terraform?](#why-terraform)
- [x] [Terraform Commands](#terraform-commands)
- [x] [Creating an AWS Subnet and Security Group using Terraform](https://github.com/naistangz/terraform_demo)


## Infrastructure as code 
```bash
Configuration Management 
Orchestration Management 
```

## Recap - What is IaC?
- IaC is a method to provision and manage IT infrastructure through the use of source code, rather than through standard operating procedures and manual processes.
- It is the process of treating our servers, databases, networks, and other infrastructure like software.
- This code can help us configure and deploy infrastructure components quickly and consistently and significantly reduces time.
- IaC helps us to automate the infrastructure deployment process in a repeatable, consistent manner

## Why is IaC is important?
- Historically, sysadmins used to deploy infrastructure manually including every server, every route table entry, every database configuration, every load balancer was set up manually.
- DevOps, changed this by treating these configurations like software and setting up through Infrastructure as Code (IaC).
- IaC alleviates the issues and cost implications of investing in hardware as well as the the costs that come with human capital and real estate.
- IaC allows to spin up servers, databases, etc very quickly, which would address the [scalability](#scalability), [high availability](#availability) and [agility](#agility) problems.  
- IaC allows for consistency, due to code reusability 

## Scalability 
- Being able to adapt to changes over time and meet market demands
- Market demands are never static, so automating the management of environments is useful to meet unexpected changes such as a spike in traffic
- AWS provides monitoring services to detect changes such as CPU usage, expiring data points and automatically spins up new servers.

## Availability 
- High available systems mean that operations that continue as normal
- Any downtime will impact this, so it is important to maintain the system setup and plan to mitigate potential problems before they arise.
- You can use Amazon EC2 auto scaling to maintain a minimum number of running instances for your application at all times so when traffic increases, you can use Elastic Load Balancing to distribute incoming traffic across these EC2 instances, thereby increasing the availability of your application
- You can also place your instances in multiple Availability Zones in the event if one availability zone experiences an outage.

## Agility 
- Agility means the ability to change course, according to changes in our environment
- This means inspecting and adapting such as the ability to shorten lead times, responding to changing circumstances, quickly and inexpensively and delivering in rapid cycles
- Being agile also means risk mitigating. Market demands are never static, customers are fickle, macro economic circumstances can impact decisions and financial performance. Being technologically agile is key to being competitive and flexible. 

## What is the difference between orchestration and configuration management?
Orchestration|Configuration
----|----
Arranging or coordinating multiple systems|Configuring is about bringing consistency
Designed to automate deployment of servers| Systematically handling changes to a system in a way that it maintains integrity over time
--|Consistency of systems and hardware
--|Configure software and systems that has already been provisioned
Terraform to deploy underlying infrastructure e.g network topology (VPCs, subnets, route tables), load balancers|Ansible deploys our apps on top of those servers

## Configuration management tools 
```bash
Chef
Puppet 
Ansible
SaltStack
```

## Orchestration Tools 
```bash
Terraform
Openstack Heat 
AWS Cloudformation
Kubernetes
```

## What is Terraform?
- A tool for developing, changing, versioning infrastructure safely and efficiently 
- Terraform can manage existing and popular service providers as well as custom in-house solutions.
- Terraform provides support for immutable infrastructure (Immutable images are static and any updates must generate a new version of the base image)

## Why terraform
- Simple json syntax
- Open source
- Able to provision infrastructure using on premise computer without using AWS Services, therefore it is cost effective
- Code re-usability, allowing to make changes faster. 
- Every aspect of a cloud provider's platform is accessible without scripting in an API. 
- Terraform's `plan` command lets you see what changes you're about to apply before you apply them
- Terraform allows you to rebuild/change and track changes to infrastructure with ease.
- Terraform enables you to implement all kinds of coding principles like having your code in source control and the ability to write automated tests.
- Uses **declarative statements**, meaning you declare how you want your IT infrastructure to be configured and then Terraform maps out the dependencies and builds everything for you.


### Terraform commands

```tf
terraform init
terraform plan - checks the steps inside the code and lists the successes and errors
terraform apply - will implement the code - deploy the infrastructure
```

---

# Creating an AWS Subnet and security group using Terraform

1. `main.tf`
```hcl-terraform
provider "aws" {
# which region do we have the AMI available
  region = var.region

}

# Creating an instance - launch an EC2 Instance from the AMI
resource "aws_instance" "app_instance" {
          ami          = "ami-08617e0e0b2d50721"
# what type of ec2 instance we want to create = t2.micro
          instance_type = "t2.micro"

# public IP
          associate_public_ip_address = true
          tags = {
            Name = "Eng67.Anais.terraform.app"

          }

} # end Creating an instance


# Creating a subnet block of code and attaching this to DevOpsStudent VPC
resource "aws_subnet" "public_subnet" {

  cidr_block              = var.subnetCIDRblock
  vpc_id                  = var.vpc_id
  map_public_ip_on_launch = var.mapPublicIP
  availability_zone       = var.availabilityZone
tags = {
  Name = "Eng67.Anais.Ansible.Subnet.Public"
}

} # end Creating Public Subnet

# Create a security group and attach it to the VPC
resource "aws_security_group" "public_sg" {
  vpc_id                  = var.vpc_id
  name                    = "Eng67.Anais.public.SG"
  description             = "Eng67.Anais.public.SG.terraform"

  # Allow ingress of port 80
  ingress {
    cidr_blocks = var.ingressCIDRblock
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
  }


  # Allow egress of all ports
  egress {
    cidr_blocks = var.egressCIDRblock
    from_port   = 0
    protocol    = "-1"
    to_port     = 0
  }

tags = {
  Name = "Eng67.Anais.public.SG"
  Description = "Eng67.Anais.public.SG.terraform"
}

} # end creating public sg
```

2. Create variables file `variables.tf` example:
```hcl-terraform

variable "availabilityZone" {
  default = "eu-west-1b"
}

variable "vpc_id" {
  default = "vpc-07e47e9d90d2076da"
}

variable "vpcCIDRblock" {
    default = "172.31.0.0/16"
}

variable "subnetCIDRblock" {
    default = "172.31.7.0/24"
}
```
