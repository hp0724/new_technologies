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


### install module
**Download the modules required for execution.**
![Untitled (9)](https://github.com/hp0724/new_technologies/assets/75898031/8a8febe8-3ca7-4cfb-bee4-de23b960c66a)



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

```jsx
from visual_utils import visualize_utils as V
import pickle
import os
from mayavi import mlab
import torch

mlab.init_notebook()

for i in range(10):
    data_dir = 'data_dict/data_dict%06d.pkl' % i
    pred_dir = 'pred_dict/pred_dict%06d.pkl' % i
    print('{0:06d} Open Start'.format(i))
   
    with open(data_dir, 'rb') as f:
        data_dict = pickle.load(f)

    with open(pred_dir, 'rb') as f:
        pred_dicts = pickle.load(f)

    print('{0:06d} Open Success'.format(i))
    
    if len(data_dict) > 0:
        mlab.options.offscreen = True
       
        V.draw_scenes(
            points=data_dict['points'][:, 1:], ref_boxes=pred_dicts[0]['pred_boxes'],
            ref_scores=pred_dicts[0]['pred_scores'], ref_labels=pred_dicts[0]['pred_labels']
        )
        result_dir = 'image/result%06d.png' % i
        mlab.savefig(result_dir)
        print('{0:06d} Finish'.format(i))
```



