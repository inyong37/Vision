# Vision Processing
OpenCV & Python & TensorFlow & Keras

## I. Install
### i.    [Install OpenCV on Computer](https://github.com/inyong37/Vision/blob/master/Install/OpenCV-Computer.md)
### ii.   [Install OpenCV on Raspberry Pi](https://github.com/inyong37/Vision/blob/master/Install/OpenCV-RaspberryPi.md)
### iii.  [Install TensorFlow CPU on Computer](https://github.com/inyong37/Vision/blob/master/Install/TensorFlow-Computer-CPU.md)
### iv.   [Install TensorFlow GPU on Computer](https://github.com/inyong37/Vision/blob/master/Install/TensorFlow-Computer-GPU.md)
### v.    [Install TensorFlow on Raspberry Pi](https://github.com/inyong37/Vision/blob/master/Install/TensorFlow-RaspberryPi.md)
### vi.   [Install Keras](https://github.com/inyong37/Vision/blob/master/Install/Keras.md)
### vii.  [Install Keras-Reinforcement Learning](https://github.com/inyong37/Vision/blob/master/Install/Keras-rl.md)
### 
### viii. [Virtual Environment with Conda](https://github.com/inyong37/Vision/blob/master/Install/Virtual-Environment_conda.md)

## II. Uninstall
### i.    [Unstall OpenCV on Raspberry Pi](https://github.com/inyong37/Vision/blob/master/Uninstall/OpenCV-RaspberryPi.md)

----------

## I. Dehazing to Object Detection (Human & Fire)
### Image Processing with OpenCV
#### Human detection with RPi
reference: https://github.com/OmalPerera/Human-detection-system-with-raspberry-Pi/blob/master/pi_surveillance.py
#### HOG detectMultiScale (1)
reference: http://hamait.tistory.com/509
#### HOG detectMultiScale (2)
reference: https://www.pyimagesearch.com/2015/11/16/hog-detectmultiscale-parameters-explained/
### Deep Learning

## II. Vanishing Point to Control Posture
Image Processing

## III. Optical Character Recognition to Path Planning
Deep Learning

## IV. Depth to Obstacle Avoidance
#### NYU Dataset V1
reference: https://cs.nyu.edu/~silberman/datasets/nyu_depth_v1.html
#### NYU Dataset V2
reference: https://cs.nyu.edu/~silberman/datasets/nyu_depth_v2.html
#### How to read NYU mat file with python
reference: https://ddokkddokk.tistory.com/21
#### Install Packages for Depth Processing
```
pip install scikit-image
python -m pip install -U matplotlib
```
reference: http://scikit-image.org/docs/dev/install.html

reference: https://matplotlib.org/users/installing.html
#### Change Code for Windows/OS X
```
import skimage.io as io
```
to 
```
import matplotlib
matplotlib.use('TkAgg')
from skimage import io
io.use_plugin('matplotlib')
```
reference: https://github.com/scikit-image/scikit-image/issues/2595
#### RGBD Dataset
reference: http://www.open3d.org/docs/tutorial/Basic/rgbd_images/index.html#
