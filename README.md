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
#### Human detection with RPi [Github](https://github.com/OmalPerera/Human-detection-system-with-raspberry-Pi/blob/master/pi_surveillance.py)
#### HOG detectMultiScale [Korean](http://hamait.tistory.com/509), [English](https://www.pyimagesearch.com/2015/11/16/hog-detectmultiscale-parameters-explained/)
#### Dark Channel Prior [Github](https://github.com/anhenghuang/dehaze), [Paper](http://www.robots.ox.ac.uk/~vgg/rg/papers/hazeremoval.pdf)
### ii. Deep Learning
#### A. Dataset [Reference](https://www.researchgate.net/post/Is_there_exists_any_haze_fog_dust_smog_removal_images_data-set_with_ground_truth_images)
#### a. [RESIDE: V0 (REalistic Single Image DEhazing)](https://sites.google.com/view/reside-dehaze-datasets/reside-v0), [Paper (arXiv)](https://arxiv.org/pdf/1712.04143.pdf), [Paper (IEEE)](https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=8451944)
#### b. [I-Haze](http://www.vision.ee.ethz.ch/ntire18/i-haze/), [Paper (arXiv)](https://arxiv.org/abs/1804.05091)
#### c. [D-Hazy](http://www.meo.etc.upt.ro/AncutiProjectPages/D_Hazzy_ICIP2016/), [Paper (IEEE)](https://ieeexplore.ieee.org/document/7532754)
#### d. O-Haze [Paper (arXiv)](https://arxiv.org/abs/1804.05101)
### iii. Challenge
#### [NTIRE2018](http://www.vision.ee.ethz.ch/ntire18/)

## II. Vanishing Point to Control Posture
Image Processing

## III. Depth to Obstacle Avoidance (TODO)
### i. Deep Learning
#### A. Dataset
#### a. [NYU Dataset V1](https://cs.nyu.edu/~silberman/datasets/nyu_depth_v1.html), [Paper](https://cs.nyu.edu/~silberman/papers/indoor_seg_struct_light.pdf)
#### b. [NYU Dataset V2](https://cs.nyu.edu/~silberman/datasets/nyu_depth_v2.html), [Paper](https://cs.nyu.edu/~silberman/papers/indoor_seg_support.pdf)
#### How to read NYU mat file with python [Korean Blog](https://ddokkddokk.tistory.com/21)
#### Packages [scikit-image](http://scikit-image.org/docs/dev/install.html) [matplotlib](https://matplotlib.org/users/installing.html)
```
> pip install scikit-image
> python -m pip install -U matplotlib
```

#### Change Code for Windows/OS X [Github issue](https://github.com/scikit-image/scikit-image/issues/2595)
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

#### c. RGBD Dataset [Reference](http://www.open3d.org/docs/tutorial/Basic/rgbd_images/index.html#)

#### B. Model
#### a. FCRN [Paper (arXiv)](https://arxiv.org/abs/1606.00373), [Github](https://github.com/iro-cp/FCRN-DepthPrediction)

## IV. Optical Character Recognition to Path Planning (TODO)
### i. Deep Learning
#### a. Tesseract [Github](https://github.com/tesseract-ocr/tesseract), [Demo](http://tesseract.projectnaptha.com/)
#### Python Version - pytesseract [Github](https://github.com/madmaze/pytesseract), [pip](https://pypi.org/project/pytesseract/)
```
> pip install pytesseract
```
#### Install Windows Version [Github](https://github.com/tesseract-ocr/tesseract/wiki#windows), [Download](https://github.com/UB-Mannheim/tesseract/wiki) 
#### Training [Github](https://github.com/tesseract-ocr/tesseract/wiki/TrainingTesseract-4.00)
#### Korean Ubuntu [Blog](https://webnautes.tistory.com/947)
#### Korean [Korean Blog](https://m.blog.naver.com/samsjang/220694855018)
#### 공백 제거 [Korean Blog](https://hashcode.co.kr/questions/692/%EC%8A%A4%ED%8A%B8%EB%A7%81%EC%97%90-%EB%AA%A8%EB%93%A0-%EA%B3%B5%EB%B0%B1-%EB%AC%B8%EC%9E%90%EB%A5%BC-%EC%A0%9C%EA%B1%B0%ED%95%98%EA%B3%A0-%EC%8B%B6%EC%9D%80%EB%8D%B0-%EC%95%9E-%EB%92%A4-%EA%B3%B5%EB%B0%B1%EB%A7%8C-%EC%A0%9C%EA%B1%B0%EB%90%A9%EB%8B%88%EB%8B%A4)
##### 한번 경로 변경 등을 하면 Pycharm을 끄고 재시작 해야 됨
#### 특수 문자 제거 [Korean Blog](https://niceman.tistory.com/156)
