```
1.   $ sudo apt-get update
2.   $ sudo apt-get upgrade -y
3.   $ mkdir line_robot
4.   $ cd ~/line_robot
5.   $ sudo apt install python3-gpiozero
6.   $ python3 -m venv venv --system-site-packages
7.   $ source venv/bin/activate
```
8. create path of project

   line_robot/\n
   ├── main.py                  
   ├── templates/\n
   │   └── index.html           
   ├── venv/                    
   └── requirements.txt         
```
9.   $ pip install -r requirements.txt
10.  $ nano run.sh
```

paste program to run.sh file

```
#!/bin/bash
cd /home/pi/line_robot
source venv/bin/activate
sudo venv/bin/python main.py # Chang File name!!!
```

```
11. $ chmod +x run.sh
12. $ ./run.sh
```