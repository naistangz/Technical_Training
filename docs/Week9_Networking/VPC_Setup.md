# Working with AWS Networking and Amazon VPC

**Contents**
- [x] [What is a VPC](#what-is-a-vpc) :cloud:
- [x] [Why use a VPC](#why-use-a-vpc)
- [x] [Subnets](#subnet)
- [x] [Private and Public Subnets](#private-and-public-subnets)
- [x] [Public Subnet Prerequisites](#public-subnet-prerequisites)
- [x] [Private Subnet Prerequisites](#private-subnet-prerequistes)
- [x] [Internet Gateway](#igw)
- [x] [Routing Tables](#routing-table)
- [x] [Setting up a VPC](#setting-up-a-vpc)
- [x] [Setting up a Bastion Server](#setting-up-a-bastion-server-a-new-instance) :japanese_castle:

## What is a VPC?
- Reside inside the AWS Cloud 
- By default, when creating your VPC, the only person that has access to this is your own AWS account.
- It is totally isolated and no one else can gain access to your VPC other than your own AWS account.

## Why use a VPC?
- A Virtual Private Cloud allows you to deploy resources within your VPC, such as:
    - Different compute resources (e.g. CPU and memory) 
    - Storage 
    - Database 
    - Network infrastructure
- This allows you to build and deploy solutions within the Cloud.
- By default you are allowed up to 5 VPCs per region per AWS account
- To create your VPC, you can define an IP address range, in the form of a CIDR block (Classless Inter-Domain Routing)

## Subnet 
- Subnets allow you to segment your VPC infrastructure into multiple different networks
- They reside inside your VPC

## Why create subnets?
- To better manage your resources
- To isolate certain resources from others
- To create high-availability and resiliency within your infrastructure.
- When creating a VPC there are two pieces of information you need:
    - Name
    - [CIDR block address](#cidr-block)

## Private and Public Subnets
- When we create a VPC, we need to give it a CIDR block range
- We need to do the same with our subnets as well
- A **public subnet** is accessible from outside of your VPC e.g the Internet.
- For any resources created within your public subnet e.g. web servers, would be accessible from the Internet
- A **private subnet**, for example your backend databases, would be inaccessible by default from the Internet.
- In order to make a subnet public or private, you have to add an Internet gateway.
- The **main difference** is the **route** the traffic takes out to the Internet - the Internet Gateway of the NAT Gateway.

## Public Subnet Prerequisites
- The public subnet hosting the bastion instance must have the following:
- [x] An Internet Gateway for SSH server responses to the SSH Client.
- [x] A Routing Rule in the subnet's Route Talbes directing SSH responses to the Internet Gateway.
- [x] A compute instance with access to the app-server
- [x] An SSH public key corresponding a private key on the SSH client.
- [x] An Ingress rules allowing access to port 22. Port 22 is the default for SSH

## Private Subnet Prerequistes
- The private subnet hosting the app-server must have the following.
- [x] A compute Instance with access back to the bastion host.
- [x] An SSH public key corresponding to a private key on the SSH client.
- [x] An Ingress rule allowing access to port 22.

## IGW
- An Internet Gateway is a managed component by AWS that is attached to your VPC and acts as a gateway between your VPC and the outside world.
- An IGW is a transparent component. It does not have an IP address of its own, and is not a component that you need to manage.
- **Note**: For an EC2 instance to talk to the outside world, instances must be located on a subnet that has a route defined to the IGW, **and** there must be a public IP address (Elastic IP - a reserved public IP address)
- This is **mandatory** to enable **bi-directional** communication between the outside world and the instances. 
- Serves as a bridge between our isolated VPC to the Internet by the IGW which is managed by AWS.
- Before the public subnet can access the Internet, we need to add a route to the public subnet's route table.
- Associated with every subnet when it is created will also be an associated route table.
- You can have the same route table associated to multiple subnets.
- You **cannot** associate more than one route table to a single subnet.

## CIDR block
- The **CIDR block address** is a range of IP addresses and this CIDR block range can have a subnet mask between a range of IP addresses from a `/16` all the way to a `/28`.
- E.g. We create our VPC with the following **CIDR** block `10.0.0.0/16`
- **Note:** Any subnets that we create within our VPC need to reside within this CIDR block range.

## Routing Table 
> Extracted from [Stratoscale](https://www.stratoscale.com/blog/cloud/vpc-for-dummies/)
> AWS Route Tables [Link](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Route_Tables.html?shortFooter=true)
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


## Setting up a VPC 
### Part I
1. Create AWS account [Here](https://aws.amazon.com/premiumsupport/knowledge-center/create-and-activate-aws-account/)
2. Navigate to Services, click on VPC
3. Choose Ireland Location
4. When choosing the area be aware it's not the same as availability zones.
5. Region, close cluster of data centres
6. Availability zones = within the region = logically connected but physically segregated data centres inside a region.

### Part II Create VPC
1. Create VPC
2. Choose description name tag
```bash
Eng67.Anais.VPC
```
3. Specify IPv4 CIDR block
```bash
123.11.0.0/16
```
**Note**: `/16` mask allows you to create subnets with a `/24` mask allowing you to create networks - each with 256 available IP addresses.

4. Select `No IPv6 CIDR Block`
5. Tenancy Default

## Creating an IGW
1. Create an Internet Gateway by navigating to VPC bar on the left.
2. Select a descriptive name tag 
```bash
Eng67.Anais.IGW
```
3. Go to actions on the right and attach IGW to the VPC we have just created

## Creating Public and Private Subnets
### Public Subnet
1. Navigate to VPC bar and create subnet
2. Use descriptive name tag e.g.
```bash
Eng67.Atang.Subnet.Public
```
3. Assign your VPC
4. Choose no preference for availability zone
5. Select IPv4 CIDR block:
```bash
123.11.1.0/24
```
5. Click create

### Private Subnet
1. Follow the same steps for public subnet using descriptive name tags
```bash
Eng67.Atang.Subnet.Private
```
2. Type following IPv4 CIDR block:
```bash
123.11.2.0/24
```
3. Click create

## Creating a route table
1. Navigate to Route Table Option from VPC bar
2. There should already be a default Route Table by typing in your VPC ID.
3. Create new route table with descriptive name tags
```bash
Eng56.ATang.Route.Public
```
4. Assign VPC 
5. Once created edit routes
6. Add 0.0.0.0/0 to the Destination and your IGW as Target
7. Add 123.11.0.0/16 to the Destination and local as Target.
8. Save Routes
9. Click on Subnet Associations and assign public subnets to your public route and private subnets to your private route.

Do the same with a private route main but once you have configured the instance (e.g mongo.conf), close internet access by going to edit routes and removing IGW target.

## Creating a Network ACL
### Rules Public 
1. Navigate to Network ACL under security
2. Enter descriptive name tag
```bash
Eng67.ATang.NACL.public
```
3. Click create then edit inbound rules:
```bash
Rule    Type              Protocol    Port Range     Source                                    Allow/Deny
100     HTTP(80)          TCP(6)      80             0.0.0.0/0                                 Allow
110     HTTPS(443)        TCP(6)      443            0.0.0.0/0                                 Allow
120     Custom TCP Rule   TCP(6)      1024-65535     0.0.0.0/0                                 Allow
130     Custom TCP Rule   TCP(6)      22             Personal IP                               Allow
140     Custom TCP Rule   TCP(6)      27017          123.11.2.0/24                             Allow
150     Custom TCP Rule   TCP(6)      1024-65535     123.11.2.0/24 (CIDR Private Subnet IP)    Allow
```
4. Edit Outbound rules then click save:
```bash
Rule     Type             Protocol    Port Range     Destination    Allow/Deny
101      ALL TCP          TCP(6)      ALL            0.0.0.0/0      Allow
```

5. Click on subnet associations and edit subnet associations. 
6. Select Public Subnet.
7. Create new EC2 Instances and select the VPC and subnet you created in the `Network` and `Subnet` settings in `Step 3: Configuring Instance Details`

**Ingress Rule:**
- Allow port 80 
- Allow port 443
- Allow port 22 on range of IPs
- Allow ephemeral ports 


## Testing using Mac Terminal
1. Connect to the EC2 Instance with VPC
2. In terminal, `ssh` into the instance by typing in the following command:
```bash
ssh -i "private_key.pem" ubuntu@34.245.71.30
```
3. Install web server `nginx`
```bash
sudo apt-get install nginx
```

4. Type in the following IP into the browser to verify that `nginx` has been installed successfully:
```bash
34.245.71.30
```

## Setting up a Bastion Server (a new instance)
### Introduction :japanese_castle:
> Extracted from [Cloud Academy](https://cloudacademy.com/blog/aws-bastion-host-nat-instances-vpc-peering-security/)

Bastion host or server is an **instance** that is **provisioned** with a **public IP address** and can be accessed via **SSH**. Once set up, the bastion host acts as a **jump server** allowing secure connection to instances provisioned **without a public IP address**.

Access to the private subnets and regular internet access from the servers, e.g. for software installation, will only be allowed with a special maintenance **security group** attached to those servers.

<img src="https://cloud.ibm.com/docs-content/v1/content/b013743f65e5c455bad277431a84cb77fc2431d5/solution-tutorials/images/solution47-vpc-secure-management-bastion-server/ArchitectureDiagram.png">

- [x] After setting up required infrastructure (subnet, security groups, etc) on the cloud, the admin connect (SSH) to the bastion host using the private SSH key.
- [x] The admin assigns a maintenance security group with proper outbound rules.
- [x] **SG** Inbound and Outbound traffic must be **restricted** at the protocol level as much as possible
- [x] **SG** Inbound rule base should accept SSH or RDP connections only from the specific IP addresses (admin IP), AVOID wide open access (0.0.0.0/0)
- [x] **SG** Outbound connection should also be restricted to SSH (secure shell) or RDP (remote desktop) access to private instance.
- [x] The admin connects (SSH) securely to the instance's private IP address **via** the bastion host to install or update any required software e.g. a web server
- [x] The internet user makes an HTTP/HTTPs request to the web server

## Steps
- Create New Instance (Bastion Server)
- Create new security group
- Allow SSH on port 22 from this IP address.
    - This means that any instances associated to this security group allow inbound SSH from any resource sitting within this security group, which is associated to our bastion host.
    - This will allow the bastion host SSH access to these instances.
- Securely copy private key into Bastion instance using the following command:
```bash
scp -i ~/.ssh/DevOpsStudents.pem DevOpsStudents.pem ubuntu@52.19.173.136:/home/ubuntu/.ssh
```
- `ssh into bastion with bastion public ip` using private key. The connection will come through the IGW (internet gateway).
- `ssh into db instance with private ip` to access our private subnet.

1. Navigate to AWSNodeAPPipeline folder
```bash 
cd AWSNodeAPPipeline
```
2. Enter following to link files (app folder and provision file) in OS to app 
```bash
scp -i ~/.ssh/privatekey.pem -r ~/PycharmProjects/AWSNodeAppPipeline/environment/app/ ubuntu@54.78.57.81:/home/ubuntu/environment
scp -i ~/.ssh/privatekey.pem -r ~/PycharmProjects/AWSNodeAppPipeline/app/ ubuntu@54.78.57.81:/home/ubuntu/
```
3. SSH into App on VPC:
```bash
ssh -i "privatekey.pem" ubuntu@54.78.57.81
```
4. Run the `provision.sh` file in `environment/app` to install all packages (`npm`, `nginx`, etc):
```bash
provision.sh
```

5. `cd` into app to run `app.js`
```bash
cd ~/app
pm2 start app.js
```

6. Enter the IP address into the browser (with reverse proxy working correctly) to see the app working:
```bash
54.78.57.81
```

![App VPC Successfully working](app_vpc_success.gif)