# I. Install NVIDIA drivers.
[reference](https://www.mvps.net/docs/install-nvidia-drivers-ubuntu-18-04-lts-bionic-beaver-linux/)
## i. Remove nvidia drivers.
```
sudo apt-get purge nvidia*
```
## ii. Add graphics drivers.
```
sudo add-apt-repositroy ppa:graphics-drivers
sudo apt-get update
sudo apt-get install screen
screen
```
## iii-A. Check your nvidia graphic card's driver version. for example '430'.
```
sudo apt-get install nvidia-430
sudo reboot
```
## iii-B. Updated in 2019-08-22-Thu [Reference](https://askubuntu.com/questions/951046/unable-to-install-nvidia-drivers-unable-to-locate-package)
```
sudo apt-get install nvidia-driver-430
sudo reboot
```
## iv. Verify installation
```
nvidia-smi
```

# II. Setup Korean.
[reference](https://gabii.tistory.com/entry/Ubuntu-1804-LTS-%ED%95%9C%EA%B8%80-%EC%84%A4%EC%B9%98-%EB%B0%8F-%EC%84%A4%EC%A0%95)
```
ibus-setup
```
# III. Errors
## i. Could not get lock /var/lib/dpkg/lock-frontend [Reference](https://kgu0724.tistory.com/71)
```
sudo killall apt apt-get
sudo rm /var/lib/apt/lists/lock
sudo rm /var/cache/apt/archives/lock
sudo rm /var/lib/dpkg/lock*
sudo dpkg --configure -a
sudo apt update
```
