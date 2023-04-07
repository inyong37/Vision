# Moving a File from a Container to Host OS

## Date

2022-10-27-Thursday.

## Environment

Ubuntu 20.04.4 LTS

## Get a File from a Container

```Bash
sudo docker cp {container_id or container_name}:/home/{user_name}/{file_name} /home/{user_name}/
```

---

### Reference
- Send a file to/from Container Stackoverflow, https://stackoverflow.com/questions/22907231/how-to-copy-files-from-host-to-docker-container, 2022-10-27-Thu.
