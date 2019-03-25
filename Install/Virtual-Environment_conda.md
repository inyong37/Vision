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

## II. Activate Virtual Environment

### i. Basic
```
> activate envs
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

#### Show installed packages
```
conda list
```
