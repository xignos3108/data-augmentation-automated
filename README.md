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
```shell script
    pip install -U albumentations
```
### Run main.py
```shell script
    python ./main.py
```
### Choose transforms and build augmentation pipline with your needs
Pipline configuration exists in transformation.py

# Bugs
Error occurs with 'A(ooo5).txt', 'E(0028).txt', 'I(0010).txt'.
Remove those files before running the code.


  
