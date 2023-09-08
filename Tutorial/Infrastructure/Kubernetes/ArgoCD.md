# [Argo CD](https://argoproj.github.io/cd/)

Argo CD is a declarative, GitOps continuous delivery tool for Kubernetes.

Application definitions, configurations, and environments should be declarative and version controlled. Application deployment and lifecycle management should be automated, auditable, and easy to understand.

## Date

2023-06-05-Monday.

## Environment

* Ubuntu 22.04.1 LTS
  * Kubernetes 1.24.13

## Quick Start

```Bash
kubectl create namespace argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
```

---

## Architecture

![image](https://github.com/inyong37/Vision/assets/20737479/f4f79dd8-6266-46a4-86bf-b2d48b7f327e)

---

### Reference
- ArgoCD, https://argoproj.github.io/cd/, 2023-09-08-Fri.
- Argo CD, https://argo-cd.readthedocs.io/en/stable/, 2023-06-05-Mon.
