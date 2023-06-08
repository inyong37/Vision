# [Unzip the compression file](https://codechacha.com/ko/linux-tar/#6-tarbz2-%EC%95%95%EC%B6%95-%ED%95%B4%EC%A0%9C)

## Date

2023-02-22-Wednesday.

2023-05-31-Wednesday.

## Environment

- Debian GNU/Linux 11 (bullseye)
- Ubuntu 20.04.4 LTS

## tar

### Unzip `tar.bz2`

Current directory:

```Bash
tar -jxvf {file_name}
```

Specific directory:

```Bash
tar -zxvf {file_name} -C {output_directory}
```

## gz

### Compress gz

```Bash
gzip {file_name} # gzip foo.jpg
```

### Extract a gz file

```Bash
gzip -d {gz_file_name} # gzip -d bar.gz
```

### Extract Multiple gz files

```Bash
gzip -d *.gz
```

---

### Reference
- Unzip Blog KR, https://codechacha.com/ko/linux-tar/#6-tarbz2-%EC%95%95%EC%B6%95-%ED%95%B4%EC%A0%9C, 2023-02-22-Wed.
- Extract Multiple zip gz Files Blog KR, https://sexydatadesigner.tistory.com/108, 2023-05-31-Wed.
- Compress and Extract gz Files Blog KR, https://araikuma.tistory.com/121, 2023-05-31-Wed.
