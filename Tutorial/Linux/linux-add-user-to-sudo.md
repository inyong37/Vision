# Add User to Sudo

## Date

2023-03-29-Wednesday.

## Environment

Debian GNU/Linux 11 (bullseye)

Fedora 37

## Add User to Sudo

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
