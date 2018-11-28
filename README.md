# Vision Processing
OpenCV & Python & TensorFlow & Keras

## Install OpenCV on Raspberry Pi
### 간단한 방법
```
sudo apt-get install python-opencv
```
### 복잡한 방법
Reference: https://www.pyimagesearch.com/2018/09/26/install-opencv-4-on-your-raspberry-pi/
### 1. Enable Camera
```
sudo -s
raspi-config
```
```
5 Interfaceing Option
P1 Camera
```
```
apt-get update
apt-get upgrade
reboot
```
### 2. Install dependencies
```
sudo -s
apt-get install build-essential cmake unzip pkg-config libjpeg-dev libpng-dev libtiff-dev libavcodec-dev libavformat-dev libswscale-dev libv4l-dev libxvidcore-dev libx264-dev libgtk-3-dev libcanberra-gtk* libatlas-base-dev gfortran python3-dev libgtk2.0-dev pkg-config
```
### 3. Download OpenCV
```
cd ~
```
#### 3-1. OpenCV-4.0.0-alpha
```
wget -O opencv.zip https://github.com/opencv/opencv/archive/4.0.0-alpha.zip
wget -O opencv_contrib.zip https://github.com/opencv/opencv_contrib/archive/4.0.0-alpha.zip
unzip opencv.zip
unzip opencv_contrib.zip
mv opencv-4.0.0-alpha opencv
mv opencv_contrib-4.0.0-alpha opencv_contrib
```
#### 3-2. OpenCV-3.4.4 (X)
```
wget -O opencv.zip https://github.com/opencv/opencv/archive/3.4.4.zip
wget -O opencv_contrib.zip https://github.com/opencv/opencv_contrib/archive/3.4.4.zip
unzip opencv.zip
unzip opencv_contrib.zip
mv opencv-3.4.4 opencv
mv opencv_contrib-3.4.4 opencv_contrib
```
### 4. CMake and compile
```
cd opencv
mkdir build
cd build
cmake -D CMAKE_BUILD_TYPE=RELEASE \
    -D CMAKE_INSTALL_PREFIX=/usr/local \
    -D OPENCV_EXTRA_MODULES_PATH=~/opencv_contrib/modules \
    -D ENABLE_NEON=ON \
    -D ENABLE_VFPV3=ON \
    -D BUILD_TESTS=OFF \
    -D INSTALL_PYTHON_EXAMPLES=OFF \
    -D BUILD_EXAMPLES=OFF ..
```
### 5. Increase SWAP
```
nano /etc/dphys-swapfile
```
```
# set size to absolute value, leaving empty (default) then uses computed value
#   you most likely don't want this, unless you have an special disk situation
CONF_SWAPSIZE=2048
```
```
/etc/init.d/dphys-swapfile stop
/etc/init.d/dphys-swapfile start
```
### 6. Compile OpenCV
```
cd ~
cd opencv/build
```
```
make -j4
make install
ldconfig
```
### 7. Test OpenCV
```
$ python
```
```
>> import cv2
>> exit()
```
----------
## Dehazing to Object Detection (Human & Fire)
Image Processing

Deep Learning
## Vanishing Point to Control Posture
Image Processing

## Optical Character Recognition to Path Planning
Deep Learning

## Depth to Obstacle Avoidance
Deep Learning
