# AWS and Networking 

## Infrastructure as Code
- IaC, configures operating systems, networking, cloud services in the form of code, thereby treating it like software.

# Designing AWS Infrastructure
## 1. VPCs and Subnets
- At any core of any cloud infrastructure it a virtual private netware of cloud and the subnets you create within that network 
- You create **subnets** within your virtual private cloud with the intent of grouping resources that are going to be bound to certain routing rules
- These **routing** rules determine if your subnets are going to be public, private or isolated from traffic
- The goal is to have public and private subnets in different availability zones 
- **Public subnets** - route to internet gateway, allows traffic to and from internet into public subnets with public IP
- **Private subnets** - provide NAT gateways, these NATs or network address translation gateways are made to provide outbound internet access only
- **AWS CloudFormation** - service to build VPC, automatically declaresd CIDR blocks and understands the security that goes around those subnets so you don't have to.

## 2. Routing 
- Determines where network traffic is directed
- Provides way to allow network packets to be forwarded to correct destination.
- Implicit router is already linked to VPC when creating VPC.
- Routing allows you to control access in and out of your subnets.
- The only reason a subnet can be considered private or public is because of the network routing rules that you associate with it.
- **Private subnets** allow access to the internet, outbound only, meaning that service will be able to go to the internet to download features and patches for the operating system as needed. Not reachable for security reasons.
- **Public subnets** - Route table connects public subnets directly to IGW (internet gateway) that will allow traffic in and out of the internet to any resources that have a public IP address and are located within our public subnets.
- Building this routing by hand is complex, you need to create **route tables**, **route entries**, that will be going into those route tables.
- Also require **route table associations** to indicate which subnets will be bound to which rules.

## 3. Security Groups 
- Stateful
- Protect at instance level, act as firewall
- Manages inbound and outbound traffic
- When introducing a new resource, a new instance (server), it will require networking permissions to operate.
- Example: if we deploy web server into private subnet and in same stack we have a load balancer going into public subnet with a listener on port 80, we need to also open port 80 for ingress into web service security group.

## 4. Servers Load Balancing several servers
- Load balancers serve as entry points from internet and as mechanism to spread workload evenly across servers
- Web servers within a subnets can be managed by an autoscaling group

## 5. IGW, NAT Gateways
- IGW provides means to communicate out to internet
- IGW maintained by AWS
- Scales horizontally (adds more) automatically, classified as highly available component of VPC infrastructure. 
- Any subnet which has a route table associated that points to IGW is considered public subnet because it has connectivity.

## Scaling horizontally vs vertically vs availability 
- Horizontal - adding more machines 
- Vertical - adding more power (CPU, RAM) to existing machine
- Availability - probability that a system is operational at given time, the amount of time a device is operating as a percentage of total time it should be operating 

# What on earth is port 80?!
## Ports are constructs 
- Ports are software constructs 
- They live in software that's written to run on devices that interconnect to each other over the internet, specifically any TCP/IP based network 
- TCP/IP is just a protocol, the language that defines how computers talk to each other over a network.

## Computers talking to one another 
- When we go to a web page from a website like [www.google.com](www.google.com) the following takes place:
    - Web browser e.g Chrome, Firefox turns [www.google.com](www.google.com) into the IP address of the computer out there on the internet that holds the website.
- The internet is about numbers
- Once string [www.google.com](www.google.com) is converted into an IP address, e.g `67.225.235.59`, that number helps to route our request (client) to that server.
- Our ISP (internet service provider) uses IP address to find location of server.

## Servers
- They are just end point computers
- They serve web pages, send and receive email, manage databases, upload and download files.
- In order for servers to understand what we want, port numbers tell the server **what** it is you want to do. 
- Port 80 by default informs the server that it is a requesting for web pages using HTTP. 
- Port numbers were arbitrarily standardised. Port 80 used to standardise representation of web pages.

## Different ports for different tasks
- Connecting to server to send email `port 25`
- Connecting to server to download file while using FTP (file transfer protocol) `port 21`
- Connecting to server via SSH to perform remote administration `port 22`
- Connecting to server to request an encrypted web page using https `port 443`
- We do not need to know about these ports because the software we use, our web browsers, email programs, etc already know which port to use for what kind of request.
- Ports are just standardised numbers that's included in a request that our computer makes of another computer to identify what kind of request it is. 
