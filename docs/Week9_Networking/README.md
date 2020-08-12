# Networking and Configuration Management
# N-tier Architecture vs Monolith :computer:

**Contents**
- [x] [What is a Network?](#what-is-a-network)
- [x] [What is an IP?](#what-is-the-maximum-ip-in-ipv4)
- [x] [Understanding IP addresses](#understanding-ip-addresses)
- [x] [Subnets](#subnet)
- [x] [Understand Subnetting](#why-use-subnetting)
- [x] [What a maximum IP in IPV4?](#what-is-the-maximum-ip-in-ipv4)
- [x] [IP and Binary - Demo Convert 1 IP into binary](#ip-and-binary---demo-convert-1-ip-into-binary)
- [x] [IP4 VS IPV6](#ipv4-vs-ipv6)
- [x] [Class Networks](#class-networks)
- [x] [Classless Inter-Domain Routing](#cidr)
- [x] [Monolith Architecture](#monolith-architecture)
- [x] [N-Tier Architecture](#n-tier-architecture)
- [x] [Virtual Private Cloud](#vpcs)
- [x] [Virtual Private Networks](#vpns)
- [x] [IGW Internet Gateways](#igws) 
- [x] [NACLs](#nacls-network-access-control-lists)
- [x] [Route Tables](#routing-table) 
- [x] [SGs Security Groups](#sg-security-groups-ec2)

> Network [PDF](https://www.ece.uvic.ca/~itraore/elec567-13/notes/dist-03-4.pdf)\
> [Setting up a VPC on AWS](VPC_Setup.md)

## What is a network?
- Consists of two or more computers that are linked in order to share resources (e.g printers and CDs), exchange files, or allow electronic communications.
- These computers on a network can be linked through cables, telephone lines, radio waves, satellites, or infrared light beams.
- There are two common types of networks include:
    - [Local Area Network (LAN)](#LAN)
    - [Wide Area Network (WAN)](#WAN)
    
## What is an IP?
- Stands for internet protocol, is the internet's principal set of rules for communications.
- IP is part of an internet protocol suite, which also includes Transmission Control Protocol [(TCP)](#tcp)
- The IP governs rules for packetising, addressing, transmitting, routing and receiving data over networks.
- An IP address has two parts - one part **identifies the host**, such as a computer or other device. The other part **identifies the network it belongs to**. [TCP/IP](#tcpip) uses a subnet mask to separate them.
- 1) The Network ID 
- 2) The Host ID

## Understanding IP addresses
- Address used to uniquely identify a device on an IP network.
- An address is made up of 32 binary bits, which can be divisible into a network portion and host portion with the help of a subnet mask.
- 32 binary bits are broken into four octets (1 octet = 8 bits).
- Each octet is converted to decimal and separated by a dot.
- The value in each octet ranges from 0 to 255 or 00000000 - 11111111 binary.

## What is IPv4?
- The fourth version of the internet protocol
- Uses 32-bit IP address (each number between each dot, is a byte. One byte as 8 bits)
- **IPv4** was invented in the 1970s as the first major version of internet protocol.


## What is the maximum IP in IPv4?
- With 32 bits the max number of **IP addresses** is **2 to the power of 32** and contains **4,294,967,296** IPv4 addresses
- There are 588,514,304 reserved addresses therefore, there are **3,706,452,992** public addresses.


## IP and Binary - Demo Convert 1 IP into binary 
- Binary is a base-2 number system, made up of two numbers: 0 and 1
- Computers interpret IP addresses in binary.
- Computers think in binary, meaning everything is described using two values or states: on or off, true or false, yes or no, 1 or 0.

An IP address provide a numeric identify to an interface. The address is used with a subnet mask. Without a subnet mask, an IP address is an ambiguous address and without IP address a subnet mask is just a number.
Both addresses are 32 bits in length. These bits are divided in four parts. 
The calculation direction is **Left to Right**

Example IP address: 192.168.0.1

**192**
Position value|Comparison|Value in Binary
---|---|---
128|128 < 192|1
64|128+64 = 192 == 192|1
32|192+32 = 224 > 192|0
16|224 + 16 = 240 > 192|0
8|240 + 8 = 248 > 192|0
4|248 + 4 = 252 > 192 | 0
2|252 + 2 = 255 > 192 |0
1|255 + 1> 192| 0

Which gives:
```bash
11000000.10101000.00000000.00000001
```

## IPv4 vs IPv6
- IPv4 is 32-Bit
- IPv6 is 128-Bit
- All 4.29 billion IP addresses have now been assigned, leading to the address shortage issues we face today. 
- Number of IPv6 addresses is 1028 times larger than the number of IPv4 addresses
IPv6 hexadecimal better suited to mobile networks
- **Problem of only having 4B IPs**:

## LAN
- Local Area Network. 
- A computer network that interconnects within a limited area such as a residence, school, laboratory, university campus or office building.
- Examples of LAN tech: Ethernet, Token Ring, Fibber, Distributed Data Interconnect (FDDI)

## WAN
- Wide Area Network. 
- A telecommunications network that extends over a large geographical area for the purpose of computer networking. 
- A `WAN` can cover country, continent or even a whole world. 
- The **internet** is the world's largest `WAN`.
- Examples of WAN tech: Asynchronous Transfer Mode (ATM), Integrated Services Digital Network (ISDN)

## TCP/IP
> Extracted from [avast](https://www.avast.com/c-what-is-tcp-ip)
- Computers communicate with each other through TCP/IP. 
- TCP/IP is typically built into computers and is largely automated
- Stands for Transmission Control Protocol/Internet Protocol
- They are a set of rules that allow computers to communicate on a network such as the Internet.
- Humans use social protocols to know how to behave and communicate with other people, technologies also set communication rules, e.g. the telegraph using Morse code or a CB radio using codes like "10-4."
- Communication was more complicated when people started to exchange information between its owns computers but didn't enable communication with other vendors' computers.
- The **agreed-upon** standard was needed that permitted computers from all vendors to communicate with each other (TCP/IP)

**IP** is the part that obtains the address to which data is sent
**TCP** is responsible for data delivery once that IP address has been found
The `IP address` is like the phone number assigned to your smartphone. `TCP` is all the technology that makes the phone ring, and that enables you to talk to someone on another phone. They are different from one another, but they are also meaningless without one another. 

## Subnet
## What is a Subnet?
- A subnetwork or **subnet** is a subdivision of an IP **network**.
- A smaller network inside a large network.
- Subnetting makes network routing much more efficient e.g a large network might want to have smaller networks inside of it... such as one department (e.g accounting) of a business.
- Subnetting allows a network administrator break a network into 'subnets', allowing them to connect more people to the network without getting more IP addresses.
- A subnet can be configured as a VPN-only subnet by routing traffic via [virtual private gateway.](https://docs.aws.amazon.com/vpn/latest/s2svpn/VPC_VPN.html)

## Subnetting
- Process of splitting a CIDR block into smaller CIDR blocks within the same range by using different subnet masks.
- Subnetting enables you to create smaller networks using a smaller CIDR range from your larger network IP address space.
- **For example** if you had a CIDR block range of: 
```bash
10.0.0.0/16 
```
This is a large IP range to have as a single network as it allows for up to 65,534 hosts (256 * 256 * 256).\
To make better use of this range and to create smaller networks allowing segmentation within your network you could subnet the `CIDR` block into smaller `CIDR` ranges using a different subnet mask, such as `/17` for each subnet. 

## What is a Subnet mask?
- A 32-bit (8 by 4) combination used to describe which portion of an address refers to the subnet and which part refers to the host
- A byte = 8 bits 
- Class A, B, and C networks have default masks, also known as natural masks:
- For each class, different numbers of octets (four numerical blocks of IP addresses) are used to identify the networks.
- The remaining octets determine the number of hosts in a network. 
```bash
Class A: 255.0.0.0
Class B: 255.255.0.0
Class C: 255.255.255.0
```

## CIDR
- Classless Inter-Domain Routing
- `CIDR` is based on the idea of [subnet masks](#subnet). A mask is placed over an IP address and creates a sub network: a network that is subordinate to the internet.
- The subnet mask signals to the router which part of the IP address is assigned to the hosts and which determines the network.

An IP address on Class A network that has not been subnetted would have an address/mask pair similar to 8.20.15.1 255.0.0.0

Converted IP addresses:
```bash
8.20.15.1 = 00001000.00010100.00001111.00000001
255.0.0.0 = 11111111.00000000.00000000.00000000
```

This helps identify the network and the host ID. The address bits which have corresponding mask bits set to 1 represent network ID. The mask bits set to 0 represent node ID.
```bash
8.20.15.1 = 00001000.00010100.00001111.00000001
255.0.0.0 = 11111111.00000000.00000000.00000000
            -----------------------------------
             net id |      host id    
```

Submask 
A second IP that tells you where to match IPs to be in the same network
Computer A 192.65.63.1
Computer B 190.65.30.1
Submask 
If 255.0.0.0 Then not on same network 
If 0.225.0.0 Then on same network

Max number 255

255.255.255.255 entire availability 
256 * 256 * 256 * 256 = approx 4B

## What is an interface?
- A network connection 

## Class Networks 
When planning for IP addressing on your network, you have to determine which network class is appropriate for your network.
- Networks are categorised by class:
- **Classes A, B, C, and D**

## N-Tier Architecture 
Aka **Multi-tier architecture** or **multilayered architecture**. **N-Tier** architecture is a client-server architecture in which presentation, application processing and data management functions are physically separated. They provide a model by which developers can create flexible and reusable applications. A typical `n-tier` application includes a presentation tier, a middle tier, and a data tier.
- **Layer 1: Presentation Logic** Typically hosted on front-end Web servers. User interface. 
- **Layer 2: Business Logic** Hosted on mid-tier application or general-purpose servers
- **Layer 3: Database Management** - Hosted on back-end database servers
- 3-tier means Presentation Layer + Component Layer + Data access layer
- N-tier is when additional layers are added beyond these, usually for additional modularity, configurability.

<img src="https://upload.wikimedia.org/wikipedia/en/6/66/Overview_of_a_three-tier_application.png" alt="n-tier-diagram">


### Layer 1 The presentation tier
- User interface
- The go-between for the data tier and the user, passing on the user's different actions to the logic tier
- CSS, Javascript, HTML
- If you need to log in, the presentation tier will show you boxes for username, password, and the submit button.
- When you submit the form, this will be passed on to the logic tier.

### Layer 2 The Logic Tier
- The logic tier will have the JSP, Java Servlets, Ruby, PHP and other programs.
- This is run on a web server. 
- Business logic - like validation of data, calculations, CRUD operations 
- This tier makes communication faster and easier between the client and data layer
- Defines the workflow activity that is necessary to complete a task. 


### Layer 3 The Data Tier
- This is the database, such as MySQL, NoSQL or PostgreSQL database
- These run on a separate database server

## How does this differ from MVC framework?
- N-tier architecture has a middle layer or a logic tier, which facilitates all communications between the different tiers.
- In an MVC framework, the interaction is triangular. Instead of going through the logic tier, it is the control layer that accesses the  model and view layers, which the model layer accesses the view layer.
- The control layer makes a model using the requirements and then pushes that model into the view layer. 

## Benefits of N-Tier Architecture
- Separating application components into separate tiers increases the maintainability and scalability of the application
- It does this by enabling easier adoption of new technologies that can be applied to a single tier without the requirement to redesign the whole solution
- N-tier applications typically store sensitive information in the middle-tier, which maintains isolation from the presentation tier. 
- **Secure:** You can secure each of the tiers separately using different methods
- **Scalable:** You can add more resources without affecting the other tiers.
- **Flexible:** You can expand each tier in any manner that your requirements dictate. 

## Monolith Architecture
- A traditional model for software in which the structure is a single and indivisible unit. A monolith has one code base with multiple modules.

## Disadvantages of Monolith architecture
- A large code base can be harder to understand
- IDE (integrated development environment) can become overloaded, and size may also slow down startup time.
- Every element is closely related and dependent on the others, so it is difficult to change to a new or advanced technology, language, or framework
- Updating can be a challenge
- Problems with scalability, because each element has different resource requirements 

<img src="https://divante.com/blog/wp-content/uploads/2020/01/Frame-1.png">

## VPCs
> Extracted from [Prasad Vara](https://www.infoq.com/articles/aws-vpc-explained/)
### What is a VPC?
- A virtual private cloud (VPC) is your own private data center within the AWS infrastructure. 
- It is your own isolated segment of the AWS Cloud
- By default, when creating VPC, only your AWS account has access to it.
- There are millions of VPN but they do not have access to your VPC, vice versa.
- Since this is your network, you can decide to slice it up any way you prefer.

### Why use a VPC?
- Allows you to start deploying resources e.g compute resources, database, network infrastructure
- By default, you are allowed five VPCs per region per AWS account.
- To create a VPC, you give it a name and define an IP address range that the VPC can use. 
- This is done in the form of a CIDR block (Classless Inter-Domain Routing)
- VPC isolated segment of the AWS public cloud which allows you to provision and deploy resources in a safe and secure manner. 

For example, you can decide that your VPC network will be 192.168.0.0/15 which can accommodate **65,536** (256 * 256) different IP addresses and 256 different [subnets](#subnet).

### What is inside a common 2 tier VPC?
1. **Web Tier**
2. **Database Tier**

<img src="https://d1o2okarmduwny.cloudfront.net/wp-content/uploads/2014/11/Diagram-674x577.png">

### How does it relate to networks?
- When creating a VPC, you want to create subnets in your VPC. 
- Subnets are like containers within your VPC that segment off a slice of the CIDR block you define in your VPC (Classless Inter-Domain Routing)
- Subnets give different access rules and places resources in different containers where those rules should apply. 
- E.g you would not have a big open window in your bathroom, much like you would not put a database with secretive information in a public subnet allowing any and all network traffic. You would want to put that database in a private subnet. 
- Subnetting enforces a greater level of security.
- Logical grouping of similar resources also helps you to maintain an ease of management across yoru infrastructure.
- Creating subnets allow you to create a logical network division between your resources e.g. subnet for database instances, subnet for application servers, a subnet for web infrastructure.

## Enforcing security with subnets
- By having multiple Subnets with similar resources grouped togethers, it allows for greater security management. 
- You can create private subnets by implementing network level virtual firewalls, called network access control lists, or NACLs, making it possible to filter traffic on specific ports from both an ingress and egress point at the Subnet level.
 
<img src="https://i.stack.imgur.com/plsWk.png" alt="VPC_with_public_private_subnet">
 
https://stackoverflow.com/questions/45164355/what-is-vpc-subnet-in-aws

## VPNs
- Virtual Private Network.
- A VPN can allow users to exhange data efficiently across shared or public networks, as though they are directly linked to the private network

## IGWs
- An Internet Gateway is a managed component by AWS that is attached to your VPC and acts as a gateway between your VPC and the outside world.
- An IGW is a transparent component. It does not have an IP address of its own, and is not a component that you need to manage.
- **Note**: For an EC2 instance to talk to the outside world, instances must be located on a subnet that has a route defined to the IGW, **and** there must be a public IP address (Elastic IP - a reserved public IP address)
- This is **mandatory** to enable **bi-directional** communication between the outside world and the instances. 
- Serves as a bridge between our isolated VPC to the Internet by the IGW which is managed by AWS.
- Before the public subnet can access the Internet, we need to add a route to the public subnet's route table.
- Associated with every subnet when it is created will also be an associated route table.
- You can have the same route table associated to multiple subnets.
- You **cannot** associate more than one route table to a single subnet.

## NACLs (Network Access Control Lists) 
- Virtual network-level firewalls that are associated to each and every subnet
- Help control both ingress and egress (incoming, outbound) traffic moving in and out of your VPC and between your subnets.

## SG Security Groups EC2
- Firewall at EC2 level
- Responsible for controlling the traffic in and out of your instances.

## AWS - Difference between Security Groups and Network ACLs
**TL;DR**
Security group is firewall of EC2 instance, Network ACL is firewall of subnet

**Subnet or EC2 instance?**\
- SGs are tied to an instance whereas Network ACLs are tied to the subnet level
- Instances in the subnet with an associated NACL will follow rules of NACL.
- SGs have to be assigned explicitly to the instance, meaning any instances within the subnet group gets the rule applied.

## Routing Table
- A **routing table** or **routing information base (RIB)**, is a data table stored in a router or a network host that lists the routes to particular network destinations.
- A set of rules, often viewed in table format, that is used to determine where data packets travelling over an [IP](#what-is-an-ip) will be directed.
- Also called the forwarding table.
- The place where routing information is stored 
- A routing table contains routing entries, which is a list of destinations (or a list of network prefixes or routes)
- In AWS, traffic within VPC does not need to be routed.
- A router takes care of this and the entries in this [router](#what-is-a-router) are controlled by you through Route Tables.
- When you want to access a resource outside of your VPC, - you route traffic through your IGW (for public instances) or through the NGW (for private instances).
- The route tables are associated with each of your subnets to allow the flow of traffic according to the policies and options you have in place. 

## What is a router?
- Piece of network hardware that connects a local network to the internet.
- A router forwards data packets between computer networks.
- Routers perform the traffic direction functions on the Internet.
- Data sent through the internet, such as a web page or email, is in the form of data packets.
- A router is connected to two or more data lines from different IP networks. 
- A router directs incoming and outgoing internet traffic on that network in the fastest and most efficient way.


> Navigate [HERE](VPC_Setup.md) on setting up a VPC on AWS