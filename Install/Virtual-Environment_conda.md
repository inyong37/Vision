# 1. Create Virtual Environment with conda

### Basic
```
> conda create -n envs
```
'envs' is virtual environment name

### Python Version
```
> conda create -n envs python=2.7
```

### Specific Package 
```
> conda create -n envs python=2.7 anaconda
```

### Specific Directory/Path
```
> conda create --prefix C:\Python\Anaconda\conda\conda\envs\tensorflow python=3.6 anaconda
```

# 2. Activate Virtual Environment

### Basic
```
> activate envs
```

### Specific Directory/Path
```
> activate  C:\Users\Inyong\Python\Anaconda\conda\conda\envs\py36
```

# 3. Remove Virtual Environment with conda

### Basic
```
> conda env remove -n envs
```
'envs' is the name of virtual environment

### Specific Directory/Path
'''
> conda env remove -n  C:\Users\Inyong\Python\Anaconda\conda\conda\envs\py36
```
