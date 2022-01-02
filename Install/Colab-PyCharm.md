# Use Colab in PyCharm

## I. Setup ngrok
### i. Sgin-Up/In

### ii. Get authtoken

## II. Setup Colab
### i. Define default setup
```Python
from google.colab import drive
drive.mount('/content/drive')
NGROK_TOKEN = '{YOUR_TOKEN}'
PASSWORD = '{YOUR_PASSWORD}'
```

### ii. Install colab-ssh
```Python
!pip install colab-ssh
```

### iii. Get `HostName`, `Port`, and `User` | [Related issue](https://github.com/WassimBenzarti/colab-ssh/issues/45)
```Python
from colab_ssh import launch_ssh
launch_ssh(NGROK_TOKEN, PASSWORD)
```

## III. Setup PyCharm | **only in Professional Version**
### i. Add Python Interpreter | [Configure an interpreter using SSH](https://www.jetbrains.com/help/pycharm/configuring-remote-interpreters-via-ssh.html)
- Host: `{HostName}`
- Port: `{Port}`
- Username: `{User}`
- Password: `{PASSWORD}`
- Interpreter: `/usr/bin/python3`

----------

#### Reference
- Use Colab in Visual Studio Code/PyCharm Blog KR, https://velog.io/@taki0412/%EA%B5%AC%EA%B8%80-Colab-%EC%84%9C%EB%B2%84%EB%A5%BC-%EB%A1%9C%EC%BB%AC%EC%97%90%EC%84%9C-%EC%82%AC%EC%9A%A9%ED%95%98%EA%B8%B0, 2022-01-02-Sun.
- colab-ssh issue GitHub, https://github.com/WassimBenzarti/colab-ssh/issues/45, 2022-01-03-Mon.
- Configure an interpreter using SSH JetBrain, https://www.jetbrains.com/help/pycharm/configuring-remote-interpreters-via-ssh.html, 2022-01-03-Mon.
