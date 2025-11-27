# Day 4

## Info - Ansible Role
<pre>
- Ansible role follows specific directory structure and certain conventions
- it make our code reusable across ansible playbooks
- ansible roles can't be executed directly 
- ansible roles can be invoked from ansible playbooks
</pre>

## Lab - Creating a custom ansible role and using it in our Ansible playbook ( complete this lab exercise and notify me )
```
cd ~/ansible-nov-2025
git pull
cd Day4/ansible/ansible-role
ansible-playbook -i inventory install-nginx-playbook.yml
```

<img width="1280" height="800" alt="image" src="https://github.com/user-attachments/assets/500c34a8-b427-4798-a814-53d741310856" />
<img width="1280" height="800" alt="image" src="https://github.com/user-attachments/assets/b6906ac7-9447-4981-a25f-fb43f44b3f04" />
<img width="1280" height="800" alt="image" src="https://github.com/user-attachments/assets/28f0caca-4dc6-4825-8f4d-a1afba42a3b8" />
<img width="1280" height="800" alt="image" src="https://github.com/user-attachments/assets/efa3f67f-aa21-4281-b168-7c076a4646ee" />
<img width="1280" height="800" alt="image" src="https://github.com/user-attachments/assets/e883ed3a-f84d-457b-8b66-6fe616aa11b3" />


## Info - Ansible Configuration File
<pre>
- This config file has ansible settings
- We could override the default ansible setting in this file
- This file can be kep in current directory or home directory or /etc/ansible folder or you can keep the file at location and point to that file with the environment variable ANSIBLE_CONFIG
- ansible searches for this file in the below order and wherever it finds it picks and ignores the rest
  - checks if ANSIBLE_CONFIG is configured if yes it picks the ansible.cfg at that path
  - next it checks in current directory, if it finds the ansible.cfg it picks from current directory otherwise
  - next it check in the user home directory for a file named .ansible.cfg, if it finds it uses that file otherwise
  - next it looks for ansible.cfg at /etc/ansible folder
</pre>
