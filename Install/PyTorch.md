# Installing PyTorch

### I. Activate target virtual environment
```
activate {env_name}
```

### Install PyTorch
#### A. Install CPU version of PyTorch *recommend to install LTS version*
*On Windows & Linux w. Conda*
```
conda install pytorch torchvision torchaudio cpuonly -c pytorch-lts
```

*macOS is not currently supported for lts*

*On Windows w. Pip*
```cmd
> pip3 install torch==1.8.2+cpu torchvision==0.9.2+cpu torchaudio===0.8.2 -f https://download.pytorch.org/whl/lts/1.8/torch_lts.html
```

*On Linux w. Pip*
```bash
$ pip3 install torch==1.8.2+cpu torchvision==0.9.2+cpu torchaudio==0.8.2 -f https://download.pytorch.org/whl/lts/1.8/torch_lts.html
```

*macOS is not currently supported for lts*

*~~On Windows & Linux w. conda~~* (deprecated)
```
conda install pytorch-cpu torchvision-cpu -c pytorch
```

#### B. Install GPU version of PyTorch :point_right: [check CUDA version](https://github.com/inyong37/Vision/blob/master/Install/PyTorch.md#a-cuda)
*CUDA 10.2 on Windows & Linux w. Conda*
```
conda install pytorch torchvision torchaudio cudatoolkit=10.2 -c pytorch
```
*CUDA 11.3 on Windows & Linux w. Conda*
```
conda install pytorch torchvision torchaudio cudatoolkit=11.3 -c pytorch
```

*CUDA 10.2 on Windows w. Pip*
```cmd
> pip3 install torch==1.10.2+cpu torchvision==0.11.3+cpu torchaudio==0.10.2+cpu -f https://download.pytorch.org/whl/cpu/torch_stable.html
```

*CUDA 10.2 on Linux w. Pip*
```bash
$ pip3 install torch torchvision torchaudio
```

*CUDA 11.3 on Windows w. Pip*
```cmd
> pip3 install torch==1.10.2+cu113 torchvision==0.11.3+cu113 torchaudio===0.10.2+cu113 -f https://download.pytorch.org/whl/cu113/torch_stable.html
```

*CUDA 11.3 on Linux w. Pip*
```bash
$ pip3 install torch==1.10.2+cu113 torchvision==0.11.3+cu113 torchaudio==0.10.2+cu113 -f https://download.pytorch.org/whl/cu113/torch_stable.html
```

#### ~~Install CUDA 9.0 version of PyTorch using Conda~~ 
```
conda install pytorch torchvision cudatoolkit=9.0 -c pytorch
```

#### ~~Windows & pip & Python 3.6 & CUDA 9.0 :point_right: [check Python version](https://github.com/inyong37/Vision/blob/master/Install/PyTorch.md#b-python)~~
```
pip3 install https://download.pytorch.org/whl/cu90/torch-1.1.0-cp36-cp36m-win_amd64.whl
pip3 install torchvision
```

## II. Verify
:point_right: [tensor_tutorial.py](https://pytorch.org/tutorials/_downloads/092fba3c36cb2ab226bfdaa78248b310/tensor_tutorial.py)

## III. Tutorial
:point_right: [Tutorial](https://pytorch.org/tutorials/)

----------

# Checking the version
### A. CUDA
```
nvcc --version
```

### B. Python
```
python --version
```

# Uninstalling PyTorch
Recommend to using the Pip
```
pip uninstall pytorch torchaudio torchvision
```

----------

#### Reference
- PyTorch, https://pytorch.org/, 2019-03-25-Mon.
- Get Started PyTorch, https://pytorch.org/get-started/locally/, 2022-02-18-Fri.
