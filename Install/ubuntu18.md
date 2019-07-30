# I. Install NVIDIA drivers
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
## iii. Check your nvidia graphic card's driver version. for example '430'.
```
sudo apt-get install nvidia 430
sudo reboot
```
### iv. Verify installation
```
nvidia-smi
```

## II. 
