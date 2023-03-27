# Set-up ngrok

## Date

2023-03-27-Monday.

## Environment

Fedora 37

## Setup ngrok

If you start ngrok without setting authority, you would see this page.

```Bash
ngrok                                                                                                                                                              (Ctrl+C to quit)

Add OAuth and webhook security to your ngrok (its free!): https://ngrok.com/free

Session Status                online
Session Expires               1 hour, 55 minutes
Terms of Service              https://ngrok.com/tos
Version                       3.2.1
Region                        Japan (jp)
Latency                       36ms
Web Interface                 http://127.0.0.1:4040
Forwarding                    https://c660-220-94-163-20.jp.ngrok.io -> http://localhost:8080

Connections                   ttl     opn     rt1     rt5     p50     p90
                              3       0       0.00    0.01    5.00    5.00

HTTP Requests
-------------

GET /favicon.ico               404 Not Found
GET /                          404 Not Found
GET /                          404 Not Found
GET /favicon.ico               404 Not Found
GET /favicon.ico               404 Not Found
GET /                          404 Not Found
```

<img width="1066" alt="Screenshot 2023-03-27 at 2 53 24 PM" src="https://user-images.githubusercontent.com/20737479/227852430-0234c832-ac9f-4aec-809e-4352eae89968.png">

### 1. [Sign up](https://dashboard.ngrok.com/get-started/setup)


### [Verify the Email](https://dashboard.ngrok.com/user/settings)

If you start the ngrok without verifing your email, an error might be occured:

```Bash
ERROR:  The account "inyong" may not start an ngrok agent session until the admin's email address is verified. Verify your email at https://dashboard.ngrok.com/user/settings
ERROR:
ERROR:  ERR_NGROK_123
ERROR:
```

### 2. [Set Authority](https://dashboard.ngrok.com/get-started/your-authtoken) on the Host Machine.

```Bash
ngrok config add-authtoken {personal_token}
```

---

### Reference
- setup ngrok, https://dashboard.ngrok.com/get-started/setup, 2023-03-27-Mon.
- authtoken ngrok, https://dashboard.ngrok.com/get-started/your-authtoken, 2023-03-27-Mon.
