# Unzip Multiple Zip files

## Date

2023-04-27-Thursday.

## Environment

macOS 13.3.1

## Unzip

```Bash
file.zip file.z01 file.z02 file.z03
```

### 1. Make One Zip File

```Bash
zip -FF {zips_name} --out {combined_zip_file_name.zip}
# zip -FF file.zip --out output.zip
```

### 2. Unzip the Zip File

```Bash
unzip -qt {combined_zip_file_name.zip}
# unzip -qt output.zip
```

---

### Reference
- Unzip Multiple Files Blog KR, https://dbjina.tistory.com/53, 2023-04-27-Thu.
