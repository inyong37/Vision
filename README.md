# Vision Processing
OpenCV & Python & TensorFlow & Keras

## I. Dehazing to Object Detection (Human & Fire) (TODO)

### i. Image Processing with OpenCV

#### Human detection with RPi [Github](https://github.com/OmalPerera/Human-detection-system-with-raspberry-Pi/blob/master/pi_surveillance.py)
#### HOG detectMultiScale [Korean](http://hamait.tistory.com/509), [English](https://www.pyimagesearch.com/2015/11/16/hog-detectmultiscale-parameters-explained/)
#### Dark Channel Prior [Github](https://github.com/anhenghuang/dehaze), [Paper](http://www.robots.ox.ac.uk/~vgg/rg/papers/hazeremoval.pdf)

### ii. Deep Learning

#### A. Dataset [Reference](https://www.researchgate.net/post/Is_there_exists_any_haze_fog_dust_smog_removal_images_data-set_with_ground_truth_images)

#### a. [RESIDE: V0 (REalistic Single Image DEhazing)](https://sites.google.com/view/reside-dehaze-datasets/reside-v0), [Paper (arXiv)](https://arxiv.org/pdf/1712.04143.pdf), [Paper (IEEE)](https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=8451944)
#### b. [I-Haze](http://www.vision.ee.ethz.ch/ntire18/i-haze/), [Paper (arXiv)](https://arxiv.org/abs/1804.05091)
#### c. [D-Hazy(X)](http://www.meo.etc.upt.ro/AncutiProjectPages/D_Hazzy_ICIP2016/), [Paper (IEEE)](https://ieeexplore.ieee.org/document/7532754)
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

### i. Tesseract [Github](https://github.com/tesseract-ocr/tesseract), [Demo](http://tesseract.projectnaptha.com/)

#### A. pytesseract [Github](https://github.com/madmaze/pytesseract), [pip](https://pypi.org/project/pytesseract/)
```
> pip install pytesseract
```

#### B. Install Windows Version [Github](https://github.com/tesseract-ocr/tesseract/wiki#windows), [Download](https://github.com/UB-Mannheim/tesseract/wiki) 
#### Tesseract training [Github](https://github.com/tesseract-ocr/tesseract/wiki/TrainingTesseract-4.00)
##### Variable-size Graph Specification Language (VGSL) [Github](https://github.com/tesseract-ocr/tesseract/wiki/VGSLSpecs)
##### StreetView Tensorflow Recurrent End-to-End Transcription (STREET) [Github](https://github.com/tensorflow/models/tree/master/research/street)
#### OCR Korean [Korean Blog](https://m.blog.naver.com/samsjang/220694855018)
#### Remove spaces [Korean Blog](https://hashcode.co.kr/questions/692/%EC%8A%A4%ED%8A%B8%EB%A7%81%EC%97%90-%EB%AA%A8%EB%93%A0-%EA%B3%B5%EB%B0%B1-%EB%AC%B8%EC%9E%90%EB%A5%BC-%EC%A0%9C%EA%B1%B0%ED%95%98%EA%B3%A0-%EC%8B%B6%EC%9D%80%EB%8D%B0-%EC%95%9E-%EB%92%A4-%EA%B3%B5%EB%B0%B1%EB%A7%8C-%EC%A0%9C%EA%B1%B0%EB%90%A9%EB%8B%88%EB%8B%A4)
#### Once you change the route, you need to turn off and restart Pycharm.
#### Remove special characters [Korean Blog](https://niceman.tistory.com/156)
#### Tesseract Optimal conditions [Korean Blog](https://creaby.tistory.com/17)
#### Color Reversal [Korean Blog](https://076923.github.io/posts/Python-opencv-11/)
```
image = cv2.bitwise_not(input_image)
```
#### Resize [Korean Blog](https://076923.github.io/posts/Python-opencv-8/)
```
image = cv2.resize(input_image, dsize=(0, 0), fx=0.3, fy=0.7, interpolation=cv2.INTER_LINEAR)
```

### Korean Scene Text Recognition by Character-level
#### dataset version 1 (.pkl) [download]()
|<center>Dataset</center>|<center>Language</center>|# of fonts|# of characters|total # of images|
|----------|----------|----------:|----------:|----------:|
|<center>PHD08</center>|<center>Korean</center>|9|2,350|5,139,450|
|<center>EMNIST (ByClass)</center>|<center>Number & English</center>|Hand Writing|62|814,255|

#### dataset version 2 (.png) [download](https://drive.google.com/file/d/1zmSysfB6BLwBfTDCh84coSxEhEqq2Ung/view?usp=sharing)
|<center>Language</center>|# of fonts|# of characters|total # of images|
|----------|----------:|----------:|----------:|
|<center>Korean</center>|70|11,172|782,040|
|<center>Number</center>|70|10|700|
|<center>English</center>|70|52 (upper 26, lower 26)|3,640|

#### dataset version 3 (.png) [download](https://drive.google.com/file/d/1mAXFEmYup06cBFohwEprvt1gLIRkCA7R/view?usp=sharing)
|<center>Language</center>|# of fonts|# of characters|total # of images|
|----------|----------:|----------:|----------:|
|<center>Korean</center>|69|972|58,320|
|<center>Number</center>|69|10|690|
|<center>English</center>|69|52 (upper 26, lower 26)|3,588|
----------------------------------------------------------------------------------------------------
## Install
### i.    [Install OpenCV on Computer](https://github.com/inyong37/Vision/blob/master/Install/OpenCV-Computer.md)
### ii.   [Install OpenCV on Raspberry Pi](https://github.com/inyong37/Vision/blob/master/Install/OpenCV-RaspberryPi.md)
### iii.  [Install TensorFlow CPU on Computer](https://github.com/inyong37/Vision/blob/master/Install/TensorFlow-Computer-CPU.md)
### iv.   [Install TensorFlow GPU on Computer](https://github.com/inyong37/Vision/blob/master/Install/TensorFlow-Computer-GPU.md)
### v.    [Install & Uninstall TensorFlow on Raspberry Pi](https://github.com/inyong37/Vision/blob/master/Install/TensorFlow-RaspberryPi.md)
### vi.   [Install Keras](https://github.com/inyong37/Vision/blob/master/Install/Keras.md)
### vii.  [Install Keras Reinforcement Learning](https://github.com/inyong37/Vision/blob/master/Install/Keras-ReinforcementLearning.md)
### viii. [Install Pytorch](https://github.com/inyong37/Vision/blob/master/Install/Pytorch.md)
### ix. [Install Theano](https://github.com/inyong37/Vision/blob/master/Install/Theano.md)
### x. [Virtual Environment with Conda](https://github.com/inyong37/Vision/blob/master/Install/Virtual-Environment_conda.md)
