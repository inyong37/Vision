# Change Time Zone

## Date

2023-02-23-Thursday.

2023-06-28-Wednesday.

## Environment

* Ubuntu 22.04.1 LTS

* Ubuntu 22.04.2 LTS

## Change Time Zone

```Bash
timedatectl set-timezone {continent_name/city_name}
# timedatectl set-timezone Asia/Seoul
```

### Verify it using `timedatectl`:

```Bash

               Local time: Thu 2023-02-23 11:37:01 KST
           Universal time: Thu 2023-02-23 02:37:01 UTC
                 RTC time: Thu 2023-02-23 02:37:01
                Time zone: Asia/Seoul (KST, +0900)
System clock synchronized: yes
              NTP service: active
          RTC in local TZ: no
```

---

### Reference
- Change Timezone, https://linuxize.com/post/how-to-set-or-change-timezone-in-linux/, 2023-02-23-Thu.
