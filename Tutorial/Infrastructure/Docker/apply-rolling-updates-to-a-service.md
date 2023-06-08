# Apply Rolling Update to a Service

## Date

2022-11-21-Monday.

2023-04-07-Friday.

## Environment

Ubuntu 20.04.4 LTS

Docker 23.0.3

### Apply rolling updates to a service

1. If you haven't already, open a terminal and ssh into the machine where you run your manage node. For example, the tutorial uses a machine named `manager1`.

2. Deploy your Redis tag to the swarm and configure the swarm with a 10 second update delay. Note that the following example shows an older Redis tag:
    - ```bash
      $ docker service create --replicas 3 --name redis --update-delay 10s redis:3.0.6
      ```

3. Inspect the `redis` service:
    - ```bash
      $ docker service inspect --pretty redis
      
      ...
      UpdateConfig:
       Parallelism: 1
       Delay:       10s
      ...
      ```

4. Now you can update the container image for `redis`. The swarm manager applies the update to nodes according to the `UpdateConfig` policy:
    - ```bash
      $ docker service update --image redis:3.0.7 redis
      ```
    - The scheduler applies rolling updates as follows by default:
      - Stop the first task.
      - Schedule update for the stopped task.
      - Start the container for the updated task.
      - If the update to a task returns `RUNNING`, wait for the specified delay period then start the next task.
      - If, at any time during the update, a task returns `FAILED`, pause the update.

5. Run `docker service inspect --pretty redis` to see the new image in the desired state:
    - ```bash
      $ docker service inspect --pretty redis
      ```
    - The output of `service inspect` shows if your update paused due to failure:
    - ```bash
      $ docker service inspect --pretty redis

      ID:             0u6a4s31ybk7yw2wyvtikmu50
      Name:           redis
      ...snip...
      Update status:
       State:      paused
       Started:    11 seconds ago
       Message:    update paused due to failure or early termination of task 9p7ith557h8ndf0ui9s0q951b
      ...snip...
      ```
    - To restart a paused update run `docker service update <SERVICE-ID>`. For example:
    - ```bash
      $ docker service update redis
      ```
    - To avoid repeating certain update failures, you may need to reconfigure the service by passing flags to `docker service update`.

6. Run `docker service ps <SERVICE-ID>` to watch the rolling update:
    - ```bash
      $ docker service ps redis

      NAME                                   IMAGE        NODE       DESIRED STATE  CURRENT STATE            ERROR
      redis.1.dos1zffgeofhagnve8w864fco      redis:3.0.7  worker1    Running        Running 37 seconds
       \_ redis.1.88rdo6pa52ki8oqx6dogf04fh  redis:3.0.6  worker2    Shutdown       Shutdown 56 seconds ago
      redis.2.9l3i4j85517skba5o7tn5m8g0      redis:3.0.7  worker2    Running        Running About a minute
       \_ redis.2.66k185wilg8ele7ntu8f6nj6i  redis:3.0.6  worker1    Shutdown       Shutdown 2 minutes ago
      redis.3.egiuiqpzrdbxks3wxgn8qib1g      redis:3.0.7  worker1    Running        Running 48 seconds
       \_ redis.3.ctzktfddb2tepkr45qcmqln04  redis:3.0.6  mmanager1  Shutdown       Shutdown 2 minutes ago
      ```

---

### Reference
- Rolling Update Docker, https://docs.docker.com/engine/swarm/swarm-tutorial/rolling-update/, 2022-11-21-Mon.
- Rolling Updates Blog KR, https://sarc.io/index.php/cloud/1759-docker-18-rolling-update, 2022-11-21-Mon.
