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

## Ingress Controllers

In order for the Ingress resource to work, the cluster must have an ingress controller running.

Unlike other types of controllers which run as part of the `kube-controller-manager` binary, Ingress controllers are not started automatically with a cluster. 

* AKS Application Gateway Ingress Controller is an ingress controller that configures the Azure Application Gateway.
* Ambassador API Gateway is an Envoy-based ingress controller.
* Apache APISIX ingress controller is an Apache APISIX-based ingress controller.
* Avi Kubernetes Operator provides L4-L7 load-balancing using VMware NSX Advanced Load Balancer.
* BFE Ingress Controller is a BFE-based ingress controller.
* Cilium Ingress Controller is an ingress controller powered by Cilium.
* The Citrix ingress controller works with Citrix Application Delivery Controller.
* Contour is an Envoy based ingress controller.
* EnRoute is an Envoy based API gateway that can run as an ingress controller.
* Easegress IngressController is an Easegress based API gateway that can run as an ingress controller.
* F5 BIG-IP Container Ingress Services for Kubernetes lets you use an Ingress to configure F5 BIG-IP virtual servers.
* FortiADC Ingress Controller support the Kubernetes Ingress resources and allows you to manage FortiADC objects from Kubernetes
* Gloo is an open-source ingress controller based on Envoy, which offers API gateway functionality.
* HAProxy Ingress is an ingress controller for HAProxy.
* The HAProxy Ingress Controller for Kubernetes is also an ingress controller for HAProxy.
* Istio Ingress is an Istio based ingress controller.
* The Kong Ingress Controller for Kubernetes is an ingress controller driving Kong Gateway.
* Kusk Gateway is an OpenAPI-driven ingress controller based on Envoy.
* The NGINX Ingress Controller for Kubernetes works with the NGINX webserver (as a proxy).
* The ngrok Kubernetes Ingress Controller is an open source controller for adding secure public access to your K8s services using the ngrok platform.
* The Pomerium Ingress Controller is based on Pomerium, which offers context-aware access policy.
* Skipper HTTP router and reverse proxy for service composition, including use cases like Kubernetes Ingress, designed as a library to build your custom proxy.
* The Traefik Kubernetes Ingress provider is an ingress controller for the Traefik proxy.
* Tyk Operator extends Ingress with Custom Resources to bring API Management capabilities to Ingress. Tyk Operator works with the Open Source Tyk Gateway & Tyk Cloud control plane.
* Voyager is an ingress controller for HAProxy.
* Wallarm Ingress Controller is an Ingress Controller that provides WAAP (WAF) and API Security capabilities.


---

### Reference
- Ingress Kubernetes, https://kubernetes.io/docs/concepts/services-networking/ingress/, 2023-05-25-Thu.
- Ingress Controllers Kubernetes, https://kubernetes.io/docs/concepts/services-networking/ingress-controllers/, 2023-06-28-Wed.
