# Day 3

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
```

<img width="1920" height="1168" alt="image" src="https://github.com/user-attachments/assets/abdc83e7-5a2b-4199-90b2-916c333cb996" />
