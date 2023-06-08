# Add User to Sudo

## Date

2023-03-29-Wednesday.

## Environment

Debian GNU/Linux 11 (bullseye)

Fedora 37

## Add User to Sudo

If you got this error, then you need to set the user to sudoers.

```Bash
{user} is not in the sudoers file. This incident will be reported.
```

### 1. Add User via Editing the Sudoers File

Change to the root:

```Bash
su -
```

Edit "/etc/sudoers"

```Bash
vi /etc/sudoers
```

as below:

```
root ALL=(ALL:ALL) ALL
{user} ALL=(ALL:ALL) ALL # new line
```

:tada: Done

## :construction: 2. Add User to Sudo via usermod -> Not Worked for Me

Change to the root:

```Bash
su -
```

Add {user} to sudo:

```Bash
usermod -aG sudo {user}
```

---

### Reference
- How to add user to group in Linux, https://linuxize.com/post/how-to-add-user-to-group-in-linux/, 2023-03-29-Wed.
- Command usermod not found, https://www.linuxquestions.org/questions/linux-newbie-8/command-usermod-not-found-385901/, 2023-03-29-Wed.
- How to add user to sudiers Blor KR, https://lifegoesonme.tistory.com/460, 2023-03-29-Wed.
