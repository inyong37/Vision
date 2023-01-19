# Install KubeVirt on Kubernetes (1.26.0) and Ubuntu (18.04.6 LTS)

## Requirements

### Container Runtime Support

- containerd
- crio (with runv)

Use `kubectl` to fetch and show node information:

```bash
$ kubectl get nodes -o wide
```

<img width="1011" alt="Screenshot 2023-01-19 at 11 06 45 AM" src="https://user-images.githubusercontent.com/20737479/213338659-e99b4576-1b1e-4256-a6a1-f91fd76bcca9.png">

### Validate Hardware Virtualization Support

Hardware with virtualization support is recommended. You can use virt-host-validate to ensure that your hosts are capable of running virtualization workloads:

```bash
$ apt install libvirt-client
$ virt-host-validate qemu
```

<img width="1133" alt="Screenshot 2023-01-19 at 11 12 11 AM" src="https://user-images.githubusercontent.com/20737479/213339345-7cba774f-329c-44d0-b953-7a28f1d4179c.png">

### Installing KubeVirt on Kubernetes

Point at latest release:

```bash
$ export RELEASE=$(curl https://storage.googleapis.com/kubevirt-prow/release/kubevirt/kubevirt/stable.txt)
```

Deploy the KubeVirt operator:

```bash
$ kubectl apply -f https://github.com/kubevirt/kubevirt/releases/download/${RELEASE}/kubevirt-operator.yaml
```

Create the KubeVirt CR (instance deployment request) which triggers the actual installation:

```bash
$ kubectl apply -f https://github.com/kubevirt/kubevirt/releases/download/${RELEASE}/kubevirt-cr.yaml
```

Wait until all KubeVirt components are up:

```bash
$ kubectl -n kubevirt wait kv kubevirt --for condition=Available
```

<img width="576" alt="Screenshot 2023-01-19 at 11 22 20 AM" src="https://user-images.githubusercontent.com/20737479/213340468-d59e131d-99aa-419d-896b-cb61eecdc829.png">

A timeout error occurred, but when I checked the pods, it was already running.

:key: If hardware virtualization is not available, then a software emulation fallback can be enabled using by setting in the KubeVirt CR spec.configuration.developerConfiguration.useEmulation to true as follows:

```bash
$ kubectl edit -n kubevirt kubevirt kubevirt
```

Add the following to the kubevirt.yaml file:

```vim
    spec:
      ...
      configuration:
        developerConfiguration:
          useEmulation: true
```

All new components will be deployed under the kubevirt namespace:

```bash
$ kubectl get pods -n kubevirt
```

<img width="486" alt="Screenshot 2023-01-19 at 11 21 52 AM" src="https://user-images.githubusercontent.com/20737479/213340429-e8b458ca-599e-47ae-b296-0f27f30e1e5f.png">

---

### Reference
- Installation, https://kubevirt.io/user-guide/operations/installation/, 2023-01-19-Thu.
- Find Out What Container Runtime is Used on a Node, https://kubernetes.io/docs/tasks/administer-cluster/migrating-from-dockershim/find-out-runtime-you-use/, 2023-01-19-Thu.
