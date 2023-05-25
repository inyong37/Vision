# Ingress

Am API Object that manages external access to the services in a cluster, typically HTTP.

Ingress may provide load balancing, SSL termination and name-based virtual hosting.

## What is Ingress?

Ingress exposes HTTP and HTTPS routes from outside the cluster to services within the cluster. Traffic routing is controlled by rules defined on the Ingress resource.

A simple example where an Ingress sends all its traffic to one Service:

```Bash
                                        |              [Cluster]           
client -(Ingress-managed load balancer)-> Ingress -(routing rule)-> Service -> Pod0 
                                        |                                   ㄴ> Pod1
```

An Ingress may be configured to give Services externally-reachable URLs, load balance traffic, terminate SSL/TLS, and offer name-based virtual hosting. An Ingress controller is responsible for fulfilling the Ingress, usually with a load balancer, though it may also configure your edge router or additional frontends to help handle the traffic.

An Ingress does not expose arbitrary ports or protocols. Exposing services other than HTTP and HTTPS to the interent typically uses a service of type Service.Type = NodePort of Service.Type=LoadBalancer.

---

### Reference
- Ingress Kubernetes, https://kubernetes.io/docs/concepts/services-networking/ingress/, 2023-05-25-Thu.
