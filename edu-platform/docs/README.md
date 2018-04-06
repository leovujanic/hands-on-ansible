# Educationx platform

This is show case of small web platform managed with  **Ansible**. I will show you how to create 3 different servers, running on [DigitalOcean](https://www.digitalocean.com/) droplets. The first server is a web server, a reverse proxy to the app server. App server hosts simple python application and connects to DB server running mysql. I will use my laptop as control machine.

> **Note:** This example is a product of following Ben's IT Lessons tutorial.


# Preparation

1. Create 3 droplets on DigitalOcean - for this purpose, I used [Ubuntu 16.04.4 LTS (Xenial Xerus)](http://releases.ubuntu.com/16.04.4/)

2. Change password for root user and create new user

		adduser leonardvujanic && usermod -aG sudo leonardvujanic

	and test it with

		 su - leonardvujanic

3. Ensure that minimal subset of the Python language is installed on the server

	    sudo apt-get update && apt-get -y install python-minimal

4. Add remote hosts names to your host file (ip or domain can be used also)
5.	Create ssh key on your control machine

	    ssh-keygen

6. Copy key to remote server

	    ssh-copy-id hostname-of-target-server

7. Install Ansible on control machine

## Ansible Installation
On mac install use `brew install ansible` or install it with pip as follows:

    mkdir edu-platform  && cd edu-platform

Create python virtual environment

    virtualenv .venv
    
and activate it

    source .venv/bin/activate

Install Ansible with pip

    pip install ansible

Installation can be tested `ansible --version` command

Use `deactivate` to deactivate virtual environment


## Configuration and files structure

