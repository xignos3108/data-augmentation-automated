# data-augmentation-automated
Albumentation based automated data augmentation system

# Contributor
ILKYU YI

# How to Use
### Download custom dataset(.jpg) and label file(.txt)
1. Dataset and label should exist in same folder.
2. Folder should be named as 'dataset'
3. 'dataset' folder should be located in your main directory with other .py files

### Install albumentation library and dependencies
#### Install the latest stable version from PyPI
```shell script
    pip install -U albumentations  
```
#### Install the latest version from the master branch on GitHub
```shell script
    pip install -U git+https://github.com/albumentations-team/albumentations 
```
#### Force Albumentations to use dependencies
```shell script
    pip install -U albumentations --no-binary qudida,albumentations
```
#### Install from conda-forge
```shell script
    conda install -c conda-forge imgaug
    conda install -c conda-forge albumentations
```

### Run main.py
```shell script
    python ./main.py
```
Or just press run from main.py

### Choose transforms and build augmentation pipline with your needs
Pipline configuration exists in configs.py

# Bugs
Error occurs with 'A(0005).txt', 'E(0028).txt', 'I(0010).txt'.
Remove those files before running the code.

A(0005) -> 0 0.024609 0.373611 0.049219 0.019444 -> 0.024609

(-5.000000000005e-07, 0.363889, 0.0492185, 0.38333300000000003, '0')

E(0028) -> 4 0.002734 0.859722 0.005469 0.016667 -> 0.002734

(-5.000000000000664e-07, 0.8513885, 0.005468499999999999, 0.8680555, '4')

I(0010) -> 8 0.018359 0.525694 0.036719 0.056944 -> 0.018359

(-5.000000000000664e-07, 0.8513885, 0.005468499999999999, 0.8680555, '4')

### Bug fixed 

1.Bbox coordinate causing error are set to be ignored in tf process (21/12/14)

2.Causing empty labels fixed (21/12/15)
