## Install TensorFlow GPU Version on Computer

### A. CUDA and cuDNN

### 1. Install CUDA
호환되는 tensorflow-gpu, Python, CUDA, cuDNN 확인하기

Windows: https://www.tensorflow.org/install/source_windows?hl=ko

Linux/Mac OS: https://www.tensorflow.org/install/source?hl=ko

Raspberry Pi: https://www.tensorflow.org/install/source_rpi?hl=ko

### 1-1. Install CUDA 9.0
https://developer.nvidia.com/cuda-90-download-archive 에서 자신의 환경에 맞는 CUDA download

예시 환경
```
Opertaing System : Windows
Architecture     : x86_64
Version          : 10
Installer Type   : exe (local)
```
위 예시 환경일 경우의 다운로드 링크
https://developer.nvidia.com/compute/cuda/9.0/Prod/local_installers/cuda_9.0.176_win10-exe

### 1-2. Install CUDA 10.0 (2019-09-27-Fri 기준 pip install tensorflow-gpu는 cuda10.dll 필요 https://www.tensorflow.org/install/gpu)
https://developer.nvidia.com/cuda-10.0-download-archive 에서 자신의 환경에 맞는 CUDA download

예시 환경
```
Opertaing System : Windows
Architecture     : x86_64
Version          : 10
Installer Type   : exe (local)
```
위 예시 환경일 경우의 다운로드 링크
https://developer.nvidia.com/compute/cuda/10.0/Prod/local_installers/cuda_10.0.130_411.31_win10

### 2. exe 파일 실행으로 설치

### 3. Download cuDNN
Reference: https://developer.nvidia.com/cudnn

아이디가 있다면 Login, 없다면 Join 후 Login

the Terms of the cuDNN Software License Agreement 에 동의 후 자신의 환경에 맞는 cuDNN download

다운로드한 cuDNN 파일은 unzip 한 후 파일들을 복사 또는 잘라내기 후
```
C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\9.0
```
위 디렉토리에 붙여넣기

### B. Install TensorFlow GPU With Anaconda
Reference: https://www.tensorflow.org/install/gpu

### 1. Create Virtual Environment
cmd 또는 anaconda prompt 를 실행한다.
```
> conda create -n tensorflow python=3.6 anaconda
```
위 'tensorflow' 는 가상환경의 이름이다.

### 2. Verify Virtual Environmnet
```
> conda info --envs
```

### 3. Install TensorFlow
가상환경 'tensorflow 를 activate 한다.
```
> activate tensorflow
> pip install tensorflow-gpu
```

### 4. Verify Install
```
> python -c "import tensorflow as tf; tf.enable_eager_execution(); print(tf.reduce_sum(tf.random_normal([1000, 1000])))"
```

### 5. Pycharm Interpreter Setting
```
File>Settings
Project:PyCharmProjects>Project Interpreter
```
톱니를 클릭하고 add 를 클릭한다.
```
System Interpreter>Interpreter>
```
가상환경 directory 에 있는 python.exe 를 선택한다.
