# Prometheus

From metrics to insight.

Power your metrics and alerting with the leading open-source monitoring solution.

## Date

2023-06-05-Monday.

## Environment

* Ubuntu 22.04.1 LTS
  * Kubernetes 1.24.13

## Install Prometheus Operator

### Install the Operator using the `bundle.yaml` file in the Prometheus Operator GitHub repository:

```Bash
kubectl create -f https://raw.githubusercontent.com/prometheus-operator/prometheus-operator/master/bundle.yaml
```

Verify that the Prometheus Operator installation succeeded using kubectl:

```Bash
kubectl get deploy
---
NAME                  READY   UP-TO-DATE   AVAILABLE   AGE
prometheus-operator   1/1     1            1           3m21s
```

### Configure Prometheus RBAC Permissions

```Bash
mkdir operator_k8s
cd operator_k8s
```

Create a manifest file called `prom_rbac.yaml` using an editor and paste in the following Kubernetes manifest:

```yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  name: prometheus
---
apiVersion: rbac.authorization.k8s.io/v1beta1
kind: ClusterRole
metadata:
  name: prometheus
rules:
- apiGroups: [""]
  resources:
  - nodes
  - nodes/metrics
  - services
  - endpoints
  - pods
  verbs: ["get", "list", "watch"]
- apiGroups: [""]
  resources:
  - configmaps
  verbs: ["get"]
- apiGroups:
  - networking.k8s.io
  resources:
  - ingresses
  verbs: ["get", "list", "watch"]
- nonResourceURLs: ["/metrics"]
  verbs: ["get"]
---
apiVersion: rbac.authorization.k8s.io/v1beta1
kind: ClusterRoleBinding
metadata:
  name: prometheus
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: prometheus
subjects:
- kind: ServiceAccount
  name: prometheus
  namespace: default
```

This creates a ServiceAccount called prometheus and binds it to the prometheus ClusterRole. The manifest grants the ClusterRole get, list, and watch Kubernetes API privileges.

When you’re done editing the manifest, save and close it.

Create the objects using `kubectl`:

```Bash
kubectl apply -f
```

### Deploy Prometheus

Create a file called `prometheus.yaml` and paste in the following manifest:

```yaml
apiVersion: monitoring.coreos.com/v1
kind: Prometheus
metadata:
  name: prometheus
  labels:
    app: prometheus
spec:
  image: quay.io/prometheus/prometheus:v2.22.1
  nodeSelector:
    kubernetes.io/os: linux
  replicas: 2
  resources:
    requests:
      memory: 400Mi
  securityContext:
    fsGroup: 2000
    runAsNonRoot: true
    runAsUser: 1000
  serviceAccountName: prometheus
  version: v2.22.1
  serviceMonitorSelector: {}
```

Deploy the manifest into your cluster using `kubectl apply -f`:

```bash
kubectl apply -f
```

### Create a Prometheus service

Open a manifest file called `prom_svc.yaml` and paste in the following definitions:

```yaml
apiVersion: v1
kind: Service
metadata:
  name: prometheus
  labels:
    app: prometheus
spec:
  ports:
  - name: web
    port: 9090
    targetPort: web
  selector:
    app.kubernetes.io/name: prometheus
  sessionAffinity: ClientIP
```

Create the service using `kubectl apply -f`:

```Bash
kubectl apply -f prom_svc.yaml
```

Access the Prometheus server by forwarding a local port to the Prometheus service running inside of the Kubernetes cluster:

```bash
kubectl port-forward svc/prometheus 9090
```

### Create a Prometheus ServiceMonitor

Create a file called `prometheus_servicemonitor.yaml` and paste in the following ServiceMonitor resource definition:

```yaml
apiVersion: monitoring.coreos.com/v1
kind: ServiceMonitor
metadata:
  name: prometheus-self
  labels:
    app: prometheus
spec:
  endpoints:
  - interval: 30s
    port: web
  selector:
    matchLabels:
      app: prometheus
```

```Bash
kubectl apply -f prometheus_servicemonitor.yaml
```

### Verify your updates

```Bash
kubectl port-forward svc/prometheus 9090
```

---

### Reference
- Prometheus, https://prometheus.io/, 2023-06-05-Mon.
- Download Prometheus, https://prometheus.io/download/, 2023-06-05-Mon.
- Install Prometheus Operator with Grafana Cloud for Kubernetes, https://grafana.com/docs/grafana-cloud/kubernetes-monitoring/other-methods/prometheus/prometheus_operator/, 2023-06-05-Mon.
