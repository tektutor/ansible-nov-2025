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

## Lab - While loop

Create a file named reverse-number.py with below code
<pre>
#!/usr/bin/python3

x = int( input ("Enter a number: " ) )
reverse = 0

while x > 0:
    digit = x % 10 
    reverse = reverse * 10 + digit
    x = x // 10

print("Reversed number is :", reverse )  
</pre>

Run it
```
python3 ./reverse-number.py
```
<img width="1280" height="768" alt="image" src="https://github.com/user-attachments/assets/bdca62b2-b353-4562-bf2b-0da2d30cac51" />


## Info - Python Operators and expressions

Comparision Operators in Python
<pre>
==  equal
!=  not equal
>   greter than
<   less than
>=  greter than or equal to
<=  less than or equal to
</pre>

Assignment Operators
<pre>
=  assign
+= add and assign
-= subtract and assign
*= multiply and assign
/= divide and assign
%= mod and assign
</pre>

Logical Operators
<pre>
and  True and True   results in True
or   True or False   results in True
not  Negate    e.g. not False is Tue
</pre>

## Lab - Getting used to python string
Write a python script named string.py with below code
```
#!/usr/bin/python3

firstString = "Some"
secondString = "String"
print(firstString)
print(secondString)
result = firstString + secondString
print("Cancatenated string is ", result )
print("---------------------------------------")
s = "Advanced Python"
print(s)
length = len(s)
print("Length of string ", s, " is ", length )

#First letter in the string s
print( s[0] ) # Print 'A'

#Last letter in the string s
print( s[length-1] )
print( s[-1] )

#convert to Upper case
print(s.upper())
print(s.lower())
```

Run it
```
python3 string.py
```

Expected output
<img width="1280" height="768" alt="image" src="https://github.com/user-attachments/assets/017382ac-ca96-4ba5-85e4-818d99046b84" />

## Lab - Python Function

## Lab - Python class ( user-defined data-type )

## Info - Write a RPN Calculator in Python
Note
<pre>
- the RPN Calculator will accept math expression in Reverse Polish Notation
- the input will be only a string
- Reverse Polish Notation is also called as Post fix 
- 10 + 15 ( Infix Notation )
- + 10 15 ( Prefix Notation )
- 10 15 + ( Postfix Notation )
- Infix math expression
  ( 10 * 3 ) - (100 / 20 )
                 -
          *               /
     10       3        100    20 
- Binary Tree Traversal Algorithms
  - Inorder Traversal
  - Preorder Traversal
  - Postorder Traversal algorithms
</pre>

## Info - Postorder Traversal ( Recursive Variant )
<pre>
- Process Left Child
- Process Right Child
- Process Parent
- "10 3 * 100 20 / -"
</pre>

## Lab - Cloning TekTutor's Training Repository
```
cd ~
git clone https://github.com/tektutor/ansible-nov-2025
cd ansible-nov-2025
ls
```

## Lab - Python based RPN Calculator
```
cd ~/ansible-nov-2025
git pull
cd Day1/python
cat stack.py
cat rpncalculator.py
python3 rpncalculator.py
```
