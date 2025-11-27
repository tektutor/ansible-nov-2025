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

## Info - Dynamic Inventory
<pre>
- dynamic inventory is typically a custom python script that retrieves 
  the ansible node connection details at run time
- ansible expects the dynamic inventory in the form of JSON string, as long 
  as our python script provides the ansible node details in that forward 
  it will work as expected
- the benefit of using dynamic inventory over static inventory is that, 
  when ansible nodes are taken down for system maintainence we don't need 
  to update the inventory each time like we do in static inventory
- also when new nodes are added, we don't need to add them manually in the 
  inventory as dynamic inventory script will find which all nodes are accessible 
  at the time we run the dynamic_inventory.py script
</pre>

## Lab - Using dynamic inventory
```
cd ~/ansible-nov-2025
git pull
cd Day4/ansible/ansible-node
cat ansible.cfg
./dynamic_inventory.py
ansible all -m ping
ansible-playbook install-nginx-playbook.yml
```

<img width="1280" height="800" alt="image" src="https://github.com/user-attachments/assets/ca135309-9860-47ee-b9cc-d94d54ffc367" />
<img width="1280" height="800" alt="image" src="https://github.com/user-attachments/assets/608af2ab-d273-4236-af8b-f3fb486b6a13" />
<img width="1280" height="800" alt="image" src="https://github.com/user-attachments/assets/0fd2231c-1ed3-41f6-976f-a1b8c665ae94" />
<img width="1280" height="800" alt="image" src="https://github.com/user-attachments/assets/963e1b8c-e0d6-467a-b33a-96542bcd98fb" />
<img width="1280" height="800" alt="image" src="https://github.com/user-attachments/assets/1336e4bb-f0ce-49a2-aab1-763d74396c4b" />
<img width="1280" height="800" alt="image" src="https://github.com/user-attachments/assets/f4300e0b-0030-4824-ace8-aac83dd342ca" />

## Lab - Ansible Loops
In this example the curl ports we are computing with the with_sequence loop.
```
cd ~/ansible-nov-2025
git pull
cd Day4/ansible/ansible-role
ansible-playbook install-nginx-playbook.yml
````

<img width="1280" height="800" alt="image" src="https://github.com/user-attachments/assets/589f5e4d-77d1-48f2-af75-6ca3d53fda47" />
<img width="1280" height="800" alt="image" src="https://github.com/user-attachments/assets/c154183d-0d8e-4e11-af2c-cacf2add6bb5" />
<img width="1280" height="800" alt="image" src="https://github.com/user-attachments/assets/bba37e51-08fd-4183-9b56-bf5d4421de3d" />
<img width="1280" height="800" alt="image" src="https://github.com/user-attachments/assets/9b437026-b0fc-41bc-8ddd-623a180e6f94" />
<img width="1280" height="800" alt="image" src="https://github.com/user-attachments/assets/899ed6a8-43e1-4002-9080-9b9277ea9d0a" />







