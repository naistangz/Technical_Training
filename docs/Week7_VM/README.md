# Vagrant

Contents

[Part I Working with Boxes](#what-is-vagrant)

1. [What is Vagrant?](#what-is-vagrant)
2. [Why use vagrant?](#why-use-vagrant)
3. [Using vagrant](#using-vagrant)
4. [Vagrant Features](#vagrant-features)
5. [Brief intro TCP/IP and DNS networking](#tcpip-and-dns-networking)

[Part II Configuring Boxes with Vagrant Files](#part-ii)
1. [Vagrant Files]
2. [Vagrant Synced folders]
3. [Vagrant networking]
4. [Vagrant providers]
5. [Vagrant provisioners]

[Part III Vagrant Use Cases]
1. [Application developer environment overview]
2. [Creating a developer environment]
3. [Vagrant multi-machine Vagrantfile]


## What is vagrant?
- Software written in Ruby for creating a full development environment within minutes
- From a developer's perspective, working on a software project, this involves setting up, installing and configuring multiple services.
- Most times, developers will be working in their own development environment entirely configured inside the laptop.
- This involves installing all the required dependency softwares on your laptop/workstation.
- This is time and resource intensive especially when dealing with modern web applications that has a lot of moving parts to it e.g web servers, application servers, backend API services, etc.

## Why use vagrant? 
- Preserve purpose-built isolated development environments.
- **Vagrant** allows users to maintain the application dependency configuration and environment completely in sync with other developers working in the project, regardless of what operating system are being used.
- Software dev envs depends on tools and libraries
    - As software versions age, tools and libraries are updated and older version are left behind.
    - 1-5 years later, any developer can run that VM and build that software version.
- Makes environments portable
- Makes it very easy to create and share virtual appliances through Vagrant Cloud.
- **Vagrant** achieves this, by leveraging virtualisation (creating a virtual hardware and running an operating system on top of another operating system, by slicing up the hardware). 

## Using Vagrant
- Vagrant is the layer on top of the virtualisation platform.
- Using vagrant, you can define all aspects of your development environment, which can be used for creating virtual machines.
- Vagrant takes care of creating, managing and destroying the development environment.
- The virtualisation platform of choice for vagrant is VirtualBox

# Vagrant Features
- Connect to a Vagrant VM
- Folder synchronisation 
- Networking
- Providers
- Provisioners
- Multi-machine Vagrantfiles

# TCP/IP and DNS Networking
**TCP/IP**
- Transport Control Protocol/Internet Protocol 
- They are a set of rules for communication between computers where each device (host) is assigned a unique IP address which is valid on a particular network.
- An IP address can be assigned statically or dynamically.

**DNS - Domain Name System**
- Every device on the Internet is assigned a 12 digit IP address
- DNS allows a domain name to be used as a pseudonym for a specific IP address
- When typing in a website, the system looks up the name on an assigned DNS server and resolves it to its IP address
- The `PING` command can be used to check if a domain name is resolving to an IP address, and if that IP address can be reached from your machine. 

## Running my first box
```bash
Anaiss-MBP:~ anaistang$ vagrant -v
Vagrant 2.2.9
Anaiss-MBP:~ anaistang$ cd ~
Anaiss-MBP:~ anaistang$ pwd
/Users/anaistang
Anaiss-MBP:~ anaistang$ mkdir myfirstbox
Anaiss-MBP:~ anaistang$ cd myfirstbox
```

**Initialising a Vagrant file**
```bash
Anaiss-MBP:myfirstbox anaistang$ vagrant init bento/ubuntu-16.04
A `Vagrantfile` has been placed in this directory. You are now
ready to `vagrant up` your first virtual environment! Please read
the comments in the Vagrantfile as well as documentation on
`vagrantup.com` for more information on using Vagrant.
Anaiss-MBP:myfirstbox anaistang$ ls
Vagrantfile
```

**Running the box with the** `vagrant up` **command**
```bash
Anaiss-MBP:myfirstbox anaistang$ vagrant up
Bringing machine 'default' up with 'virtualbox' provider...
==> default: Box 'bento/ubuntu-16.04' could not be found. Attempting to find and install...
    default: Box Provider: virtualbox
    default: Box Version: >= 0
==> default: Loading metadata for box 'bento/ubuntu-16.04'
    default: URL: https://vagrantcloud.com/bento/ubuntu-16.04
==> default: Adding box 'bento/ubuntu-16.04' (v202007.17.0) for provider: virtualbox
    default: Downloading: https://vagrantcloud.com/bento/boxes/ubuntu-16.04/versions/202007.17.0/providers/virtualbox.box
Download redirected to host: vagrantcloud-files-production.s3.amazonaws.com
==> default: Successfully added box 'bento/ubuntu-16.04' (v202007.17.0) for 'virtualbox'!
==> default: Importing base box 'bento/ubuntu-16.04'...
==> default: Matching MAC address for NAT networking...
==> default: Checking if box 'bento/ubuntu-16.04' version '202007.17.0' is up to date...
==> default: Setting the name of the VM: myfirstbox_default_1595623997739_10589
==> default: Clearing any previously set network interfaces...
==> default: Preparing network interfaces based on configuration...
    default: Adapter 1: nat
==> default: Forwarding ports...
    default: 22 (guest) => 2222 (host) (adapter 1)
==> default: Booting VM...
==> default: Waiting for machine to boot. This may take a few minutes...
    default: SSH address: 127.0.0.1:2222
    default: SSH username: vagrant
    default: SSH auth method: private key
    default: 
    default: Vagrant insecure key detected. Vagrant will automatically replace
    default: this with a newly generated keypair for better security.
    default: 
    default: Inserting generated public key within guest...
    default: Removing insecure key from the guest if it's present...
    default: Key inserted! Disconnecting and reconnecting using new SSH key...
==> default: Machine booted and ready!
==> default: Checking for guest additions in VM...
==> default: Mounting shared folders...
    default: /vagrant => /Users/anaistang/myfirstbox
```

- The `vagrant up` command firstly looks at the name of the box. We set the name of the box in the previous `vagrant init/ubuntu-16.04`
- This is a box name, and it refers to a box available on Vagrant cloud. 
- The **first part** of the name, Bento, is the organisation name.
- Bento, is the organisation name. The Bento boxes, are a collection of boxes for various distributions of the Linux operating system.
- The **second part** of the name is the distribution inversion.
- We are using Ubuntu 1604 Xenil Xerus distribution of Linus.
- Vagrant keeps a local cache of boxes that have been run on the computer.
- If the box has been run previously, and has not been removed, it will be that cache. 
- If not, Vagrant must first try to find the box and download it. 
- Vagrant boxes are stored in a compressed file which contains files specific to the provider for which they were built.
- Vagrant will download the box file from Vagrant cloud and unzip it to the local cache.

**Checking the status of our virtual machine when running in headless mode (running in the background with no visible user interface)**
```bash
Anaiss-MBP:myfirstbox anaistang$ vagrant status
Current machine states:

default                   running (virtualbox)

The VM is running. To stop this VM, you can run `vagrant halt` to
shut it down forcefully, or you can run `vagrant suspend` to simply
suspend the virtual machine. In either case, to restart it again,
simply run `vagrant up`.
```

`sudo apt-get update` command:
1. The `sudo apt-get update` command is used to download package information from all configured sources
2. The sources defined in `/etc/apt/sources.list` file and other files located in `/etc/apt/sources.list.d/` directory.
3. When you run update command, it downloads the package information from the Internet.
4. `apt` is a package manager.

`sudo apt-get update -y`
1. Automates updates  

`sudo apt-get upgrade` command:
1. New packages will be installed if required to satisfy dependencies, but existing packages will never be removed. 
2. Install outdated packages, apply security patches for packages and keeps your system secure.
3. `sudo apt-get upgrade` installs available upgrades of all packages currently installed on the system from the sources configured via `sources.list` file. 

**Listing the status of all Vagrant VMs on your machine (if there are multiple running on your system)**
```bash
Anaiss-MBP:myfirstbox anaistang$ cd ..
Anaiss-MBP:~ anaistang$ vagrant global-status
id       name    provider   state    directory                           
-------------------------------------------------------------------------
5c4f44b  default virtualbox poweroff /Users/anaistang                    
758fc47  default virtualbox running  /Users/anaistang/myfirstbox         
 
The above shows information about all known Vagrant environments
on this machine. This data is cached and may not be completely
up-to-date (use "vagrant global-status --prune" to prune invalid
entries). To interact with any of the machines, you can go to that
directory and run Vagrant, or you can use the ID directly with
Vagrant commands from any directory. For example:
"vagrant destroy 1a2b3c4d"
```

**Using** `vagrant halt` **to shut down a Vagrant virtual machine without having to change to its environment directory**
```bash
Anaiss-MBP:~ anaistang$ vagrant halt 758fc47
==> default: Attempting graceful shutdown of VM...
```

`Vagrant halt 758fc47` is the ID that was returned to us from the global status command

## Connect to Box
- By default, Ubuntu Server does not include a graphical shell
- Vagrant runs virtual machines in headless mode 
- Common method to connect remotely to Linux operating system is Secure Socket Shell (SSH)
- SSH uses cryptographic keys for authentication
- Vagrant configures boxes at start-up with a common security configuration and a standard key pair for `SSH authentication`.
- This makes it easy to connect via SSH through a Vagrant CLI command 
- Vagrant includes an SSH client that we can use to connect to boxes that support SSH

```bash
Anaiss-MBP:myfirstbox anaistang$ vagrant ssh
/Users/anaistang/.ssh/config: terminating, 1 bad configuration options
```

**Try:**

```bash
Anaiss-MBP:myfirstbox anaistang$ vagrant ssh-config > vagrant-ssh
Anaiss-MBP:myfirstbox anaistang$ ssh -F vagrant-ssh default
```

This command drops you into a full-fledged SSH session (connecting to machine via SSH)

```bash
Welcome to Ubuntu 16.04.6 LTS (GNU/Linux 4.4.0-185-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

 * "If you've been waiting for the perfect Kubernetes dev solution for
   macOS, the wait is over. Learn how to install Microk8s on macOS."

   https://www.techrepublic.com/article/how-to-install-microk8s-on-macos/

0 packages can be updated.
0 updates are security updates.



This system is built by the Bento project by Chef Software
More information can be found at https://github.com/chef/bento
vagrant@vagrant:~$ 
```


The prompt is no longer our Mac prompt. It is now the Ubuntu box connected remotely via SSH

**Experimenting with commands in the Ubuntu Box:**

**File system in this Ubuntu system
```bash
vagrant@vagrant:~$ ls
vagrant@vagrant:~$ cd /
vagrant@vagrant:/$ ls
bin   etc         lib         media  proc  sbin  sys  vagrant
boot  home        lib64       mnt    root  snap  tmp  var
dev   initrd.img  lost+found  opt    run   srv   usr  vmlinuz
```

`ifconfig` **command lists the network configurations of all the interfaces on the box:**
```bash
vagrant@vagrant:/$ ifconfig
eth0      Link encap:Ethernet  HWaddr 08:00:27:51:2c:84  
          inet addr:10.0.2.15  Bcast:10.0.2.255  Mask:255.255.255.0
          inet6 addr: fe80::a00:27ff:fe51:2c84/64 Scope:Link
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:542 errors:0 dropped:0 overruns:0 frame:0
          TX packets:402 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000 
          RX bytes:69114 (69.1 KB)  TX bytes:66028 (66.0 KB)

lo        Link encap:Local Loopback  
          inet addr:127.0.0.1  Mask:255.0.0.0
          inet6 addr: ::1/128 Scope:Host
          UP LOOPBACK RUNNING  MTU:65536  Metric:1
          RX packets:64 errors:0 dropped:0 overruns:0 frame:0
          TX packets:64 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1 
          RX bytes:5824 (5.8 KB)  TX bytes:5824 (5.8 KB)
```

**Disconnecting and terminating the SSH connection and returning to OSX prompt**
```bash
vagrant@vagrant:/$ exit
logout
Connection to 127.0.0.1 closed.
Anaiss-MBP:myfirstbox anaistang$ 
```

SSH is used to connect to a box to test installation and configuration management scripts or to run diagnostics on a box while a process is running. 
The Vagrant CLI includes Windows box connections commands for RDP, which is a remote desktop client and PowerShell.

## Halting and Destroying Boxes
```bash
Anaiss-MBP:myfirstbox anaistang$ vagrant halt
==> default: Attempting graceful shutdown of VM...
Anaiss-MBP:myfirstbox anaistang$ 
```
- The `vagrant halt` command will send a shutdown signal to the box. The guest operating system will attempt to `shut down gracefully`
- A box that has been shut down can be restarted with a `vagrant up` at any time

**Starting over in your environment:**
Changes made to the box that you want to discard, and start from initial state of the box as it was the first time it was booted.
```bash
Anaiss-MBP:myfirstbox anaistang$ vagrant destroy
    default: Are you sure you want to destroy the 'default' VM? [y/N] y
==> default: Destroying VM and associated drives...
Anaiss-MBP:myfirstbox anaistang$ 
```

- The `bento/ubuntu-16.04` box will be re-imported and started in its initial state.
- This box and all boxes on Vagrant Cloud are referred to as base boxes.
- They're intended as starting points
- Most vagrant use cases involve you as the user starting with the base box, then adding software and configuration to create a box fit for a particular purpose.

 # Part II
 ## Configuring Boxes with Vagrant files
 - Vagrant boxes are configured using a Vagrantfile 
 - They are ruby programs used by CLI (Command Line Interface) to set attributes of a Vagrant box such as CPU, memory, disk, and network configurations.
 
 ## Vagrant Synced Folders
 - Hypervisors (computer software, that creates and runs virtual machines) have the ability to synchronise a folder on the host operating system to a folder in a virtual machine.
 - The Vagrant synced folder feature exposes those hypervisor features and the synced folder section of the Vagrantfile is used to configure it.
 
 **Vagrantfile**
 ```bash
config.vm.synced_folder "filepath", "/home/vagrant/environment"
```
 
Synced folders have a range of uses. One common use is to map a folder between a box and a host containing the application code. A developer can edit code on the host system and the changes are synced to the box where it can be executed in an isolated runtime environment.

 ## Vagrant Networking
 - Port Forwarding
    - **Port:** A number between 1 and 65555 assigned to a TCP packet
    - **Known Ports:**
        - 21: FTP
        - 80: HTTP
        - 443: HTTPS/TLS
    - Vagrant can forward requests that are sent to a port on the host network to the same or different port on the box network.
    - This is known as forwarding or mapping ports between the host and box.
    - We install a web server to the Ubuntu box to see port forwarding in action (Nginx).     
 - Private Networks
    - Private networks use non-routable IP addresses to create isolated networks.
    - This is useful for security and testing purposes.
 - Public Networks