# AWS  

## What is AWS?
- A secure cloud services platform, offering compute power, database storage, content delivery and other functionality to help businesses scale and grow.
- Infrastructure as a Service (IaaS)
- Platform as a Service (PaaS)

## IAM 
Identity Access Management

## VPC

## Network Access Control Lists
- Firewall for subnet
- Controls inbound and outbound traffic
- Stateless, meaning if you want your instances to communicate over port 80 (HTTP), then you have to add an inbound as well as an outbound rule allowing port 80.
- When creating a VPC, it comes with a default Network ACL that allows all inbound and outbound rules.
- If you create a custom NACL, both inbound and outbound rules are denied

## Security Groups 
- Stateful
- They are virtual firewalls for your **instance** to control inbound and outbound traffic. 
- If you don't specify a security group, the instance is automatically assigned to the default security group for the VPC.

## Using SGs and NACLs in VPC
- Configuring SGs and NACLs in VPC help reduce attack surface of your applications hosted on AWS.
- They mutually complement each other, because SGs allow defining the traffic to resources within the applications
- NACLs allow defining the port, protocol, and source of traffic that should be explicitly denied at the subnet level.

## What is Amazon EC2 Instance?
- Amazon Elastic Compute Cloud, is a service, forms part of Amazon's cloud-computing platform that allow users to rent virtual computers on which to run their own applications.
- EC2 allows us to deploy virtual servers and manage storage through an [AMI](#ami)
- An EC2 instance is a virtual server in Amazon's Elastic Compute Cloud (EC2) for running applications on the **Amazon Web Services** infrastructure.
- **EC2** is a service that allows business subscribers to run application programs in the computing environment. 

## Why use an EC2?
- It lessens the needs to invest in hardware
- Helps streamline development processes
- Reduces time to boot new servers
- You can easily scale up the capacity 
- Flexibility with operating systems

## How do you set up AWS EC2?
- Involves creating an AMI, which includes an operating system, apps and configurations
- That AMI is loaded to the Amazon Simple Storage Services (S3)

## AMI
- Templates 
- Amazon Machine Image
- A template to create virtual machines within the Amazon Elastic Compute Cloud
- Template for the instance (e.g operating system, an application server)


