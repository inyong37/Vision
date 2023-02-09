# kubelet initial timeout when kubeadm init

## Date

2023-02-03-Friday.

## Environment

Ubuntu 22.04.1 LTS

Kubernetes 1.24.10

## Problem

One node works, but another one doesn't work as below:

> <img width="769" alt="Screenshot 2023-02-03 at 4 21 51 PM" src="https://user-images.githubusercontent.com/20737479/216537312-7ce493ec-21a4-433c-861b-fd79652e4a3f.png">

> <img width="773" alt="Screenshot 2023-02-03 at 4 22 09 PM" src="https://user-images.githubusercontent.com/20737479/216537365-27781c15-3b07-440d-b5a0-5964c7e0abb3.png">

## Solution

I guess container runtime is not installed rightly. Therefore, I reinstalled container runtime interface.
