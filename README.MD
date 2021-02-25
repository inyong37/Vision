# Vision
Computuer Vision and Image Processing with Python, OpenCV, and Keras.

----------

## :foggy: 1. Dehazing to Object Recognition :construction:
Human, and fire detection and recognition in indoor foggy environment.

### i. Image Processing with OpenCV
#### A. Dehazing
##### a. Dark Channel Prior | [GitHub](https://github.com/anhenghuang/dehaze) | [Paper](http://www.robots.ox.ac.uk/~vgg/rg/papers/hazeremoval.pdf)

#### B. Object Recognition
##### a. Human detection with RPi | [Github](https://github.com/OmalPerera/Human-detection-system-with-raspberry-Pi/blob/master/pi_surveillance.py)
##### b. HOG detectMultiScale | [Blog (KR)](http://hamait.tistory.com/509) | [Blog (US)](https://www.pyimagesearch.com/2015/11/16/hog-detectmultiscale-parameters-explained/)

### ii. Image Processing with Deep Learning
#### :books: A. Dataset | [Reference](https://www.researchgate.net/post/Is_there_exists_any_haze_fog_dust_smog_removal_images_data-set_with_ground_truth_images)
##### a. RESIDE: V0 (REalistic Single Image DEhazing) | [Homepage](https://sites.google.com/view/reside-dehaze-datasets/reside-v0) | [Paper (IEEE)](https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=8451944) | [Paper (arXiv)](https://arxiv.org/pdf/1712.04143.pdf)
##### b. I-HAZE | [Homepage](http://www.vision.ee.ethz.ch/ntire18/i-haze/) | [Paper (arXiv)](https://arxiv.org/abs/1804.05091)
##### c. D-HAZY | [Homepage](http://www.meo.etc.upt.ro/AncutiProjectPages/D_Hazzy_ICIP2016/) | [Paper (IEEE)](https://ieeexplore.ieee.org/document/7532754)
##### d. O-HAZE | [Paper (arXiv)](https://arxiv.org/abs/1804.05101)

### :checkered_flag: iii. Challenge
#### A. NTIRE2018 | [Homepage](http://www.vision.ee.ethz.ch/ntire18/)

----------

## :dart: 2. Vanishing Point to Control Posture :heavy_check_mark:
Using Image Processing with OpenCV

----------

## 3. Depth to Obstacle Avoidance :construction:
### i. Image Processing with Deep Learning
#### :books: A. Dataset

##### a. NYU Dataset V1 | [Homepage](https://cs.nyu.edu/~silberman/datasets/nyu_depth_v1.html) | [Paper](https://cs.nyu.edu/~silberman/papers/indoor_seg_struct_light.pdf)
##### b. NYU Dataset V2 | [Homepage](https://cs.nyu.edu/~silberman/datasets/nyu_depth_v2.html) | [Paper](https://cs.nyu.edu/~silberman/papers/indoor_seg_support.pdf)

##### c. Sample Code for NYU
- How to read NYU mat file with python | [Blog (KR)](https://ddokkddokk.tistory.com/21)
  - Packages [scikit-image](http://scikit-image.org/docs/dev/install.html) [matplotlib](https://matplotlib.org/users/installing.html)
```cmd
> pip install scikit-image
> python -m pip install -U matplotlib
```

- Change Code for Windows or OS X | [GitHub issue](https://github.com/scikit-image/scikit-image/issues/2595)
```Python
import skimage.io as io
```
to 
```Python
import matplotlib
matplotlib.use('TkAgg')
from skimage import io
io.use_plugin('matplotlib')
```

##### c. RGBD Dataset | [Homepage](http://www.open3d.org/docs/tutorial/Basic/rgbd_images/index.html#)

#### B. Model
##### a. FCRN | [Paper (arXiv)](https://arxiv.org/abs/1606.00373) | [GitHub](https://github.com/iro-cp/FCRN-DepthPrediction)

----------

## 4. Optical Character Recognition to Path Planning :construction:
### i. Tesseract | [GitHub](https://github.com/tesseract-ocr/tesseract) | [Demo](http://tesseract.projectnaptha.com/)

### ii. PyTesseract | [GitHub](https://github.com/madmaze/pytesseract) | [Install with pip](https://pypi.org/project/pytesseract/)
```cmd
> pip install pytesseract
```

#### A. Install Windows Version | [GitHub](https://github.com/tesseract-ocr/tesseract/wiki#windows) | [Download](https://github.com/UB-Mannheim/tesseract/wiki)
#### B. Tesseract training | [GitHub](https://github.com/tesseract-ocr/tesseract/wiki/TrainingTesseract-4.00)
#### C. Variable-size Graph Specification Language (VGSL) | [GitHub](https://github.com/tesseract-ocr/tesseract/wiki/VGSLSpecs)
#### D. StreetView Tensorflow Recurrent End-to-End Transcription (STREET) | [GitHub](https://github.com/tensorflow/models/tree/master/research/street)
#### E. Korean OCR | [Blog (KR)](https://m.blog.naver.com/samsjang/220694855018)
- a. Remove spaces | [Blog (KR)](https://hashcode.co.kr/questions/692/%EC%8A%A4%ED%8A%B8%EB%A7%81%EC%97%90-%EB%AA%A8%EB%93%A0-%EA%B3%B5%EB%B0%B1-%EB%AC%B8%EC%9E%90%EB%A5%BC-%EC%A0%9C%EA%B1%B0%ED%95%98%EA%B3%A0-%EC%8B%B6%EC%9D%80%EB%8D%B0-%EC%95%9E-%EB%92%A4-%EA%B3%B5%EB%B0%B1%EB%A7%8C-%EC%A0%9C%EA%B1%B0%EB%90%A9%EB%8B%88%EB%8B%A4)
- b. Once you change the route, you need to turn off and restart Pycharm.
- c. Remove special characters | [Blog (KR)](https://niceman.tistory.com/156)
- d. Tesseract Optimal conditions | [Blog (KR)](https://creaby.tistory.com/17)
- e. Color Reversal | [Blog (KR)](https://076923.github.io/posts/Python-opencv-11/)
```Python
image = cv2.bitwise_not(input_image)
```
- f. Resize | [Blog (KR)](https://076923.github.io/posts/Python-opencv-8/)
```Python
image = cv2.resize(input_image, dsize=(0, 0), fx=0.3, fy=0.7, interpolation=cv2.INTER_LINEAR)
```

### :checkered_flag: iii. Challenge

#### A. Robust Reading Competition ICDAR | [Homepage](https://rrc.cvc.uab.es/)
Overview - ICDAR 2019 Robust Reading Challenge on Multi-lingual scene text detection and recognition | [Homepage](https://rrc.cvc.uab.es/?ch=15)

### iv. Korean STR
Korean Scene Text Recognition by Character-level

#### :books: A. Dataset
##### a. Dataset Version 1 (.png) | [MNIST.zip](https://drive.google.com/file/d/1c7dlim-q_G_6XMPkZOhMPA474EHmkdx7/view?usp=sharing) | [PHD08.zip](https://drive.google.com/file/d/1jrAc5lqw-Nd0zfxS5tiY1E-mL3skty_N/view?usp=sharing)

|<center>Dataset</center>|<center>Language</center>|# of fonts|# of characters|total # of images|
|----------|----------|----------:|----------:|----------:|
|<center>PHD08</center>|<center>Korean</center>|9|2,350|5,139,450|
|<center>EMNIST (ByClass)</center>|<center>Number & English</center>|Hand Writing|62|814,255|

##### b. Dataset Version 2 (.png) | [7z](https://drive.google.com/file/d/1zmSysfB6BLwBfTDCh84coSxEhEqq2Ung/view?usp=sharing)

|<center>Language</center>|# of fonts|# of characters|total # of images|
|----------|----------:|----------:|----------:|
|<center>Korean</center>|70|11,172|782,040|
|<center>Number</center>|70|10|700|
|<center>English</center>|70|52 (upper 26, lower 26)|3,640|

##### c. Dataset Version 3 (.png) | [7z](https://drive.google.com/file/d/1mAXFEmYup06cBFohwEprvt1gLIRkCA7R/view?usp=sharing) | [zip](https://drive.google.com/file/d/1XVv-L0oR-xAQjs22f0lL2wZDwyY0RnDv/view?usp=sharing)

|<center>Language</center>|# of fonts|# of characters|total # of images|
|----------|----------:|----------:|----------:|
|<center>Korean</center>|69|972|58,320|
|<center>Number</center>|69|10|690|
|<center>English</center>|69|52 (upper 26, lower 26)|3,588|

##### d. Dataset Version 4 (.png) | [7z](https://drive.google.com/file/d/1vQPIzj3Yuw4acuhzhdOV7c3z_ZQ5U0_q/view?usp=sharing) | [zip](https://drive.google.com/file/d/1wkYzcCbIYVmw2b4qdzDpQr0FBwVpMt78/view?usp=sharing) | [pkl](https://drive.google.com/file/d/1tHITLOsm3o27qUrz2CPUon1WTwhdFNGN/view?usp=sharing)

|<center>Language</center>|# of fonts|# of characters|total # of images|
|----------|----------:|----------:|----------:|
|<center>Korean</center>|69|972|116,640|
|<center>Number</center>|69|10|1,240|
|<center>English</center>|69|26|3,588|
- Korean and numbers use two font sizes.
- Incorporate uppercase letters into lowercase letters.
- Font sizes of Korean and number are 44, and 54, font size of English is 44.
- Image size is 64.
- Hangul characters refer to [this](https://drive.google.com/file/d/156bFGx1A4XjAvv5zSGpw5MkCckUx7LaB/view?usp=sharing) and calculated the frequency.

----------
## Install
### i.    [Install OpenCV on Computer](https://github.com/inyong37/Vision/blob/master/Install/OpenCV-Computer.md)
### ii.   [Install OpenCV on Raspberry Pi](https://github.com/inyong37/Vision/blob/master/Install/OpenCV-RaspberryPi.md)
### iii.  [Install TensorFlow CPU on Computer](https://github.com/inyong37/Vision/blob/master/Install/TensorFlow-Computer-CPU.md)
### iv.   [Install TensorFlow GPU on Computer](https://github.com/inyong37/Vision/blob/master/Install/TensorFlow-Computer-GPU.md)
### v.    [Install & Uninstall TensorFlow on Raspberry Pi](https://github.com/inyong37/Vision/blob/master/Install/TensorFlow-RaspberryPi.md)
### vi.   [Install Keras & Keras Reinforcement Learning](https://github.com/inyong37/Vision/blob/master/Install/Keras.md)
### vii. [Install Pytorch](https://github.com/inyong37/Vision/blob/master/Install/Pytorch.md)
### Viii. [Install Theano](https://github.com/inyong37/Vision/blob/master/Install/Theano.md)
### iX. [Virtual Environment with Conda](https://github.com/inyong37/Vision/blob/master/Install/Virtual-Environment-conda.md)
### X. [Setup Ubuntu](https://github.com/inyong37/Vision/blob/master/Install/Ubuntu.md)
----------
- Image Processing vs. Computer Vision [Reference](https://iskim3068.tistory.com/1)
- Dehazing - Image Processing/Object Recognition - Computer Vision
- Vanishing Point - Computer Vision
- Depth Prediction - Computer Vision
- Opitcal Character Recognition - Computer Vision
