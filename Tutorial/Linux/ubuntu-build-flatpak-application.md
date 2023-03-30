# Building Flatpak Application

## Date

2023-03-30-Thursday.

## Environment

Ubuntu 22.04.1 LTS

## Building Flatpak Application

### 1. Install a runtime and the matching SDK

```Bash
sudo flatpak install -y flathub org.freedesktop.Platform//22.08 org.freedesktop.Sdk//22.08
```

### 2. Create the app

make directory for workspace:

```Bash
mkdir -p flatpak-test
```

```Bash
vim hello.sh
```

as below:

```sh
#!/bin/sh
echo "Hello world, from a sandbox"
```

### 3. Add a manifest

```Bash
vim org.flatpak.Hello.yml
```

as below:

```yml
app-id: org.flatpak.Hello
runtime: org.freedesktop.Platform
runtime-version: '22.08'
sdk: org.freedesktop.Sdk
command: hello.sh
modules:
  - name: hello
    buildsystem: simple
    build-commands:
      - install -D hello.sh /app/bin/hello.sh
    sources:
      - type: file
        path: hello.sh
```

### 4. Build the application

```Bash
flatpak-builder build-dir org.flatpak.Hello.yml
```

:tada: Output:

```Bash
Downloading sources
Initializing build dir
Committing stage init to cache
Starting build of org.flatpak.Hello
========================================================================
Building module hello in /home/inyong/flatpak-test/.flatpak-builder/build/hello-1
========================================================================
Running: install -D hello.sh /app/bin/hello.sh
Committing stage build-hello to cache
Cleaning up
Committing stage cleanup to cache
Finishing app
Please review the exported files and the metadata
Committing stage finish to cache
Pruning cache
```

:tada: tree:

```Bash
inyong@server:~/flatpak-test$ tree
.
├── build-dir
│   ├── export
│   ├── files
│   │   ├── bin
│   │   │   └── hello.sh
│   │   └── manifest.json
│   ├── metadata
│   └── var
│       ├── lib
│       ├── run -> /run
│       └── tmp
├── hello.sh
└── org.flatpak.Hello.yml

8 directories, 5 files
```

### 5. Test the build

Build:

```Bash
flatpak-builder --user --install --force-clean build-dir org.flatpak.Hello.yml
```

:tada: Output:

```Bash
Emptying app dir 'build-dir'
Downloading sources
Starting build of org.flatpak.Hello
Cache hit for hello, skipping build
Cache hit for cleanup, skipping
Cache hit for finish, skipping
Everything cached, checking out from cache
Exporting org.flatpak.Hello to repo
Commit: 9b13defb5872190eb051121b1140921cc11c65e175c9b7eb606f94a58fc21bd7
Metadata Total: 9
Metadata Written: 2
Content Total: 3
Content Written: 0
Content Bytes Written: 0 (0 bytes)
Installing app/org.flatpak.Hello/x86_64/master
Pruning cache
```

Run:

```Bash
flatpak run org.flatpak.Hello
```

:tada: Output:

```Bash
Hello world, from a sandbox
```

:tada: tree:

```Bash
inyong@server:~/flatpak-test$ tree
.
├── build-dir
│   ├── export
│   ├── files
│   │   ├── bin
│   │   │   └── hello.sh
│   │   └── manifest.json
│   ├── metadata
│   └── var
│       ├── lib
│       ├── run -> /run
│       └── tmp
├── hello.sh
└── org.flatpak.Hello.yml

8 directories, 5 files
```

### 6. Put the app in a repository

```Bash
flatpak-builder --repo={repo} --force-clean build-dir org.flatpak.Hello.yml
```

If you want to share the application you can put it in a repository. This is done by passing the `--repo` argument to `flatpak-builder`.

This does the build again, and at the end exports the result to a local directory called `{repo}`. Note that flatpak-builder keeps a cache of previous builds in the .flatpak-builder subdirectory, so doing a second build like this is very fast.

In order for your application to show up in application stores while testing with a local repository, you might have to run `flatpak build-update-repo repo`.

:tada: Output:

```Bash
Emptying app dir 'build-dir'
Downloading sources
Starting build of org.flatpak.Hello
Cache hit for hello, skipping build
Cache hit for cleanup, skipping
Cache hit for finish, skipping
Everything cached, checking out from cache
Exporting org.flatpak.Hello to repo
Commit: 2b0af3d5191525e896226d34e4eac262cb6b6827e4ef3867ca293d221d33d9ac
Metadata Total: 9
Metadata Written: 6
Content Total: 3
Content Written: 3
Content Bytes Written: 798 (798 bytes)
Pruning cache
```

---

## Install and run the app from the local repo

### Add a repository

This command has to be executed on workspace such as `cd $HOME/flatpak-test`, and `{repo}` is the name of local-repo we used in #6 command:

```Bash
flatpak --user remote-add --no-gpg-verify tutorial-repo {repo}
```

:bulb: See repositories and FYI: remove-delete

```Bash
inyong@server:~/flatpak-test$ flatpak remotes --show-details
Name          Title      URL                                                     Collection ID Subset Filter Priority Options                         … … Homepage             Icon
flathub       Flathub    https://dl.flathub.org/repo/                            -             -      -      1        system                          … … https://flathub.org/ https://dl.flathub.org/repo/logo.svg
tutorial-repo -          file:///home/inyong/flatpak-test/local-repo             -             -      -      1        user,no-gpg-verify              … … -                    -
hello-origin  Local repo file:///home/inyong/flatpak-test/.flatpak-builder/cache -             -      -      0        user,no-enumerate,no-gpg-verify … … -                    -
```

```Bash
inyong@server:~$ flatpak remote-delete tutorial-repo
```

### Install and Run

```Bash
inyong@server:~/flatpak-test$ flatpak --user install tutorial-repo org.flatpak.Hello
Looking for matches…
error: org.flatpak.Hello/x86_64/master is already installed from remote hello-origin
inyong@server:~/flatpak-test$ flatpak run org.flatpak.Hello
Hello world, from a sandbox
```

---

### Reference
- Building your first Flatpak, https://docs.flatpak.org/en/latest/first-build.html, 2023-03-30-Thu.
