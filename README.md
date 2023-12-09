## framework

![Untitled (4)](https://github.com/hp0724/new_technologies/assets/75898031/5add9ca5-b0e1-4de7-bc5a-35061a009870)


## [AI-Hub](https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&dataSetSn=71623)
**Download data needed for the project from AI HUB**
![Untitled (5)](https://github.com/hp0724/new_technologies/assets/75898031/f826304a-ded5-43d6-a5a6-7d98d7f417f6)





## openPCdet
**OpenPCDet is a clear and simple standalone open source project for LiDAR-based 3D object detection.**
![Untitled (6)](https://github.com/hp0724/new_technologies/assets/75898031/b87886ac-b610-40b2-94f8-d94616825bbc)


**Clone OpenPCdet through git.**

![Untitled (7)](https://github.com/hp0724/new_technologies/assets/75898031/f45f47a6-39fb-4adb-bd4f-018a0983042a)


### Spconv
**Install spconv for your cuda version**
![Untitled (8)](https://github.com/hp0724/new_technologies/assets/75898031/eb52aedc-f633-4f82-97f1-757cd951158a)

### Required Module

**Run on the terminal**

**mayavi**
```jsx
pip install mayavi
```

**torch**
```jsx
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```
*Install Torch Version according to your nvidia driver*

**tqdm**
```jsx
pip install tqdm
```
**spconv**
```jsx
pip install spconv-cu113
```
**pypcd**
```jsx
pip install pypcd
```
**cv2**
```jsx
pip install opencv-python



## Run OpenPCDet setup.py

```jsx
!python3 setup.py develop
```


### Run nuscenes_models cbgs_voxel0075_res3d_centerpoint

```jsx
!python demo.py --cfg_file cfgs/nuscenes_models/cbgs_voxel0075_res3d_centerpoint.yaml --ckpt cfgs/nuscenes_models/cbgs_voxel0075_centerpoint_nds_6648.pth --data_path ../data/openData/training/file_name_000000.bin
```

## Visualization in local

**This is an issue that cannot be visualized in colab, so it is visualized locally.**
**using picle file for visulization**

### Driving Environment

**On python 3.9**   
**Using PyCharm Community Edition**

### Required Module

**Run on the terminal**

**mayavi**
```jsx
pip install mayavi
```

**torch**
```jsx
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```
*Install Torch Version according to your nvidia driver*

**tqdm**
```jsx
pip install tqdm
```
**spconv**
```jsx
pip install spconv-cu113
```
**pypcd**
```jsx
pip install pypcd
```
**cv2**
```jsx
pip install opencv-python
```
### Setting
**1. In lib\pypcd\__init__.py, modify this**
```jsx
from pypcd import * -> from .pypcd import *
```
**2. In lib\pypcd\pypcd.py, change to file that provided**

### main.py
**Code that converts pkl files generated from SWTermProject.ipynb file into predicted images**

***Note***  
data_dir, pred_dir path needs to be changed to path with pkl file   
result_dir path needs to be changed to the location where the image will be stored
### utils.py
**Request to create an image at main.py and the file will convert it to an image**

### pcd_To_Bin.py
**Convert pcd file with bin file (field value x,y,z,intensity required)**

***How to use***
```jsx
python pcd_To_Bin.py --pcd_path [pcd_path] --bin_path [bin_path]
```
### video.py
**Play the saved predicted images in video format**
