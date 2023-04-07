# Scale the Service in the Swarm

## Date

2022-11-21-Monday.

2023-04-07-Friday.

## Environment

Ubuntu 20.04.4 LTS

Docker 23.0.3

### [Scale the service in the swarm](https://docs.docker.com/engine/swarm/swarm-tutorial/scale-service/) | [Blog (KR)](https://sarc.io/index.php/cloud/1775-docker-19)

Once you have deployed a service to a swarm, you are ready to use the Docker CLI to scale the number of containers in the service. Continers running in a service are called "tasks".

1. If you haven't alreday, open a terminal and ssh into the machine where you run your manager node. For example, the tutorial uses a machine named `manager1`.

2. Run the following command to change the desired state of the service running in the swarm:
    - ```bash
      $ docker service scale <SERVICE-ID>=<NUMBER-OF-TASKS>
      ```

3. Run `docker service ps <SERVICE-ID>` to see the updated task list:
    - ```bash
      $ docker service ps helloworld

      NAME                                    IMAGE   NODE      DESIRED STATE  CURRENT STATE
      helloworld.1.8p1vev3fq5zm0mi8g0as41w35  alpine  worker2   Running        Running 7 minutes
      helloworld.2.c7a7tcdq5s0uk3qr88mf8xco6  alpine  worker1   Running        Running 24 seconds
      helloworld.3.6crl09vdcalvtfehfh69ogfb1  alpine  worker1   Running        Running 24 seconds
      helloworld.4.auky6trawmdlcne8ad8phb0f1  alpine  manager1  Running        Running 24 seconds
      helloworld.5.ba19kca06l18zujfwxyc5lkyn  alpine  worker2   Running        Running 24 seconds
      ```
    - You can see that swarm has created 4 new tasks to scale to a total of 5 running instances of Alpine Linux. THe tasks are distributed between the three nodes of the warm. One is running on `manager1`.

4. Run `docker ps` to see the containers running on the node where you're connected. THe following example shows the tasks running on `manager1`:
    - ```bash
      docker ps

      CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
      528d68040f95        alpine:latest       "ping docker.com"   About a minute ago   Up About a minute                       helloworld.4.auky6trawmdlcne8ad8phb0f1
      ```
    - If you want to see the containers running on other nodes, ssh into those nodes and run the `docker ps` command.

---

### Reference
- Scale the service in the swarm Docker Docs, https://docs.docker.com/engine/swarm/swarm-tutorial/scale-service/, 2022-11-21-Mon.
- Docker 가상 환경 구축 입문 (19) - 서비스 스케일링 Blog KR, https://sarc.io/index.php/cloud/1775-docker-19, 2023-04-07-Fri.
