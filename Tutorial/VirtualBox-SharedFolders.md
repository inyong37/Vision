# [Sharing folder between Host OS and Guest OS in VirtualBox](https://ndb796.tistory.com/378)

## Environment

Host OS: Ubuntu (20.04.4 LTS), VirtualBox 6.1

Guest OS: Ubuntu (18.04.6 LTS)

## Host OS

Guest OS>Settings>Shared Folders>Adds new shared folder.

Add Share:
- Folder Path: `/home/user/share` # Create folder to share
- Folder Name: `share`
- Auto-mount check
- Make Permanent check
- OK

OK

## Guest OS

```Bash
$ sudo mkdir /mnt/share # folder to use for sharing
$ sudo mount -t vboxsf share /mnt/share # name set by Host OS and folder path
```

> <img width="214" alt="Screenshot 2023-01-25 at 3 50 06 PM" src="https://user-images.githubusercontent.com/20737479/214498725-e7e26bc9-fa40-4584-a63e-4631fe0a0d42.png">

---

### Reference

- Oracle VM VirtualBox에서 호스트(Host)와 게스트(Guest) 공유 폴더 설정하기, https://ndb796.tistory.com/378, 2023-01-25-Wed.
