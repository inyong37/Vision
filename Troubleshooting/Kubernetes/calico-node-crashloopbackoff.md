# calico-node

## Date

2023-02-09-Thursday.

## Environment

Ubuntu 22.04.1 LTS

Kubernetes 1.24.10

Calico 3.25.0

## Problem


One of calico-node pod's status is `CrashLoopBackOff`:

```Bash
root@master01:~# kubectl get pods -A -o wide                                                                                                                             [228/1896]
NAMESPACE     NAME                                       READY   STATUS             RESTARTS          AGE   IP                NODE       NOMINATED NODE   READINESS GATES
kube-system   calico-kube-controllers-55fc758c88-9kd84   1/1     Running            0                 2d    10.85.0.4         master01   <none>           <none>
kube-system   calico-node-77n6g                          0/1     Running            0                 2d    192.168.1.238     master01   <none>           <none>
kube-system   calico-node-97d52                          0/1     Running            0                 47h   192.168.1.237     node01     <none>           <none>
kube-system   calico-node-bq2rt                          0/1     CrashLoopBackOff   556 (3m50s ago)   47h   192.168.103.107   node02     <none>           <none>
kube-system   coredns-57575c5f89-dhr9r                   1/1     Running            0                 2d    10.85.0.3         master01   <none>           <none>
kube-system   coredns-57575c5f89-vtbnl                   1/1     Running            0                 2d    10.85.0.2         master01   <none>           <none>
```

The log says:

```Bash
root@master01:~# kubectl logs calico-node-hw6vr -n kube-system
Defaulted container "calico-node" out of: calico-node, upgrade-ipam (init), install-cni (init), mount-bpffs (init)
2023-02-09 05:44:36.050 [INFO][9] startup/startup.go 427: Early log level set to info
2023-02-09 05:44:36.050 [INFO][9] startup/utils.go 127: Using NODENAME environment for node name node02
2023-02-09 05:44:36.051 [INFO][9] startup/utils.go 139: Determined node name: node02
2023-02-09 05:44:36.051 [INFO][9] startup/startup.go 94: Starting node node02 with version v3.25.0
2023-02-09 05:44:36.051 [INFO][9] startup/startup.go 432: Checking datastore connection
2023-02-09 05:44:36.066 [INFO][9] startup/startup.go 456: Datastore connection verified
2023-02-09 05:44:36.066 [INFO][9] startup/startup.go 104: Datastore is ready
2023-02-09 05:44:36.093 [INFO][9] startup/startup.go 485: Initialize BGP data
2023-02-09 05:44:36.095 [INFO][9] startup/autodetection_methods.go 103: Using autodetected IPv4 address on interface weave: 10.32.0.1/12
2023-02-09 05:44:36.095 [INFO][9] startup/startup.go 561: Node IPv4 changed, will check for conflicts
2023-02-09 05:44:36.099 [WARNING][9] startup/startup.go 990: Calico node 'master01' is already using the IPv4 address 10.32.0.1.
2023-02-09 05:44:36.099 [INFO][9] startup/startup.go 391: Clearing out-of-date IPv4 address from this node IP="10.32.0.1/12"
2023-02-09 05:44:36.114 [WARNING][9] startup/utils.go 49: Terminating
Calico node failed to start
```

## Solution #1

Delete and restart autonmatically - didn't work:

```Bash
root@master01:~# kubectl delete pod calico-node-bq2rt -n kube-system
pod "calico-node-bq2rt" deleted
root@master01:~# kubectl get pods -A -o wide
NAMESPACE     NAME                                       READY   STATUS             RESTARTS      AGE    IP                NODE       NOMINATED NODE   READINESS GATES
kube-system   calico-kube-controllers-55fc758c88-9kd84   1/1     Running            0             2d     10.85.0.4         master01   <none>           <none>
kube-system   calico-node-77n6g                          0/1     Running            0             2d     192.168.1.238     master01   <none>           <none>
kube-system   calico-node-97d52                          0/1     Running            0             47h    192.168.1.237     node01     <none>           <none>
kube-system   calico-node-hw6vr                          0/1     CrashLoopBackOff   5 (58s ago)   4m1s   192.168.103.107   node02     <none>           <none>
```
