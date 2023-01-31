# I. Ubuntu 18.04.2 LTS (Bionic Beaver)

## i. Install NVIDIA drivers.
[Reference](https://www.mvps.net/docs/install-nvidia-drivers-ubuntu-18-04-lts-bionic-beaver-linux/)
### A. Remove nvidia drivers.
```
sudo apt-get purge nvidia*
```
### B. Add graphics drivers.
```
sudo add-apt-repositroy ppa:graphics-drivers
sudo apt-get update
sudo apt-get install screen
screen
```
### C-a. Check your nvidia graphic card's driver version. for example '430'.
```
sudo apt-get install nvidia-430
sudo reboot
```
### C-b. Updated in 2019-08-22-Thu
[Reference](https://askubuntu.com/questions/951046/unable-to-install-nvidia-drivers-unable-to-locate-package)
```
sudo apt-get install nvidia-driver-430
sudo reboot
```
### D. Verify installation
```
nvidia-smi
```

## ii. Setup Korean.
[Reference 1](https://gabii.tistory.com/entry/Ubuntu-1804-LTS-%ED%95%9C%EA%B8%80-%EC%84%A4%EC%B9%98-%EB%B0%8F-%EC%84%A4%EC%A0%95)

[Reference 2](https://hiseon.me/linux/ubuntu/ubuntu-initial-setup/)
```
ibus-setup
```
## iii. Errors
### A. Could not get lock /var/lib/dpkg/lock-frontend
[Reference](https://kgu0724.tistory.com/71)
```
sudo killall apt apt-get
sudo rm /var/lib/apt/lists/lock
sudo rm /var/cache/apt/archives/lock
sudo rm /var/lib/dpkg/lock*
sudo dpkg --configure -a
sudo apt update
```

## iv. Install Nvidia Driver with Commands
```
$ sudo apt-get purge nvidia*
$ sudo add-apt-reository ppa:graphcs-drivers
$ sudo apt-get update
$ sudo apt-get install screen
$ screen
$ sudo apt-get install nvidia-390
$ sudo reboot
$ lsmod | grep nvidia
$ nvidia-smi
$ dpkg -L nvidia-driver-390
```
Reference: https://www.mvps.net/docs/install-nvidia-drivers-ubuntu-18-04-lts-bionic-beaver-linux/

# II. Ubuntu 16.04.6 LTS (Xenial Xerus)
```
None
```

# III. Ubuntu 14.04.6 LTS (Trusty Tahr)

## i. Install ROS Indigo
```
$ sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
$ sudo apt-key adv --keyserver hkp://ha.pool.sks-keyservers.net --recv-key 0xB01FA116
$ sudo apt-get update
$ sudo apt-get upgrade
$ sudo apt-get install ros-indigo-desktop-full
```
### If error occurs
```
$ sudo apt-get install libsdformat1
$ sudo rosdep init
$ rosdep update
$ echo "source /opt/ros/indigo/setup.bash" >> ~/.bashrc
$ sudo apt-get install python-rosinstall
```
### Initialize work space
```
$ mkdir -p ~/catkin_ws/src
$ cd ~/catkin_ws/src
$ catkin_init_workspace
```
### Test catkin make
```
$ cd ~/catkin_ws/
$ catkin_make
```
### Test ROS
```
$ roscore
```
Reference: https://dnddnjs.gitbooks.io/drone-autonomous-flight/content/ubuntuc5d0_ros_indigo_c124_ce58.html

## ii. Setting Gazebo simulation and SDKs
### Make test work space, package
```
$ mkdir ~/test_ws/src
$ cd ~/test_ws/src
$ catkin_create_pkg test_pkg std_msgs rospy roscpp
$ git clone https://github.com/AutonomyLab/ardrone_autonomy.git
$ git clone https://github.com/occomco/tum_simulator.git
$ cd ~/test_ws
$ rosdep install —from-paths src —ignore-src —rosdistro indigo -y
$ catkin_make
$ source devel/setup.bash
$ rospack depends test_pkg
```
### Put/Edit code in test_pkg
```
$ nano test.py
$ ctrl + x
$ y
$ chmod +x test.py
```
Reference: https://www.youtube.com/watch?v=zwTnY-ZqNcM, https://github.com/amroygaol/AR_Drone_Example_code

## iii. Execute simulation and code
### Terminal 1
```
$ roscore
```
### Terminal 2
```
$ cd ~/test_ws
$ roslaunch cvg_sim_gazebo ardrone_testworld.launch
```
### Terminal 3
```
$ cd ~/test_ws
$ rosrun test_pkg test.py
```

## Setup xrdp
### I. Install xrdp
```bash
$ sudo apt update && sudo apt install xrdp -y
```

### II. Check xrdp status and add current user into sll cert key list
```bash
$ sudo systemctl status xrdp
$ sudo adduser xrdp ssl-cert
```

*change xrdp port*
```bash
$ sudo vim /etc/xrdp/xrdp.ini # default port is 3389
```

### III. Setup xrdp always enable
```bash
$ sudo systemctl enable xrdp.service
```

### IV. Install firewalld to opne port for xrdp
```bash
$ sudo apt update && sudo apt install firewalld -y
```

### V. Setup Firewall
```bash
$ sudo firewall-cmd --permanent --zone=public --add-port={port_number}/tcp
$ sudo systemctl restart firewalld.service
$ sudo reboot
```

### VI. Connect from other devices using Remote Desktop Application
*Windows*
Remote Desktop

## Setup Static IP after Ubuntu 22 on CLI/Terminal/Shell

### 1. Edit yaml file

```Bash
$ sudo su # Edit file with root authority
$ vim /etc/netplan/{ethernet_name}.yaml
```

```yaml
...
      dhcp4: no
      addresses:
      - 192.168.123.123/24
      gateway4: 192.168.123.1
      nameservers:
        addresses:
        - 8.8.8.8
        - 168.126.63.1
        search: []
...
```

### 2. Apply edited yaml

```Bash
$ netplan apply
```

### 3. Verity

```Bash
$ ping 8.8.8.8
```

> <img width="376" alt="Screenshot 2023-01-31 at 5 41 57 PM" src="https://user-images.githubusercontent.com/20737479/215710851-88d6885a-a1ab-4c8b-9d9d-376e07f0c3de.png">

---

#### Reference
- install xrdp on Ubuntu 20, https://ko.linux-console.net/?p=393, 2022-02-24-Thu.
- setup xrdp on Ubuntu, https://corona-world.tistory.com/21, 2022-02-24-Thu.
- install firewalld on Ubuntu, https://lindarex.github.io/ubuntu/ubuntu-firewalld-installation/, 2022-02-24-Thu.
