# Day 1


## Python Overview
<pre>
- is a high level scripting programming language
- dynamically typed language
- data type
  - int
  - float
  - string
  - bool
  - sequential types
    - list
    - tuple
    - range
  - maps
    - dict
    - set
  - binary types
    - bytes
    - bytearray
- it is used for developing
  - console/command-line applications
  - AI/ML 
  - Web applications
  - Games
  - Academic
  - pattern matching
  - embedded projects
- python is supported in following OS
  - Unix
  - Linux
  - Mac
  - Windows
</pre>

## Lab - Checking your python environment
```
python3 --version
```

Expected output
<pre>
python3 --version                  
Python 3.13.3  
</pre>

## Lab - Installing Visual studio code editor in your lab machine
When it prompts for password, type rps@12345
```
sudo snap install code --classic
```

## Lab - Writing a hello world python program

In your home directory on the linux box
```
cd /home/student
mkdir -p python
cd python
```

Create a file named hello.py with the below code using 
```
#!/usr/bin/python3

print("Hello Python !")
```

Run it
```
python3 hello.py
```
<img width="1280" height="768" alt="image" src="https://github.com/user-attachments/assets/98750362-f6e6-4a4a-ba11-c4664fe11608" />
<img width="1280" height="768" alt="image" src="https://github.com/user-attachments/assets/6c328ee4-bd0b-4fba-882a-b08fbc2f7316" />

Other way to run your python script is
```
chmod +x ./hello.py
ls
./hello.py
```

## Lab - Find sum of int range accepting user inputs

Write a simple python program as shown below
<img width="1280" height="768" alt="image" src="https://github.com/user-attachments/assets/52ab8d6b-be8c-48d9-b89f-8b399af0b7e1" />

Run it
```
python3 sumofintegers.py
```
<img width="1280" height="768" alt="image" src="https://github.com/user-attachments/assets/afa3b022-95f3-4d1a-b0f2-4d10c716a00c" />
