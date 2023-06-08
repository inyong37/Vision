# Fluent Bit

Fluent Bit is a super fast, lightweight, and highly scalable logging and metrics processor and forwarder. It is the preferred choice for cloud and containerized environments.

## Date

2023-06-05-Monday.

## Environment

* Ubuntu 22.04.1 LTS
  * Kubernetes 1.24.13

## Installation

The recommended way to deploy Fluent Bit is with the official Helm Chart: https://github.com/fluent/helm-charts

### Installing with Helm Chart

Helm is a package manager for Kubernetes and allows you to quickly deploy application packages into your running cluster. Fluent Bit is distributed via a helm chart found in the Fluent Helm Charts repo: https://github.com/fluent/helm-charts.

To add the Fluent Helm Charts repo use the following command

```bash
helm repo add fluent https://fluent.github.io/helm-charts
```

To validate that the repo was added you can run helm search repo fluent to ensure the charts were added. The default chart can then be installed by running the following

```Bash
helm upgrade --install fluent-bit fluent/fluent-bit
```

---

### Reference
- Fluent Bit, https://fluentbit.io/, 2023-06-05-Mon.
- Install Fluent Bit, https://docs.fluentbit.io/manual/installation/getting-started-with-fluent-bit, 2023-06-05-Mon.
- Install Kubernetes Fluent Bit, https://docs.fluentbit.io/manual/installation/kubernetes#installation, 2023-06-05-Mon.
