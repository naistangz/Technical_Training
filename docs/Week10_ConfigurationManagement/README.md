# Ansible 

**Contents**
- [x] [Ansible](#ansible)
- [x] [Open-source](#-what-does-open-source-mean)
- [x] [What can Ansible automate?](#what-can-ansible-automate)
- [x] [Why Ansible?](#why-ansible)
- [x] [What is YAML](#what-is-yaml)
- [x] [What does agentless mean?](#what-does-agentless-mean)
- [x] [What is Configuration Management?](#what-is-configuration-management)
- [x] [What is Infrastructure as Code?](#-what-is-infrastructure-as-code)
- [x] [Terraform](#infrastructure-as-code-tools)
- [x] [How does Ansible fit into DevOps](#-how-does-ansible-fit-into-devops)
- [x] [Best practices of IaC](#best-practices-of-iac)

## What is Ansible?
- Ansible is an open-source, configuration management tool to **provision IT environments**, **deploy software** or be integrated to **CI/CD** pipelines.
- Ansible helps improve the scalability, consistency and reliability of your IT environment
- Ansible can automate repetitive system administration tasks
- Ansible uses SSH to push changes from a single source to multiple remote resources

## What does open-source mean?
- Software that is designed to be publicly accessible
- Anyone can see, modify, and distribute the code as they see fit.

## What can Ansible automate?
- **Provisioning**: Set up various servers (e.g Nginx web server) you need in your infrastructure
- **Configuration management**: Changes the configuration of an application, OS, or device; start and stop services; install or update applications; implement a security policy; or perform a wide variety of other configuration tasks.
- **Application deployment**: Make **DevOps** easier by automating the deployment of internally developed applications to your production systems.
- **Security and Compliance**:

https://www.edureka.co/blog/what-is-ansible/

## Why Ansible?
- Simplicity 
- Ansible uses **YAML**, a simple configuration language rather than **Ruby** which Puppet and Chef use.
- Ansible deployment is also agentless, meaning instead of installing an agent on every system you want to manage, Ansible just requires that systems have **Python (on Linux servers)** or **PowerShell (on Window servers) and SSH**
- Agentless means Ansible works by connecting to our virtual machines through SSH (by default).
- Ansible is a helpful tool that allows you to create multiple virtual machines and describe how these machines should be configured or what actions should be taken on them.
- Ansible issues all commands from a central location to perform these tasks.
- No other client software is installed and uses SSH to connect to the nodes.
- Only Ansible needs to be installed on the control machine (the machine from which you will be running commnads)
- It is **efficient**: No extra software, more resources for your applications. Ansible modules work via JSON, therefore Ansible is extensible with modules written in a programming language you're already familiar with.
- **Cost effective**: by building consistent ephemeral environments for staging, tests, or QA.

## What is YAML?
- Human-readable data serialisation language 
- Simple syntax, stands for Yet Another Markup Language 

## What does agentless mean?
- Refers to operations where no service, daemon or process needs to run in the background on the machine.
- Agentless doesn't require any agent to be installed for monitoring.
- You don't need to install software or firewall ports on the nodes that it manages.
- E.g you don't need to install Python, because it's already pre-installed in our Virtual Machine.
- No need to install dependencies

## What is Configuration Management?
- Chef, Puppet
- They help configure the software and systems on this infrastructure that has already been provisioned.
- It maintains configuration of the product performance by keeping a record and updating detailed information which describes an enterprise's hardware and software.

## What is Infrastructure as Code?
- Type of IT setup wherein developers or operations team automatically manage and provision technology stack for an application through software e.g. Ansible, rather than using a manual process to configure hardware devices and operating systems.
- Process of managing and provisioning computer data centers through machine-readable definition files e.g YAML or Ruby, rather than physical hardware configuration.
- Process of automating your infrastructure deployments

## Infrastructure as Code tools
1. Terraform
    - Provisioning tool 
    - Allows you to describe your infrastructure as code and creates 'execution plans' that outline exactly what will happen when you run your code.
    
## How does Ansible fit into DevOps?
> - Extracted from [TechBeacon](https://techbeacon.com/enterprise-it/infrastructure-code-engine-heart-devops)
- Simple IT automation, automating repeatable tasks like provisioning, configuration, and deployments for one machine or millions.
- Accelerates feedback loop
- Discover bugs sooner 
- More reliable deployments
- Ansible is agentless meaning no additional software or firewall ports are required and you do not have to separately set up a management infrastructure which includes managing your entire systems, network and storage.
- Ansible further reduces the effort required for your team to start automating right away.
- Ansible isn't just about automation. IaC requires DevOps practices to automation scrips to ensure they're free of errors, are able to be redeployed on multiple servers and can be rolled back in case of problems, and can be engaged by both operations and development teams.

## Best practices of IaC:
1.**Managing infrastructure via source control**, providing a detailed audit trail for changes.
2.**Applying testing to infrastructure** in the form of unit testing, functional testing, and integration testing.
3.**Avoid written documentation**, since the code itself will document the state of the machine. This is particularly powerful because it means, for the first time, that infrastructure documentation is always up to date.
4.**Enables collaboration** around infrastructure configuration and provisioning, most notably between dev and ops.

Steps in terminal
1. Create folder called ansible_demo:
```bash
mkdir ansible_demo
```
2. create vagrant file within the folder
```bash
cd ansible_demo
nano Vagrantfile
```
3. Configure vagrant file to set up virtual machines 
4. Vagrant up
```bash
vagrant up
```
6. Vagrant status to check all VMs are running
```bash
vagrant status
```
7. In each of the VMs sudo apt-get update by SSHing into each one
```bash
vagrant ssh web
vagrant@web:~$ sudo apt-get update
vagrant@web:~$ exit
```

```bash
vagrant ssh db
vagrant@db:~$ sudo apt-get update
vagrant@db:~$ exit
```

```bash
vagrant ssh aws
vagrant@aws:~$ sudo apt-get update
vagrant@aws:~$ exit
```

8. Then exit 
```bash
exit
```

9. Install ansible onto the controller by SSHing into the AWS VM
```bash
vagrant ssh aws
sudo apt-get install software-properties-common -y
sudo apt-add-repository --yes --update ppa:ansible/ansible
sudo apt-get install ansible -y
```

10. Ansible also requires a Python interpreter (in order to run its modules). Python may already be installed.
```bash
sudo apt-get install python -y
```

11. Check ansible has been installed 
```bash
ansible --version
```

12. Install `tree` package manager which is organises our files concisely.
```bash
sudo apt-get install tree -y
```

13. cd `/etc/ansible/`
```bash
$ tree
```

14. Use ping to test if a particular host is reachable
```bash
$ ansible web -m ping
```

15. The ping utility uses the echo request, and echoes reply messages within the Internet Control Message Protocol (ICMP)
```bash
ping 192.168.33.11
ping 192.168.33.12
```

**or**
 
```bash
ansible all -m ping
```

17. Type in `tree` and configure `hosts`
```bash
$ tree
$ sudo nano hosts
```

18. Type in following IP addresses in the default `hosts` file to connect to other VMs
```bash
[web]
192.168.33.10 ansible_connection=ssh ansible_ssh_user=vagrant ansible_ssh_pass=vagrant

[db]
192.168.33.11 ansible_connection=ssh ansible_ssh_user=vagrant ansible_ssh_pass=vagrant
 
[aws]
#192.168.33.12 ansible_connection=ssh ansible_ssh_user=vagrant ansible_ssh_pass=vagrant
```

19. Exit and SSH into the web and db VMs
```bash
sudo su 
ssh vagrant@192.168.33.10 
sudo apt-get update
exit
ssh vagrant@192.168.33.11
sudo apt-get update
exit
```

20. `ansible all -m ping` which should return:
```bash
root@aws:/etc/ansible# ansible all -m ping
[DEPRECATION WARNING]: Distribution Ubuntu 18.04 on host 192.168.33.11 should use /usr/bin/python3, but is using /usr/bin/python for backward compatibility with
 prior Ansible releases. A future Ansible release will default to using the discovered platform python for this host. See 
https://docs.ansible.com/ansible/2.9/reference_appendices/interpreter_discovery.html for more information. This feature will be removed in version 2.12. 
Deprecation warnings can be disabled by setting deprecation_warnings=False in ansible.cfg.
192.168.33.11 | SUCCESS => {
    "ansible_facts": {
        "discovered_interpreter_python": "/usr/bin/python"
    }, 
    "changed": false, 
    "ping": "pong"
}
[DEPRECATION WARNING]: Distribution Ubuntu 18.04 on host 192.168.33.10 should use /usr/bin/python3, but is using /usr/bin/python for backward compatibility with
 prior Ansible releases. A future Ansible release will default to using the discovered platform python for this host. See 
https://docs.ansible.com/ansible/2.9/reference_appendices/interpreter_discovery.html for more information. This feature will be removed in version 2.12. 
Deprecation warnings can be disabled by setting deprecation_warnings=False in ansible.cfg.
192.168.33.10 | SUCCESS => {
    "ansible_facts": {
        "discovered_interpreter_python": "/usr/bin/python"
    }, 
    "changed": false, 
    "ping": "pong"
}
```

Automating the steps by creating a script:
```bash
sudo apt-get install software-properties-common -y
sudo apt-add-repository --yes --update ppa:ansible/ansible
sudo apt-get install ansible -y
sudo apt-get install tree -y

cd /etc/ansible/ 
echo 
"[web]
192.168.33.10 ansible_connection=ssh ansible_ssh_user=vagrant ansible_ssh_pass=vagrant

[db]
192.168.33.11 ansible_connection=ssh ansible_ssh_user=vagrant ansible_ssh_pass=vagrant
" >> hosts

```