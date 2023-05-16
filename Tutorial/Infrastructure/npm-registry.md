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
npm adduser --registry http://0.0.0.0:4873/
```

### Make index.js

```js
console.log("Hello World!");
```

### Make package.json

```json
{
  "name": "@inyong/module1",
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
npm publish --registry http://0.0.0.0:4873/
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
