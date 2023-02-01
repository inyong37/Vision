# Kubernetes apply/create fail during installing rook-ceph

## Environment

Ubuntu 18.04.6 LTS

Kubernetes 1.26.0

## Date

2023-01-25-Wednesday.

## Problem

<img width="1118" alt="Screenshot 2023-01-26 at 10 58 35 AM" src="https://user-images.githubusercontent.com/20737479/214740607-94f43227-3019-45a5-ba27-e92b39e20666.png">

## Solution

The problem was rook-ceph is using deprecated (removed) API of Kubernetes.

Therefore I have to check the new API for rook-ceph or downgrade the Kubernetes.

---

### Reference
- Deprecated API Migration Guide, https://kubernetes.io/docs/reference/using-api/deprecation-guide/, 2023-01-26-Thu.
