# Split a file

## Date

2023-08-23-Wednesday.

## Environment

Ubuntu 20.4.6 LTS

## Split a File

```bash
split -b {split_by_size} {file} {prefix include path} -a {number_of_postfix}
split -l {split_by_line} {file} {prefix include path} -a {number_of_postfix}
split -b 10K file dir/splitted_ -a 3
```

---

### Reference
- Split Blog KR, https://jhnyang.tistory.com/209, 2023-08-23-Wed.
