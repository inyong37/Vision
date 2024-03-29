# Install KubeVirt on Kubernetes (1.26.0) and Ubuntu (18.04.6 LTS)

## Date

2023-01-19-Thursday.

2023-02-02-Thursday.

2023-02-03-Friday.

## Environment

Ubuntu 18.04.6 LTS -> Ubuntu 20.04.5 LTS -> Ubuntu 22.04.1 LTS

Kubernetes 1.26.0 -> Kubernetes 1.24.0

## 0. Requirements

### Container Runtime Support

- containerd
- crio (with runv)

### Validate Hardware Virtualization Support

Hardware with virtualization support is recommended. You can use virt-host-validate to ensure that your hosts are capable of running virtualization workloads:

```Bash
apt install -y libvirt-clients
```

Check:

```Bash
virt-host-validate qemu
```

<img width="1133" alt="Screenshot 2023-01-19 at 11 12 11 AM" src="https://user-images.githubusercontent.com/20737479/213339345-7cba774f-329c-44d0-b953-7a28f1d4179c.png">

<img width="1209" alt="Screenshot 2023-02-03 at 2 48 14 PM" src="https://user-images.githubusercontent.com/20737479/216522655-dae18dea-5384-48f3-8dbb-d3b2b9b5727b.png">

## 1. Installing KubeVirt on Kubernetes

Point at latest release:

```Bash
export RELEASE=$(curl https://storage.googleapis.com/kubevirt-prow/release/kubevirt/kubevirt/stable.txt)
```

Deploy the KubeVirt operator:

```Bash
kubectl apply -f https://github.com/kubevirt/kubevirt/releases/download/${RELEASE}/kubevirt-operator.yaml
```

Create the KubeVirt CR (instance deployment request) which triggers the actual installation:

```bash
kubectl apply -f https://github.com/kubevirt/kubevirt/releases/download/${RELEASE}/kubevirt-cr.yaml
```

Wait until all KubeVirt components are up:

```Bash
kubectl -n kubevirt wait kv kubevirt --for condition=Available
```

<img width="576" alt="Screenshot 2023-01-19 at 11 22 20 AM" src="https://user-images.githubusercontent.com/20737479/213340468-d59e131d-99aa-419d-896b-cb61eecdc829.png">

A timeout error occurred, but when I checked the pods, it was already running.

:key: If hardware virtualization is not available, then a software emulation fallback can be enabled using by setting in the KubeVirt CR spec.configuration.developerConfiguration.useEmulation to true as follows:

```Bash
kubectl edit -n kubevirt kubevirt kubevirt
```

Add the following to the kubevirt.yaml file:

```YAML
    spec:
      ...
      configuration:
        developerConfiguration:
          useEmulation: true
```

All new components will be deployed under the kubevirt namespace `kubectl get pods -n kubevirt`:

```Bash
NAMESPACE     NAME                                               READY   STATUS      RESTARTS   AGE     IP              NODE     NOMINATED NODE   READINESS GATES
kubevirt      virt-api-59d8cb4bbb-d5qr8                          1/1     Running     0          8m16s   10.40.0.6       node86   <none>           <none>
kubevirt      virt-api-59d8cb4bbb-x5r8w                          1/1     Running     0          8m16s   10.36.0.9       node88   <none>           <none>
kubevirt      virt-controller-6fff8874b6-j88wc                   1/1     Running     0          7m40s   10.40.0.9       node86   <none>           <none>
kubevirt      virt-controller-6fff8874b6-z9dd2                   1/1     Running     0          7m40s   10.36.0.10      node88   <none>           <none>
kubevirt      virt-handler-ghd4q                                 1/1     Running     0          7m40s   10.40.0.10      node86   <none>           <none>
kubevirt      virt-handler-p555f                                 1/1     Running     0          7m40s   10.36.0.11      node88   <none>           <none>
kubevirt      virt-handler-w44cp                                 1/1     Running     0          7m40s   10.32.0.7       node85   <none>           <none>
kubevirt      virt-operator-67c4d5db65-5fbzw                     1/1     Running     0          9m1s    10.36.0.6       node88   <none>           <none>
kubevirt      virt-operator-67c4d5db65-d7t6t                     1/1     Running     0          9m1s    10.40.0.5       node86   <none>           <none>
```

## 2. [Install Containerized Data Importer (CDI)](https://kubevirt.io/user-guide/operations/containerized_data_importer/)

### What is a Containerized Data Importer (CDI)?

The Containerized Data Importer (CDI) project provides facilities for enabling Persistent Volume Claims (PVCs) to be used as disks for KubeVirt VMs by way of DataVolumes. The three main CDI use cases are:
- Import a disk image from a web server or container registry to a DataVolume
- Clone an existing PVC to a DataVolume
- Upload a local disk image to a DataVolume

### Install CDI

```Bash
export TAG=$(curl -s -w %{redirect_url} https://github.com/kubevirt/containerized-data-importer/releases/latest)
```

```Bash
export VERSION=$(echo ${TAG##*/})
```

```Bash
kubectl create -f https://github.com/kubevirt/containerized-data-importer/releases/download/$VERSION/cdi-operator.yaml
```

```Bash
kubectl create -f https://github.com/kubevirt/containerized-data-importer/releases/download/$VERSION/cdi-cr.yaml
```

### Expose `cdi-uploadproxy` service

The `cdi-uploadproxy` service must be accessible from outside the cluster. Here are some ways to do that:
- NodePort Service
- [Ingress](https://kubernetes.io/docs/concepts/services-networking/ingress/)
  - An API object that manages external access to the services in a cluster, typically HTTP.
  - Ingress may provide load balancing, SSL termination and name-based virtual hosting. 
- Route
- kubectl port-forward (not recommended for production clusters)

## 3. [Install virtctl](https://kubevirt.io/user-guide/operations/virtctl_client_tool/)

Basic VirtualMachineInstance operations can be performed with the stock kubectl utility. However, the virtctl binary utility is required to use advanced features such as:
- Serial and graphical console access

It also provides convenience commands for:
- Starting and stopping VirtualMachineInstances
- Live migrating VirtualMachineInstances and canceling live migrations
- Uploading virtual machine disk images

There are two ways to get it:
- the most recent version of the tool can be retrieved from the official release page
- it can be installed as a kubectl plugin using krew

### A. Install virtctl

```Bash
export VERSION=v0.58.0
```

```Bash
wget https://github.com/kubevirt/kubevirt/releases/download/${VERSION}/virtctl-${VERSION}-linux-amd64
```

```Bash
mv virtctl-${VERSION}-linux-amd64 virtctl
```

```Bash
chmod +x virtctl
```

```Bash
install virtctl /bin/
```

### B-1. [Install `krew`](https://krew.sigs.k8s.io/docs/user-guide/setup/install/)

1. Install `git`:

```Bash
apt install git
```

2. Run this command to download and install `krew`:

```Bash
(
  set -x; cd "$(mktemp -d)" &&
  OS="$(uname | tr '[:upper:]' '[:lower:]')" &&
  ARCH="$(uname -m | sed -e 's/x86_64/amd64/' -e 's/\(arm\)\(64\)\?.*/\1\2/' -e 's/aarch64$/arm64/')" &&
  KREW="krew-${OS}_${ARCH}" &&
  curl -fsSLO "https://github.com/kubernetes-sigs/krew/releases/latest/download/${KREW}.tar.gz" &&
  tar zxvf "${KREW}.tar.gz" &&
  ./"${KREW}" install krew
)
```

3. Add the $HOME/.krew/bin directory to your PATH environment variable. To do this, update your .bashrc or .zshrc file and append the following line:

```Bash
vi ~/.bashrc
...
export PATH="${PATH}:${HOME}/.krew/bin"
...
```

and restart your shell or source ~/.bashrc:

```Bash
source ~/.bashrc
```

### B-2. [Install `virtctl` with `krew`](https://kubevirt.io/user-guide/operations/virtctl_client_tool/)

```Bash
kubectl krew install virt
```

---

### Reference
- Installation, https://kubevirt.io/user-guide/operations/installation/, 2023-01-19-Thu.
- Find Out What Container Runtime is Used on a Node, https://kubernetes.io/docs/tasks/administer-cluster/migrating-from-dockershim/find-out-runtime-you-use/, 2023-01-19-Thu.
- KubeVirt: installing Microsoft Windows from an ISO, https://kubevirt.io/2020/KubeVirt-installing_Microsoft_Windows_from_an_iso.html, 2023-01-19-Thu.
- Containerized Data Importer, https://kubevirt.io/user-guide/operations/containerized_data_importer/, 2023-01-19-Thu.
- Ingress, https://kubernetes.io/docs/concepts/services-networking/ingress/, 2023-01-19-Thu.
- virtctl Client Tool, https://kubevirt.io/user-guide/operations/virtctl_client_tool/, 2023-01-19-Thu.
- Installation krew, https://krew.sigs.k8s.io/docs/user-guide/setup/install/, 2023-01-19-Thu.
- Install virtctl with krew, https://kubevirt.io/user-guide/operations/virtctl_client_tool/, 2023-01-19-Thu.
