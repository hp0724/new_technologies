# Getting Start
## 1. Install public data
LINK : https://www.aihub.or.kr/

![Untitled (5)](https://github.com/hp0724/new_technologies/assets/75898031/f826304a-ded5-43d6-a5a6-7d98d7f417f6)
Download the data for the project from AIHUB and use it for the project

For our project, we used 3D data for transportation logistics and data types by sector


## 2. Convert pcd file to bin file
Covert pcd file to bin file 

field value required, **[x, y, z, intensity]**

**How to use**
```jsx
python pcd_To_Bin.py --pcd_path [pcd_path] --bin_path [bin_path]
```
## 3. openPCDet, in colab, get pkl data

Run this file, [SWTermProject.ipynb](SWTermProject.ipynb)

**NOTE**    
After uploading the previously converted bin files to the collab environment, the location of the **bin file** must be set.

```jsx
!python demo.py --cfg_file ... --data_path "HERE"
```
**Like this**
```jsx
!python demo.py --cfg_file cfgs/nuscenes_models/cbgs_voxel0075_res3d_centerpoint.yaml --ckpt cfgs/nuscenes_models/cbgs_voxel0075_centerpoint_nds_6648.pth --data_path ../data/openData/training/file_name_000000.bin
```

## 4. Visualization in Local
***This is an issue that cannot be visualized in colab, so it is visualized locally.***     
***Using pickle file for visualization***

### 4.1 Environment
**Python 3.9**  
**PyCharm Community Edition**
### 4.2 Required Module
***Install modules in Pycharm Terminal***

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

### 4.3 Setting
**1. In lib\pypcd\__init__.py, modify this**
```jsx
from pypcd import * -> from .pypcd import *
```
**2. In lib\pypcd\pypcd.py, change to file that provided**

### 4.4 How to Use
**4.4.1 run visualization.py**

***Note***  
*data_dir, pred_dir path needs to be changed to path with pkl file*     
*result_dir path needs to be changed to the location where the image will be stored*

**4.4.2 run video.py**

***Note***  
*Set image path to the path where the image is stored*
