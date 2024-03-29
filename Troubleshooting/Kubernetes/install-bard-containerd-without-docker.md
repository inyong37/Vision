# Using containerd for CRI in Kubernetes

## Date

2023-02-02-Thursday

## Environment

Ubuntu 20.04 LTS

## Problem

I am trying to organize new Kubernetes cluster with 3 Ubuntu 22.04 LTS PCs. After setting network, I installed continerd with `apt install containerd.io` as below steps.

:key: [Setup containerd for CRI](https://kubernetes.io/docs/setup/production-environment/container-runtimes/#containerd)

:key: [Install containerd](https://github.com/containerd/containerd/blob/main/docs/getting-started.md): The containerd.io package contains runc too, but does not contain CNI plugins.

:key: [Install containerd on Ubuntu via installing Docker](https://docs.docker.com/engine/install/ubuntu/)

However, I got an error when I commanded `kubeadm init -- ...`

> <img width="2236" alt="Screenshot 2023-02-02 at 11 04 22 AM" src="https://user-images.githubusercontent.com/20737479/216213128-c0d711f3-864f-4f07-83c8-b7f15561e8f4.png">

## [Try #1 - Not Solved](https://www.nocentino.com/posts/2021-12-27-installing-and-configuring-containerd-as-a-kubernetes-container-runtime/)

:key: All commands are executed with root authority.

Installing containerd with `apt install` is not enough. Therefore, few more steps are required as below.

1. Make directory for containerd configuration:

```Bash
mkdir -p /etc/containerd
```

2. Make config file for containerd:

```Bash
containerd config default | sudo tee /etc/containerd/config.toml
```

3. Change `SystemdCgroup` fales to ture:

```Bash
sed -i 's/ SystemdCgroup = false/ SystemdCgroup = true/' /etc/containerd/config.toml
```

Finally, restart containerd:

```Bash
systemctl restart containerd
```

## [Solution](https://forum.linuxfoundation.org/discussion/862825/kubeadm-init-error-cri-v1-runtime-api-is-not-implemented)

However, the same error code appeard :cry: The real problem was old containerd version of built-in Ubuntu 20. Therefore, I removed containerd and installed it again.

Removed:

```Bash
apt remove containerd
```

Install:

```Bash
apt install containerd.io
```

Remove old config file:

```Bash
rm /etc/containerd/config.toml
```

Restart containerd:
```Bash
systemctl restart containerd
```

Finally, kubeadm init works :tada:

> <img width="608" alt="Screenshot 2023-02-02 at 11 41 03 AM" src="https://user-images.githubusercontent.com/20737479/216217954-b9d67f9d-a783-4e03-9425-792613f63a3c.png">

---

### Reference
- Installing and Configuring containerd as a Kubernetes Container Runtime, https://www.nocentino.com/posts/2021-12-27-installing-and-configuring-containerd-as-a-kubernetes-container-runtime/, 2023-02-02-Thu.
- kubeadm init error: CRI v1 runtime API is not implemented, https://forum.linuxfoundation.org/discussion/862825/kubeadm-init-error-cri-v1-runtime-api-is-not-implemented, 2023-02-02-Thu.
