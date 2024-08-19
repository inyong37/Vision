# Check Python Package

Install and Check the Python Package

Date: 2024-08-19-Mon.

## 1. `pip`

### A. `{package}`

```Bash
pip install {package}
```

### B. `{repository}`

```Bash
pip install git+https://$id:$password@{repository}
```

### C. `{repository}` with Extra

```Bash
pip install git+https://$id:$password@{repository}#egg={package}[extra]
```

## 2. `pip show {package}`

## 3. Check the Size

```Bash
du -sh {package_path}
du -h --max-depth=1 {package_path}
```
## 4. List the File Sizes

```Bash
du -ah --max-depth=3 | sort -rh | head -n 10
find . -type f -exec du -ah {} + | sort -rh | head -n 10
```
