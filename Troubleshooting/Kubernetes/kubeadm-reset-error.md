# kubeadm reset error

## Date

2023-03-15-Wednesday.

## Environment

Ubuntu 22.04.2 LTS

Kubernetes 1.24.10

## Probelm

[While deleting a node of cluster and reseting it](https://sinsomi.tistory.com/entry/k8s-node-%EC%B6%94%EA%B0%80-master-node-worker-node-join), the errors occured:

```Bash
root@node237:~# kubeadm reset --cri-socket=/var/run/crio/crio.sock
W0315 07:32:07.756949 2862136 preflight.go:55] [reset] WARNING: Changes made to this host by 'kubeadm init' or 'kubeadm join' will be reverted.
[reset] Are you sure you want to proceed? [y/N]: y
[preflight] Running pre-flight checks
W0315 07:32:09.066304 2862136 removeetcdmember.go:84] [reset] No kubeadm config, using etcd pod spec to get data directory
[reset] No etcd config found. Assuming external etcd
[reset] Please, manually reset etcd to prevent further issues
[reset] Stopping the kubelet service
[reset] Unmounting mounted directories in "/var/lib/kubelet"
W0315 07:32:20.688648 2862136 cleanupnode.go:93] [reset] Failed to remove containers: [failed to remove running container I0315: output: I0315 07:32:09.782712 2862163 util_unix.go:103] "Using this endpoint is deprecated, please consider using full URL format" endpoint="/var/run/crio/crio.sock" URL="unix:///var/run/crio/crio.sock"
getting sandbox status of pod "I0315": rpc error: code = NotFound desc = could not find pod "I0315": PodSandbox with ID starting with I0315 not found: ID does not exist
, error: exit status 1, failed to remove running container 07:32:09.658138: output: I0315 07:32:09.860007 2862179 util_unix.go:103] "Using this endpoint is deprecated, please consider using full URL format" endpoint="/var/run/crio/crio.sock" URL="unix:///var/run/crio/crio.sock"
getting sandbox status of pod "07:32:09.658138": rpc error: code = NotFound desc = could not find pod "07:32:09.658138": PodSandbox with ID starting with 07:32:09.658138 not found: ID does not exist
, error: exit status 1, failed to remove running container 2862145: output: I0315 07:32:09.930483 2862195 util_unix.go:103] "Using this endpoint is deprecated, please consider using full URL format" endpoint="/var/run/crio/crio.sock" URL="unix:///var/run/crio/crio.sock"
getting sandbox status of pod "2862145": rpc error: code = NotFound desc = could not find pod "2862145": PodSandbox with ID starting with 2862145 not found: ID does not exist
, error: exit status 1, failed to remove running container util_unix.go:103]: output: I0315 07:32:09.999700 2862211 util_unix.go:103] "Using this endpoint is deprecated, please consider using full URL format" endpoint="/var/run/crio/crio.sock" URL="unix:///var/run/crio/crio.sock"
getting sandbox status of pod "util_unix.go:103]": rpc error: code = NotFound desc = could not find pod "util_unix.go:103]": PodSandbox with ID starting with util_unix.go:103] not found: ID does not exist
, error: exit status 1, failed to remove running container "Using: output: I0315 07:32:10.066731 2862227 util_unix.go:103] "Using this endpoint is deprecated, please consider using full URL format" endpoint="/var/run/crio/crio.sock" URL="unix:///var/run/crio/crio.sock"
getting sandbox status of pod "\"Using": rpc error: code = NotFound desc = could not find pod "\"Using": PodSandbox with ID starting with "Using not found: ID does not exist
, error: exit status 1, failed to remove running container this: output: I0315 07:32:10.137341 2862243 util_unix.go:103] "Using this endpoint is deprecated, please consider using full URL format" endpoint="/var/run/crio/crio.sock" URL="unix:///var/run/crio/crio.sock"
getting sandbox status of pod "this": rpc error: code = NotFound desc = could not find pod "this": PodSandbox with ID starting with this not found: ID does not exist
, error: exit status 1, failed to remove running container endpoint: output: I0315 07:32:10.210431 2862259 util_unix.go:103] "Using this endpoint is deprecated, please consider using full URL format" endpoint="/var/run/crio/crio.sock" URL="unix:///var/run/crio/crio.sock"
getting sandbox status of pod "endpoint": rpc error: code = NotFound desc = could not find pod "endpoint": PodSandbox with ID starting with endpoint not found: ID does not exist
, error: exit status 1, failed to remove running container is: output: I0315 07:32:10.279464 2862275 util_unix.go:103] "Using this endpoint is deprecated, please consider using full URL format" endpoint="/var/run/crio/crio.sock" URL="unix:///var/run/crio/crio.sock"
getting sandbox status of pod "is": rpc error: code = NotFound desc = could not find pod "is": PodSandbox with ID starting with is not found: ID does not exist
, error: exit status 1, failed to remove running container deprecated,: output: I0315 07:32:10.353441 2862291 util_unix.go:103] "Using this endpoint is deprecated, please consider using full URL format" endpoint="/var/run/crio/crio.sock" URL="unix:///var/run/crio/crio.sock"
getting sandbox status of pod "deprecated,": rpc error: code = NotFound desc = could not find pod "deprecated,": PodSandbox with ID starting with deprecated, not found: ID does not exist
, error: exit status 1, failed to remove running container please: output: I0315 07:32:10.426813 2862307 util_unix.go:103] "Using this endpoint is deprecated, please consider using full URL format" endpoint="/var/run/crio/crio.sock" URL="unix:///var/run/crio/crio.sock"
getting sandbox status of pod "please": rpc error: code = NotFound desc = could not find pod "please": PodSandbox with ID starting with please not found: ID does not exist
, error: exit status 1, failed to remove running container consider: output: I0315 07:32:10.492812 2862322 util_unix.go:103] "Using this endpoint is deprecated, please consider using full URL format" endpoint="/var/run/crio/crio.sock" URL="unix:///var/run/crio/crio.sock"
getting sandbox status of pod "consider": rpc error: code = NotFound desc = could not find pod "consider": PodSandbox with ID starting with consider not found: ID does not exist
, error: exit status 1, failed to remove running container using: output: I0315 07:32:10.559803 2862338 util_unix.go:103] "Using this endpoint is deprecated, please consider using full URL format" endpoint="/var/run/crio/crio.sock" URL="unix:///var/run/crio/crio.sock"
getting sandbox status of pod "using": rpc error: code = NotFound desc = could not find pod "using": PodSandbox with ID starting with using not found: ID does not exist
, error: exit status 1, failed to remove running container full: output: I0315 07:32:10.632868 2862354 util_unix.go:103] "Using this endpoint is deprecated, please consider using full URL format" endpoint="/var/run/crio/crio.sock" URL="unix:///var/run/crio/crio.sock"
getting sandbox status of pod "full": rpc error: code = NotFound desc = could not find pod "full": PodSandbox with ID starting with full not found: ID does not exist
, error: exit status 1, failed to remove running container URL: output: I0315 07:32:10.711031 2862369 util_unix.go:103] "Using this endpoint is deprecated, please consider using full URL format" endpoint="/var/run/crio/crio.sock" URL="unix:///var/run/crio/crio.sock"
getting sandbox status of pod "URL": rpc error: code = NotFound desc = could not find pod "URL": PodSandbox with ID starting with URL not found: ID does not exist
, error: exit status 1, failed to remove running container format": output: I0315 07:32:10.779696 2862385 util_unix.go:103] "Using this endpoint is deprecated, please consider using full URL format" endpoint="/var/run/crio/crio.sock" URL="unix:///var/run/crio/crio.sock"
getting sandbox status of pod "format\"": rpc error: code = NotFound desc = could not find pod "format\"": PodSandbox with ID starting with format" not found: ID does not exist
, error: exit status 1, failed to remove running container endpoint="/var/run/crio/crio.sock": output: I0315 07:32:10.856382 2862400 util_unix.go:103] "Using this endpoint is deprecated, please consider using full URL format" endpoint="/var/run/crio/crio.sock" URL="unix:///var/run/crio/crio.sock"
getting sandbox status of pod "endpoint=\"/var/run/crio/crio.sock\"": rpc error: code = NotFound desc = could not find pod "endpoint=\"/var/run/crio/crio.sock\"": PodSandbox with ID starting with endpoint="/var/run/crio/crio.sock" not found: ID does not exist
, error: exit status 1, failed to remove running container URL="unix:///var/run/crio/crio.sock": output: I0315 07:32:10.922771 2862416 util_unix.go:103] "Using this endpoint is deprecated, please consider using full URL format" endpoint="/var/run/crio/crio.sock" URL="unix:///var/run/crio/crio.sock"
getting sandbox status of pod "URL=\"unix:///var/run/crio/crio.sock\"": rpc error: code = NotFound desc = could not find pod "URL=\"unix:///var/run/crio/crio.sock\"": PodSandbox with ID starting with URL="unix:///var/run/crio/crio.sock" not found: ID does not exist
, error: exit status 1, failed to stop running pod 1a51d18a2ca0a057853b98a192b8a292d4f635defc959aca278bcbc0dad06c2e: output: I0315 07:32:10.955935 2862424 util_unix.go:103] "Using this endpoint is deprecated, please consider using full URL format" endpoint="/var/run/crio/crio.sock" URL="unix:///var/run/crio/crio.sock"
E0315 07:32:12.959551 2862424 remote_runtime.go:205] "StopPodSandbox from runtime service failed" err="rpc error: code = DeadlineExceeded desc = context deadline exceeded" podSandboxID="1a51d18a2ca0a057853b98a192b8a292d4f635defc959aca278bcbc0dad06c2e"
time="2023-03-15T07:32:12Z" level=fatal msg="stopping the pod sandbox \"1a51d18a2ca0a057853b98a192b8a292d4f635defc959aca278bcbc0dad06c2e\": rpc error: code = DeadlineExceeded desc = context deadline exceeded"
, error: exit status 1, failed to stop running pod 4cd3be7d27419477a5d8a9636e1aabc25bb8dc941db6bc7693d6e344c3239df9: output: I0315 07:32:15.846985 2863136 util_unix.go:103] "Using this endpoint is deprecated, please consider using full URL format" endpoint="/var/run/crio/crio.sock" URL="unix:///var/run/crio/crio.sock"
E0315 07:32:17.852357 2863136 remote_runtime.go:205] "StopPodSandbox from runtime service failed" err="rpc error: code = DeadlineExceeded desc = context deadline exceeded" podSandboxID="4cd3be7d27419477a5d8a9636e1aabc25bb8dc941db6bc7693d6e344c3239df9"
time="2023-03-15T07:32:17Z" level=fatal msg="stopping the pod sandbox \"4cd3be7d27419477a5d8a9636e1aabc25bb8dc941db6bc7693d6e344c3239df9\": rpc error: code = DeadlineExceeded desc = context deadline exceeded"
, error: exit status 1, failed to stop running pod 3f80fed8b30a7137ae2e41645e7b2d546e454433b439720bf0362dcbc9ddb2ac: output: I0315 07:32:18.333559 2863249 util_unix.go:103] "Using this endpoint is deprecated, please consider using full URL format" endpoint="/var/run/crio/crio.sock" URL="unix:///var/run/crio/crio.sock"
E0315 07:32:20.338399 2863249 remote_runtime.go:205] "StopPodSandbox from runtime service failed" err="rpc error: code = DeadlineExceeded desc = context deadline exceeded" podSandboxID="3f80fed8b30a7137ae2e41645e7b2d546e454433b439720bf0362dcbc9ddb2ac"
time="2023-03-15T07:32:20Z" level=fatal msg="stopping the pod sandbox \"3f80fed8b30a7137ae2e41645e7b2d546e454433b439720bf0362dcbc9ddb2ac\": rpc error: code = DeadlineExceeded desc = context deadline exceeded"
, error: exit status 1]
[reset] Deleting contents of directories: [/etc/kubernetes/manifests /etc/kubernetes/pki]
[reset] Deleting files: [/etc/kubernetes/admin.conf /etc/kubernetes/kubelet.conf /etc/kubernetes/bootstrap-kubelet.conf /etc/kubernetes/controller-manager.conf /etc/kubernetes/scheduler.conf]
[reset] Deleting contents of stateful directories: [/var/lib/kubelet /var/lib/dockershim /var/run/kubernetes /var/lib/cni]

The reset process does not clean CNI configuration. To do so, you must remove /etc/cni/net.d

The reset process does not reset or clean up iptables rules or IPVS tables.
If you wish to reset iptables, you must do so manually by using the "iptables" command.

If your cluster was setup to utilize IPVS, run ipvsadm --clear (or similar)
to reset your system's IPVS tables.

The reset process does not clean your kubeconfig files and you must remove them manually.
Please, check the contents of the $HOME/.kube/config file.
```

## Solution

Delete node's pods before reset.

```Bash
root@master-node# kubectl drain {node}
```

Deleting node didn't clear the node's containers.

---

### Reference
- Cluster join Blog KR, https://sinsomi.tistory.com/entry/k8s-node-%EC%B6%94%EA%B0%80-master-node-worker-node-join, 2023-03-15-Wed.
