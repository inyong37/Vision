# [Ansible](https://www.ansible.com/) | Red Hat Ansible Automation Platform

Red Hat Ansible Automation Platform is an end-to-end automation platform to configure systems, deploy software, and orchestrate advanced workflows. It includes resources to create, manage, and scale across the entire enterprise.

Available on Microsoft Azure, AWS, Google Cloud

Ansible is an open source, command-line IT automation software application written in Python. It can configure systems, deploy software, and orchestrate advanced workflows to support application deployment, system updates, and more.

Ansible’s main strengths are simplicity and ease of use. It also has a strong focus on security and reliability, featuring minimal moving parts. It uses OpenSSH for transport (with other transports and pull modes as alternatives), and uses a human-readable language that is designed for getting started quickly without a lot of training.

---

![image](https://github.com/inyong37/Vision/assets/20737479/53bcfdd0-ebd9-44ba-a224-e318df0ac153)

### Community Ansible

The community distribution of Ansible contains a suite of powerful command line tools supported on most operating systems with Python installed. This includes Red Hat Enterprise Linux, Debian, Ubuntu, MacOS, FreeBSD, Microsoft Windows, and more. For more information on installing Ansible refer to the installation documentation.

### Red Hat Ansible Automation Platform

Red Hat Ansible Automation Platform is a subscription product built on the foundations of Ansible with numerous enterprise features. It combines more than a dozen upstream projects into an integrated, streamlined product. Each product component also has a specific purpose with a well-defined scope. For example, the automation controller is the WebUI and API for Ansible automation, which is based on the upstream project AWX. This component is bundled into the platform to manage automation. Ansible Automation Platform is available to be run on-premise and charged by node (rather than by user), or you can use the managed service offering on Microsoft Azure.

---

## Date

2023-09-18-Monday.

## Environment

* Ansible Server: Ubuntu 20.04.4 LTS

## Setup

### Install

```Bash
sudo add-apt-repository ppa:ansible/ansible
sudo apt install ansible -y
```

Verify: `ansible --version`

```Bash
(base) inyong@desktop:~$ ansible --version
ansible [core 2.12.10]
  config file = /etc/ansible/ansible.cfg
  configured module search path = ['/home/inyong/.ansible/plugins/modules', '/usr/share/ansible/plugins/modules']
  ansible python module location = /usr/lib/python3/dist-packages/ansible
  ansible collection location = /home/inyong/.ansible/collections:/usr/share/ansible/collections
  executable location = /usr/bin/ansible
  python version = 3.8.10 (default, May 26 2023, 14:05:08) [GCC 9.4.0]
  jinja version = 2.10.1
  libyaml = True
```

```Bash
sudo apt install python3-argcomplete -y
sudo activate-global-python-argcomplete3
```

### Inventory

Edit: `sudo vim /etc/ansible/hosts`

```
...
[servers]
{server_name_01} ansible_host={ip_address} # 192.168.0.10
{server_name_01} ansible_host={ip_address} # 192.168.0.11
{server_name_01} ansible_host={ip_address} # 192.168.0.12
{server_name_01} ansible_host={ip_address} # 192.168.0.13
...
[all:vars]
ansible_python_interpreter=/usr/bin/python3
```

### SSH

```Bash
ssh-keygen -t rsa -b 4096 -C "AnsibleKey"
ssh-copy-id -i {user_name}@{ip_address} # root@192.168.0.10
```

Verify: `ansible all -m ping -u root` = `ansible all -m ansible.builtin.ping -u root`

```Bash
{server_name_01} | SUCCESS => {
    "changed": false,
    "ping": "pong"
}
```

### Command

```Bash
ansible {agents} -a "{command}" -u root
```

Example: `ansible all -a "ls" -u root`

```Bash
{server_name_01} | CHANGED | rc=0 >>
snap
```

### [Playbook](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_intro.html)

```Bash
- name: name
  hosts: all
  become: true
  tasks:
    - name: task1
...
```

Execute: `ansible-playbook {playbook}.yaml`

---

### Reference
- Ansible, https://www.ansible.com/, 2023-06-08-Thu.
- How Ansible Works, https://www.ansible.com/overview/how-ansible-works, 2023-06-08-Thu.
- Ansible in 100 Seconds, https://youtu.be/xRMPKQweySE, 2023-06-08-Thu.
- Ansible Docs, https://docs.ansible.com/, 2023-06-08-Thu.
- Ansible Tutorial Blog KR, https://ko.linux-console.net/?p=3487#gsc.tab=0, 2023-09-18-Mon.
- Ansible Tutorial Blog KR, https://kibbomi.tistory.com/258, 2023-09-18-Mon.
- Ansible Playbook, https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_intro.html, 2023-09-19-Tue.
- Ansible Playbook Blog KR, https://mcpaint.tistory.com/278, 2023-09-19-Tue.
- Ansible Playbook Blog KR, https://chanchan-father.tistory.com/517, 2023-09-19-Tue.
