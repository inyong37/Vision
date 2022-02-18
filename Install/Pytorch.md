# I. Install Pytorch

## i. Installing on Windows.
### A. Windows & Conda & CPU
```
conda install pytorch-cpu torchvision-cpu -c pytorch
```

### B. Windows & Conda & CUDA 9.0
```
conda install pytorch torchvision cudatoolkit=9.0 -c pytorch
```

### C. Windows & pip & Python 3.6 & CUDA 9.0
```
pip3 install https://download.pytorch.org/whl/cu90/torch-1.1.0-cp36-cp36m-win_amd64.whl
pip3 install torchvision
```

## ii. Verify
[tensor_tutorial.py](https://pytorch.org/tutorials/_downloads/092fba3c36cb2ab226bfdaa78248b310/tensor_tutorial.py)

## iii. Tutorial
[Tutorial](https://pytorch.org/tutorials/)

## iv. Version Check

### iA. CUDA
```
nvcc --version
```

### B. Python
```
python --version
```

----------
#### Reference
- PyTorch, https://pytorch.org/, 2019-03-25-Mon.
- Get Started PyTorch, https://pytorch.org/get-started/locally/, 2022-02-18-Fri.
