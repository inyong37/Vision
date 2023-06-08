# Setup NPM Registry with verdaccio and Docker

## Date

2023-05-15-Monday.

## Environment

- Ubuntu 22.04.2 LTS
  - Docker 23.0.3
- Ubuntu 20.04.4 LTS
  - Docker 23.0.6

## Setup NPM Package Registry "Verdaccio" with Docker

### Deploy Docker Image Container

```Bash
docker pull verdaccio/verdaccio
docker run -it --rm --name verdaccio -p 4873:4873 verdaccio/verdaccio
```

### Setup

```Bash
npm adduser --registry http://0.0.0.0:4873/ # ID, PASSWORD
```

### Make `workspace/index.js`

```js
console.log("Hello World!");
```

### Make `workspace/package.json`

```json
{
  "name": "@inyong/test",
  "version": "0.0.1",
  "main": "index.js",
  "dependencies": {},
  "devDependencies": {},
  "keywords": [],
  "author": "In Yong Hwang",
  "license": "MIT",
  "description": ""
}
```

### Publish

```Bash
cd ~/workspace
npm publish --registry http://0.0.0.0:4873/
```

### :tada: Logs

```Bash
npm notice
npm notice 📦  @inyong/test@0.0.1
npm notice === Tarball Contents ===
npm notice 29B  index.js
npm notice 208B package.json
npm notice === Tarball Details ===
npm notice name:          @inyong/test
npm notice version:       0.0.1
npm notice filename:      @inyong/test-0.0.1.tgz
npm notice package size:  285 B
npm notice unpacked size: 237 B
npm notice shasum:        2cbb502d1f74a47fe8e8c9548b7f43b3a660646e
npm notice integrity:     sha512-moj7Y0gPYIPwb[...]01bTXnMw8HPLg==
npm notice total files:   2
npm notice
npm notice Publishing to http://0.0.0.0:4873/
+ @inyong/test@0.0.1
```

### :tada: `http://{ip_address}:4873/`

<img width="1200" alt="Screenshot 2023-05-17 at 10 21 21 AM" src="https://github.com/inyong37/Vision/assets/20737479/6ae61cc7-4d32-4560-ab63-b755dcf50bfc">

---

## Errors

### Error 1: publishing without `index.js` and `package.json`; `no such file or directory package.json`

### Error 2: publishing in home directory; `cannot create a string longer than 0x1fffffe8 characters`

```Bash
npm notice === Tarball Details ===
npm notice name:          @inyong/module1
npm notice version:       0.0.1
npm notice filename:      @inyong/module1-0.0.1.tgz
npm notice package size:  1.8 GB
npm notice unpacked size: 4.2 GB
npm notice shasum:        54e820f12992c814ef4f7fba3d91b2727fc03837
npm notice integrity:     sha512-IR7HRTrGdCQtx[...]9NLURcFaCtWQA==
npm notice total files:   149844
npm notice
npm notice Publishing to http://0.0.0.0:4873/
npm ERR! code ERR_STRING_TOO_LONG
npm ERR! Cannot create a string longer than 0x1fffffe8 characters

npm ERR! A complete log of this run can be found in:
npm ERR!     /root/.npm/_logs/2023-05-16T06_38_33_573Z-debug-0.log
```

---

## Edit `config.yaml`

일반적인 접속으로는 `config.yaml` 파일을 수정할 수 없어서 처음부터 root로 접속한다(sudo, su가 안되므로 root 접속 방법이 수월함).

```bash
docker exec -it --user root {container_name} /bin/sh
```

```bash
vi /verdaccio/conf/config.yaml
```

수정하고는 localhost는 docker restart하면 적용이 되지만, 외부 접속은 바로 적용이 되지 않음.

publish를 하면 됨. publish할 때마다 version을 올려야하는 단점이 있음.

---

## Usage

npm 명령어 뒤에 `--registry [http://192.168.10.80:4873/](http://192.168.10.80:4873/)` 을 붙여야함.

```bash
npm set registry http://192.168.10.80:4873/
npm adduser --registry http://192.168.10.80:4873/
npm login --registry http://192.168.10.80:4873/
npm whoami --registry http://192.168.10.80:4873/
npm publish --registry http://192.168.10.80:4873/
npm unpublish --registry http://192.168.10.80:4873/
```

adduser 시 ID, Password, Email을 넣어야함.

---

## Authority in `config.yaml`

```yaml
packages:
  '@auth/*':
    access: $all
    publish: 'publish-user'
    unpublish: 'admin'
    proxy: npmjs
```

---

### Reference
- Install Verdaccio Docker, https://verdaccio.org/docs/docker/, 2023-05-15-Mon.
- Install Verdaccio with Heroku GitHub, https://github.com/juanpicado/verdaccio-heroku-example, 2023-05-15-Mon.
- NPM, https://docs.npmjs.com/cli/v8/using-npm/registry, 2023-05-16-Tue.
- NPM Registry, https://docs.npmjs.com/cli/v8/using-npm/registry, 2023-05-16-Tue.
- Install Verdaccio with Docker, https://verdaccio.org/docs/docker/, 2023-05-15-Mon.
- NPM Registry with verdaccio Blog KR, https://mygumi.tistory.com/371, 2023-05-16-Tue.
- Verdaccio GitHub, https://github.com/verdaccio/verdaccio, 2023-05-16-Tue.
- Verdaccio Docker Examples GitHub, https://github.com/verdaccio/verdaccio/tree/master/docker-examples, 2023-05-16-Tue.
- no such file or directory package.json Blog KR, https://xenostudy.tistory.com/520, 2023-05-16-Tue.
- How to run bash as user root on alpine images with docker? Stackoverflow, https://stackoverflow.com/questions/61683448/how-to-run-bash-as-user-root-on-alpine-images-with-docker-su-must-be-suid-to-w, 2023-05-18-Thu.
- WebUI Verdaccio, https://verdaccio.org/docs/webui/, 2023-05-18-Thu.
- Verdaccio Blog KR, https://velog.io/@army262/verdaccio-private-npm, 2023-05-18-Thu.
