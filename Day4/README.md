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
cd Day4/ansible/ansible-role
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


## Info - Ansible Tools Overview
<pre>
ansible - used to run ansible ad-hoc commands
ansible-playbook - used to run the ansible playbooks
ansible-doc - give help - usage details
ansible-galaxy - helps in download/install/create ansible roles
ansibe-vault - helps in security login credentials, certs, etc by encrypting
</pre>


## Lab - Ansible vault
Note
<pre>
- Ansible vault helps us in securely saving and retrieve login credentials, certs etc by encrypting them
- Using vault password we can decrypt and use them in playbooks on need basis
</pre>

Let's do this lab exercise and understand ansible vault practically. When prompts for password type root as password
```
cd ~/ansible-nov-2025
git pull
cd Day4/vault
cat mysql-login-credentials.yml
ansible-vault view mysql-login-credentials.yml
ansible-vault edit mysql-login-credentials.yml

ansible-playbook vault-playbook.yml --ask-vault-pass
```

<img width="1280" height="800" alt="image" src="https://github.com/user-attachments/assets/53a876fb-929e-4953-a7e8-b2669a0c6a75" />

You can also try the below commands
```
ansible-vault create my-credentials.yml
ansible-vault view my-credentials.yml
ansible-vault edit my-credentials.yml
cat my-credentials.yml
ansible-vault decrypt my-credentials.yml
cat my-credentials.yml
ansible-vaule encrypt my-credentials.yml
```

## Lab - Developing a custom ansible module and using it in an ansible playbook

Install tree utility
```
sudo dnf install -y tree, the admin password is rps@12345
```

```
cd ~/ansible-nov-2025
git pull
cd Day4/ansible/custom-ansible-module
tree
cat library/hello.py
cat playbook.yml
ansible-playbook playbook.yml
```

<img width="1280" height="800" alt="image" src="https://github.com/user-attachments/assets/253585d1-7d40-462a-911e-6eb5561396ed" />
<img width="1280" height="800" alt="image" src="https://github.com/user-attachments/assets/5f870881-4e91-49f5-bc58-bb1fb9a75219" />

<img width="1280" height="800" alt="image" src="https://github.com/user-attachments/assets/e54a8730-cefb-4048-9032-b7b2ad27a1f3" />

## Lab - Installing Ansible Tower

Installing Google chrome web browser
```
wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add -
sudo add-apt-repository "deb http://dl.google.com/linux/chrome/deb/ stable main"
sudo apt update
sudo apt install google-chrome-stable
google-chrome
```

In case, minikube is not installed already
```
curl -LO https://github.com/kubernetes/minikube/releases/latest/download/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube && rm minikube-linux-amd64
curl -LO https://dl.k8s.io/release/v1.34.0/bin/linux/amd64/kubectl
chmod +x kubectl
sudo mv kubectl /usr/local/bin
```

Minikube is already installed in our lab machine, hence you may skip the above steps
```
minikube status
minikube config set cpus 4
minikube config set memory 16384
minikube config set disk-size 100
minikube start

kubectl get nodes
```

<img width="1280" height="800" alt="image" src="https://github.com/user-attachments/assets/9bf3a126-4b34-432c-a574-1b5d8d3a5dd1" />
<img width="1280" height="800" alt="image" src="https://github.com/user-attachments/assets/9754dadd-8d92-4f07-9a1b-c965ab1c7084" />


```
git clone https://github.com/ansible/awx-operator.git
cd awx-operator
git checkout tags/2.19.0
make deploy
kubectl config set-context --current --namespace=awx
kubectl get pods
kubectl get pods -l "app.kubernetes.io/managed-by=awx-operator" -w
```

<img width="1280" height="800" alt="image" src="https://github.com/user-attachments/assets/fc748f0a-3e06-458b-85d7-0a605d509b4e" />
<img width="1280" height="800" alt="image" src="https://github.com/user-attachments/assets/502c3394-c6ea-4076-8894-8d44e5e6c6ae" />

Create a file named awx-demo.yml with below content
```
---
apiVersion: awx.ansible.com/v1beta1
kind: AWX
metadata:
  name: awx-demo
spec:
  service_type: nodeport
```

Run the below command
```
kubectl apply -f awx-demo.yml
kubectl get svc -l "app.kubernetes.io/managed-by=awx-operator"
kubectl get svc -n awx
#This is about the command below, you need to wait until all pods are running before proceeding to next command
kubectl get pods -n awx -w
kubectl logs -f deployments/awx-operator-controller-manager -c awx-manager -n awx
kubectl get secret awx-demo-admin-password -o jsonpath="{.data.password}" -n awx | base64 --decode ; echo
minikube ip
kubectl get svc/awx-demo-service -n awx

#Your Ansible Tower url is
http://192.168.49.2:<port-in-30000-series-on-awx-demo-service>
```

<img width="1280" height="800" alt="image" src="https://github.com/user-attachments/assets/12bedbd0-1377-4d0f-bc05-fc2706e6a92e" />
<img width="1280" height="800" alt="image" src="https://github.com/user-attachments/assets/c7bcc631-3c7b-4745-9759-29258764f666" />
<img width="1280" height="800" alt="image" src="https://github.com/user-attachments/assets/6b97c422-fefd-41c1-8dc8-87f8f1212d52" />
<img width="1280" height="800" alt="image" src="https://github.com/user-attachments/assets/fc2b8642-b676-4075-bc44-c05d0b529e02" />

#### Troubleshooting minikube Answer Tower Setup
```
minikube delete
minikube config set cpus 4
minikube config set memory 16384
minikube config set disk-size 10
docker system prune
minikube start

cd ~/awx-operator
git checkout tags/2.19.0
make deploy
kubectl config set-context --current --namespace=awx
kubectl get pods

kubectl apply -f awx-demo.yml
kubectl get svc -n awx
#This is about the command below, you need to wait until all pods are running before proceeding to next command
kubectl get pods -n awx -w
kubectl logs -f deployments/awx-operator-controller-manager -c awx-manager -n awx
kubectl get secret awx-demo-admin-password -o jsonpath="{.data.password}" -n awx | base64 --decode ; echo
minikube ip
kubectl get svc/awx-demo-service -n awx

#Your Ansible Tower url is
http://192.168.49.2:<port-in-30000-series-on-awx-demo-service>
```

## Demo - Ansible Tower CLI

To install tower-cli in Ubuntu
```
sudo apt update && sudo apt install -y python3 python3-pip
pip install ansible-tower-cli --break-system-packages --upgrade

tower-cli config username admin
tower-cli config password your-ansible-twoer-admin-password
tower-cli config verify_ssl false
tower-cli config insecure true
tower-cli config host http://192.168.49.2:30877
tower-cli login admin
tower-cli project list
tower-cli job list
tower-cli tower-cli job launch -J "Invoke Install nginx playbook"
```
<img width="1854" height="1048" alt="image" src="https://github.com/user-attachments/assets/ddf8c9b5-7f7a-40a0-91e2-31ac028816d9" />
<img width="1854" height="1048" alt="image" src="https://github.com/user-attachments/assets/95892458-8e05-46b4-b3ba-44ce6979266a" />

## Lab - Ansible Recommended Directory Structure
```
cd ~/ansible-nov-2025
git pull
cd Day5/ansible-dir-structure
tree
cat ansible.cfg
cat hosts
cat host_vars/ubuntu1
cat host_vars/ubuntu2
cat host_vars/rocky1
cat host_vars/rocky2
cat group_vars/all

ansible all -m ping
```
<img width="1854" height="1048" alt="image" src="https://github.com/user-attachments/assets/f502c39b-5d4d-4201-a0cd-12640b22b288" />
<img width="1854" height="1048" alt="image" src="https://github.com/user-attachments/assets/eab75c2a-51da-49c2-b3c4-3e6c818a4011" />
