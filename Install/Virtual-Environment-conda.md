# Virtual Environment with conda

## I. Create Virtual Environment with conda

### i. Basic
```
> conda create -n envs
```
'envs' is virtual environment name

### ii. Python Version
```
> conda create -n envs python=2.7
```

### iii. Specific Package 
```
> conda create -n envs python=2.7 anaconda
```

### iv. Specific Directory/Path
```
> conda create --prefix C:\Users\Inyong\Python\Anaconda\conda\conda\envs\py36 python=3.6 anaconda
```

### Summary
```
$ conda create -n enve python=3.9 anaconda
```

## II. Activate Virtual Environment

### i. Basic
```bash
> activate envs # Windows
$ conda activate envs # macOS
```

### ii. Specific Directory/Path
```
> activate  C:\Users\Inyong\Python\Anaconda\conda\conda\envs\py36
```

## III. Remove Virtual Environment with conda

### i. Basic
```
> conda env remove -n envs
```
'envs' is the name of virtual environment

### ii. Specific Directory/Path
```
> conda env remove -n  C:\Users\Inyong\Python\Anaconda\conda\conda\envs\py36
```

## IV. Conda Commands

##### Show installed packages
```
conda list
```
##### Check Python
```
> python --version
```
##### Search Python
```
> conda serach python
```
##### Change Python
```
> conda install python=3.5
```
##### Show virtual environments
```
> conda info --env
```
