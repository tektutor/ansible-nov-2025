# Day 3

## Info - What is the motivation to use Ansible? Why can't we use Powershell or Python or Batch files etc to automate?
<pre>
- Programming languages are broadly classified into 2 types
  1. Imperative Programming Language
     - We need to write code to instruct what we wanted to automate
     - We also need to write code to instruct how to perform the automation
     - examples
       - C/C++/Python/C#, Powershell, Shell scripts are all imperative languages
  2. Declarative Programming Language
     - We just need to tell what we wanted to automate, the tool will take care of how to do it
     - examples
       - Ansible
       - Puppet
       - Chef
- Hence, Ansible or any Configuration Management Tool must be used to automate the Configuration Management in the
  place of Shell scripts or Powershell.
- As Ansible,Puppet, Chef are Idempotent
- the meaning of Idempotent is
  - For instance
    - when we run an ansible playbook to install latest version of nginx first time
    - ansible will check the ubuntu1 and ubuntu1 nodes, if it finds nginx is not installed already, it will install latest version of nginx and report in yellow color i.e Success with change
    - next time when you run the same playbook on ubuntu1 and ubuntu2, this time ubuntu1 and ubuntu2 will already have latest version
      of nginx, as Ansible is smart enough(idempotent) it will not attempt to reinstall, instead it reports the automation was a success and report in green color ( sucess with no change as your server was already in the desired state )
    
</pre>  

## Info - Linux Package Manager
<pre>
- Package Manager is a tool that is used in Linux to install/uninstall, update softwares
- Package Manager abstracts all the complexities from the end-user
  - package manager knows the url from where the softwares can be downloaded and installed
  - package manager knows which Linux family, which OS version and bitness(32/64) you are using
  - package manager the compatible installer binary and installs that for you on your OS when requested
- There are many Linux Families
  - For example
    - Red Hat Linux Family
      - Fedora
      - CentOS Stream
      - Rocky Linux
      - Red Hat Enterprise Linux
    - Debian Linux Family
      - Kali Linux
      - Ubuntu
      - Rasbian
  - Each Linux Family supports specific package manager utilities
  - For instance,
    In Red Hat Linux Family
    - rpm - Red Hat Package Manager
    - yum - Package Manager
    - dnf - dandified yum package manager ( improved yum package manager - supported from RHEL 9 onwards )
    In Debian Linux Family
    - apt/apt-get package manager is supported
    - snap
- Unlike Microsoft Windows OS
  - where it is responsibility of the end-user to find the website of installer exe
  - it is also the repsonsibility of the end-user to download the correct compatible installer exe
  - assume your Windows OS is 32-bit OS, 64-bit installer exe will not work on Windows 32-bit OS

</pre>

## Lab - Install nginx web server onto Ubuntu1 and Ubuntu2 Ansible node containers using Ansible Playbook
```
cd ~/ansible-nov-2025
git pull
cd Day3/ansible
cat install-nginx-playbook.yml
ansible-playbook -i inventory install-nginx-playbook.yml
curl http://localhost:8001
curl http://localhost:8002
```

<img width="1920" height="1168" alt="image" src="https://github.com/user-attachments/assets/abdc83e7-5a2b-4199-90b2-916c333cb996" />
<img width="1920" height="1168" alt="image" src="https://github.com/user-attachments/assets/2b87ead5-a332-404c-9aab-42b1f20d88b6" />
<img width="1920" height="1168" alt="image" src="https://github.com/user-attachments/assets/84aa670b-d537-4a72-9ae6-97209918b529" />
<img width="1920" height="1168" alt="image" src="https://github.com/user-attachments/assets/86503bc1-5443-4650-bf11-189f4e281661" />
<img width="1920" height="1168" alt="image" src="https://github.com/user-attachments/assets/854f9644-8bcf-494a-968c-563529b44be7" />
<img width="1280" height="800" alt="image" src="https://github.com/user-attachments/assets/1ce9e571-4860-49ba-baab-cd47cff9cc39" />
<img width="1280" height="800" alt="image" src="https://github.com/user-attachments/assets/2d193f0a-45b2-43e4-8ac7-10f873a3758d" />
