## Install TensorFlow on Raspberry Pi

### 1. Download TensorFlow
```
$ git clone https://github.com/tensorflow/tensorflow.git
$ cd tensorflow
```

### 2-A. Python 3 Version
```
$ CI_DOCKER_EXTRA_PARAMS="-e CI_BUILD_PYTHON=python3 -e CROSSTOOL_PYTHON_INCLUDE_PATH=/usr/include/python3.4" \
    tensorflow/tools/ci_build/ci_build.sh PI-PYTHON3 \
    tensorflow/tools/ci_build/pi/build_raspberry_pi.sh
```

### 2-B. Python 2.7 Version
```
$ tensorflow/tools/ci_build/ci_build.sh PI \
    tensorflow/tools/ci_build/pi/build_raspberry_pi.sh
```

### 3.Build
```
$ tensorflow/tools/ci_build/ci_build.sh PI \
    tensorflow/tools/ci_build/pi/build_raspberry_pi.sh PI_ONE
```

### 4. Install
```
$ pip install tensorflow-version-cp34-none-linux_armv7l.whl
```
Choose own 'version'
