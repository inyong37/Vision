## Install TensorFlow CPU Version on Computer

### A. With Anaconda
Reference: https://www.tensorflow.org/install/pip

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
> pip install --upgrade tensorflow
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
