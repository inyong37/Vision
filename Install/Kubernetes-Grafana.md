# Grafana

Dashboard anything. Observe everything.

Query, visualize, alert on, and understand your data no matter where it’s stored. With Grafana you can create, explore, and share all of your data through beautiful, flexible dashboards.

## Date

2023-06-05-Monday.

## Environment

* Ubuntu 22.04.1 LTS
  * Kubernetes 1.24.13 

## Deploy Grafana on Kubernetes

### Create a file `grafana.yaml`

```yaml
---
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: grafana-pvc
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 1Gi
---
apiVersion: apps/v1
kind: Deployment
metadata:
  labels:
    app: grafana
  name: grafana
spec:
  selector:
    matchLabels:
      app: grafana
  template:
    metadata:
      labels:
        app: grafana
    spec:
      securityContext:
        fsGroup: 472
        supplementalGroups:
          - 0
      containers:
        - name: grafana
          image: grafana/grafana:9.1.0
          imagePullPolicy: IfNotPresent
          ports:
            - containerPort: 3000
              name: http-grafana
              protocol: TCP
          readinessProbe:
            failureThreshold: 3
            httpGet:
              path: /robots.txt
              port: 3000
              scheme: HTTP
            initialDelaySeconds: 10
            periodSeconds: 30
            successThreshold: 1
            timeoutSeconds: 2
          livenessProbe:
            failureThreshold: 3
            initialDelaySeconds: 30
            periodSeconds: 10
            successThreshold: 1
            tcpSocket:
              port: 3000
            timeoutSeconds: 1
          resources:
            requests:
              cpu: 250m
              memory: 750Mi
          volumeMounts:
            - mountPath: /var/lib/grafana
              name: grafana-pv
      volumes:
        - name: grafana-pv
          persistentVolumeClaim:
            claimName: grafana-pvc
---
apiVersion: v1
kind: Service
metadata:
  name: grafana
spec:
  ports:
    - port: 3000
      protocol: TCP
      targetPort: http-grafana
  selector:
    app: grafana
  sessionAffinity: None
  type: LoadBalancer
```

Run the following command:

```Bash
kubectl apply -f grafana.yaml
```

Check that it worked by running the following:

```Bash
kubectl port-forward service/grafana 3000:3000
```

Navigate to `localhost:3000` in your browser. You should see a Grafana login page.

Use `admin` for both the username and password to login.

---

### Reference
- Grafana, https://grafana.com/, 2023-06-05-Mon.
- Install Grafana on Kubernetes, https://grafana.com/docs/grafana/latest/setup-grafana/installation/kubernetes/, 2023-06-05-Mon.
- Start Grafana, https://grafana.com/docs/grafana/latest/getting-started/build-first-dashboard/, 2023-06-05-Mon.
