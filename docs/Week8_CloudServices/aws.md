# AWS  

## What is AWS?
- A secure cloud services platform, offering compute power, database storage, content delivery and other functionality to help businesses scale and grow.
- They offer mix of packaged software as a service, platform as a service and infrastructure as a service. Very extensive.
- Main uses are:
1. **Storage service or S3** - to share large files or small files to large audiences online. Sometimes it can be expensive to share huge volumes of data online so AWS provides cloud storage that offers scalability for file sharing.
2. **Simple email service** - Sending emails to thousands of customers. You cannot achieve that with outlook or Gmail. Simple email service can handle huge transactional emails.
3. **Website hosting** - AWS offers advantage of not worrying about exceeding the allocated usage of resources. Offers scalability and practical for hosting different websites.
4. **Cloudfront** - Web data transferred from a central server to an edge server's distributed network which is closer to the location of the end-user. This task is performed by the Content Delivery network (CDN). This distributes the website traffic better, improving load times and providing better experience for the end-ser. AWS offers no limit to its scalability.

<img src="https://d2o2utebsixu4k.cloudfront.net/media/images/1567147556468-Amazon-Web-Services-2.png">

## IAM 
- Identity Access Management - framework of policies that manages user identities and regulates user access within an organisation 
- Two vital IAM concepts - User and Access, former being employees, partners, suppliers, contractors, latter being an administrator.
- Three tasks: authenticate, identify and authorise (grant user privileges)

## VPC
- A virtual private cloud
- Public cloud in AWS with security around it, granting you virtual privacy.
- Personal data center in Amazon's Cloud
- Taking your data centre with all your different servers, all your different storage units, in the cloud.
- You can create subnets within the VPC

## VPC Endpoints
- End point, a device that is physically an end point on a network e.g. laptops, desktops, mobile phones, tablets, servers, virtual environments.
- In AWS, endpoints are virtual devices, they allow communication between instances in your VPC.
- Termination point or a node
- There are two types of VPC endpoints:
    1. Interface endpoints - elastic network interface with Private IP, serves as entry point for traffic destined to a supported device.
    2. Gateway endpoints - a gateway that you specify as a target for a route in your route table 

## Network Access Control Lists
- Stateless, support allow and deny rules
- Firewall for subnet (at network level)
- Controls inbound and outbound traffic
- Stateless, meaning if you want your instances to communicate over port 80 (HTTP), then you have to add an inbound as well as an outbound rule allowing port 80.
- When creating a VPC, it comes with a default Network ACL that allows all inbound and outbound rules.
- If you create a custom NACL, both inbound and outbound rules are denied

## What is Port 80?
- Port number assigned to HTTP
- Port from which computer sends and receives web client-based communication and messages from a web server and is used to send and receive HTML pages.
- Any web/HTTP client (e.g web server) uses port 80 to send and receive requested web pages from a HTTP server.
- HTTP may use port 8080 to deploy a caching or proxy server.

## What is TCP?
- Network communication protocol designed to send data packets over the internet.
- TCP is transport layer, used to create a connection between remote computers by transporting and ensuring delivery of messages over supporting networks and the Internet.
- Ensures end to end delivery of data between distinct nodes.
- TCP works with Internet Protocol (define the local location of the remote node), TCP transports the data to the correct destination.
- TCP breaks large data into smaller packets and ensures that data integrity is intact.

## Rule numbers 
- Defines precedence
- Lowest numbered rules first, first match applies 
- E.g if I've got five rules, 1, 2, 3, 4, 5 and an action is being attempted, and rule 3 says it can be done, then that rule is going to apply and we don't have to process 4 and 5. But if rule 3 says the action is allowed but rule 2 says it not allowed, it will not be allowed.

## Security Groups 
- Instance
- Stateful, meaning if instance sends out request, it will also accept incoming those communications to back in.
- Define allowed traffic flows, the ingress (entrance) and egress (exit)
- They are virtual firewalls for your **instance** to control inbound and outbound traffic. 
- If you don't specify a security group, the instance is automatically assigned to the default security group for the VPC.

## Using SGs and NACLs in VPC
- Configuring SGs and NACLs in VPC help reduce attack surface of your applications hosted on AWS.
- They mutually complement each other, because SGs allow defining the traffic to resources within the applications
- NACLs allow defining the port, protocol, and source of traffic that should be explicitly denied at the subnet level.

## What is Amazon EC2 Instance?
- Amazon Elastic Compute Cloud, is a service, forms part of Amazon's cloud-computing platform that allow users to rent virtual computers on which to run their own applications.
- EC2 allows us to deploy virtual servers and manage storage through an [AMI](#ami)
- An EC2 instance is a virtual server known as instances in Amazon's Elastic Compute Cloud (EC2) for running applications on the **Amazon Web Services** infrastructure.
- **EC2** is a service that allows business subscribers to run application programs in the computing environment. 

## Why use an EC2?
1. For computing
- It lessens the needs to invest in hardware
- Helps streamline development processes
- Reduces time to boot new servers
- You can easily scale up the capacity 
- Flexibility with operating systems
- Auto-scaling tool to dynamically scale the capacity.

2. For networking
- To gain administrative control on the virtual networking for using an isolated section of the cloud.
- Provides load balancing tools like Network Load Balancer and Application Load Balancer

## How do you set up AWS EC2?
- Involves creating an AMI, which includes an operating system, apps and configurations
- That AMI is loaded to the Amazon Simple Storage Services (S3)

## AMI
- Preconfigured EC2 instances, allow you to quickly launch new EC2 based on configuration within AMI
- No need to install an OS
- Beneficial when implementing auto scaling and creating immutable infrastructure
- Packaged environments containing software configuration
- Machine images are like templates that are configured using an operating system (Linux, Mac, Windows)
- Amazon Machine Image
- A template to create virtual machines within the Amazon Elastic Compute Cloud.
- Template for the instance (e.g operating system, an application server), launch permissions, system architecture (whether is 32 or 64 bit) and storage
- Used to create virtual servers, which are called Instances.

### Types of Machine Images
- Public Images
    - Safe, secure, customised for public consumption
- Paid Images
    - Can be purchased from a developer
    - EC2 users can purchase images from the AWS marketplace, an online store that sells software running on Amazon Web Services.
- Private Images
    - Used by EC2 users who have been granted access to it by the developer.


![Anais_example_vpc](Terraform%20-%20AWS%20-%20Load%20Balancing%20-%20Eng67.Atang.VPC.png)
