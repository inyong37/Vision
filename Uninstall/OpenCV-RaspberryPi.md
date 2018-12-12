## Uninstall OpenCV on Raspberry Pi

reference: http://www.srccodes.com/p/article/56/uninstall-remove-opencv-raspberry-pi-jessie-debain-make-uninstall-open-source-computer-vision-opencvlib

### A. Installed using apt-get

```
sudo -s
pkg-config --modversion opencv
dpkg -l libopencv*
apt-get purge libopencv*
dpkg -r opencv
```

### B. Installed using make

```
sudo -s
cd ~/opencv/build
make uninstall
```
