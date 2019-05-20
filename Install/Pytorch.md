# I. Install Pytorch

Reference: https://pytorch.org/

### i-A. Windows & Conda & Python=3.6 & CUDA=None
```
conda install pytorch-cpu torchvision-cpu -c pytorch
```

### i-B. Windows & Conda & Python=3.6 & CUDA=9.0
```
conda install pytorch torchvision cudatoolkit=9.0 -c pytorch
```

### i-C. Stable (1.1) & Windows & Pip & Python 3.6 & CUDA 9.0
```
pip3 install https://download.pytorch.org/whl/cu90/torch-1.1.0-cp36-cp36m-win_amd64.whl
pip3 install torchvision
```

### ii. Verify
[tensor_tutorial.py](https://pytorch.org/tutorials/_downloads/092fba3c36cb2ab226bfdaa78248b310/tensor_tutorial.py)

### iii. Tutorial
[Tutorial](https://pytorch.org/tutorials/)

### iv. Version Check

### iv-A. CUDA
```
nvcc --version
```

### iv-B. Python
```
python --version
```
