# Vision Processing
OpenCV & Python & TensorFlow & Keras

## I. Install
### i.    [Install OpenCV on Computer](https://github.com/inyong37/Vision/blob/master/Install/OpenCV-Computer.md)
### ii.   [Install OpenCV on Raspberry Pi](https://github.com/inyong37/Vision/blob/master/Install/OpenCV-RaspberryPi.md)
### iii.  [Install TensorFlow CPU on Computer](https://github.com/inyong37/Vision/blob/master/Install/TensorFlow-Computer-CPU.md)
### iv.   [Install TensorFlow GPU on Computer](https://github.com/inyong37/Vision/blob/master/Install/TensorFlow-Computer-GPU.md)
### v.    [Install TensorFlow on Raspberry Pi](https://github.com/inyong37/Vision/blob/master/Install/TensorFlow-RaspberryPi.md)
### vi.   [Install Keras](https://github.com/inyong37/Vision/blob/master/Install/Keras.md)
### vii.  [Install Keras Reinforcement Learning](https://github.com/inyong37/Vision/blob/master/Install/Keras-ReinforcementLearning.md)
### viii. [Install Pytorch](https://github.com/inyong37/Vision/blob/master/Install/Pytorch.md)
### ix. [Install Theano](https://github.com/inyong37/Vision/blob/master/Install/Theano.md)
### x. [Virtual Environment with Conda](https://github.com/inyong37/Vision/blob/master/Install/Virtual-Environment_conda.md)

## II. Uninstall
### i.    [Unstall OpenCV on Raspberry Pi](https://github.com/inyong37/Vision/blob/master/Uninstall/OpenCV-RaspberryPi.md)

----------

## I. Dehazing to Object Detection (Human & Fire) (TODO)
### i. Image Processing with OpenCV
#### Human detection with RPi
Reference: https://github.com/OmalPerera/Human-detection-system-with-raspberry-Pi/blob/master/pi_surveillance.py
#### HOG detectMultiScale (1)
Reference: http://hamait.tistory.com/509
#### HOG detectMultiScale (2)
Reference: https://www.pyimagesearch.com/2015/11/16/hog-detectmultiscale-parameters-explained/
#### Dark Channel Prior [Paper](http://www.robots.ox.ac.uk/~vgg/rg/papers/hazeremoval.pdf)
Reference: https://github.com/anhenghuang/dehaze
### ii. Deep Learning
#### A. Dataset
Reference: https://www.researchgate.net/post/Is_there_exists_any_haze_fog_dust_smog_removal_images_data-set_with_ground_truth_images
#### a. RESIDE: V0 (REalistic Single Image DEhazing) [Paper (arXiv)](https://arxiv.org/pdf/1712.04143.pdf) [Paper (IEEE)](https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=8451944)
Reference: https://sites.google.com/view/reside-dehaze-datasets/reside-v0
#### b. I-Haze [Paper (arXiv)](https://arxiv.org/abs/1804.05091)
Reference: http://www.vision.ee.ethz.ch/ntire18/i-haze/
#### c. D-Hazy [Paper (IEEE)](https://ieeexplore.ieee.org/document/7532754)
Reference: http://www.meo.etc.upt.ro/AncutiProjectPages/D_Hazzy_ICIP2016/)
#### d. O-Haze [Paper (arXiv)](https://arxiv.org/abs/1804.05101)
### iii. Challenge
#### NTIRE2018
Reference: http://www.vision.ee.ethz.ch/ntire18/

## II. Vanishing Point to Control Posture
Image Processing

## III. Depth to Obstacle Avoidance (TODO)
### i. Deep Learning
#### A. Dataset
#### a. NYU Dataset V1 [Paper](https://cs.nyu.edu/~silberman/papers/indoor_seg_struct_light.pdf)
Reference: https://cs.nyu.edu/~silberman/datasets/nyu_depth_v1.html
#### b. NYU Dataset V2 [Paper](https://cs.nyu.edu/~silberman/papers/indoor_seg_support.pdf)
Reference: https://cs.nyu.edu/~silberman/datasets/nyu_depth_v2.html
#### How to read NYU mat file with python
Reference: https://ddokkddokk.tistory.com/21
#### Packages
```
pip install scikit-image
```
Reference: http://scikit-image.org/docs/dev/install.html
```
python -m pip install -U matplotlib
```
Reference: https://matplotlib.org/users/installing.html
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
Reference: https://github.com/scikit-image/scikit-image/issues/2595
#### c. RGBD Dataset
Reference: http://www.open3d.org/docs/tutorial/Basic/rgbd_images/index.html#

#### B. Model
#### a. FCRN [Paper (arXiv)](https://arxiv.org/abs/1606.00373)
Reference: https://github.com/iro-cp/FCRN-DepthPrediction

## IV. Optical Character Recognition to Path Planning (TODO)
Deep Learning
