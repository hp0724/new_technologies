![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/71004678-6d47-4f4f-ac74-6732bdc95686/85f2613a-53f8-4842-91c9-edd544528b93/Untitled.png)

**framework**

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/71004678-6d47-4f4f-ac74-6732bdc95686/518f4643-7033-4388-a424-8d81fa5ab19a/Untitled.png)

[AI-Hub](https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&dataSetSn=71623)

**Download data needed for the project from AI HUB**

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/71004678-6d47-4f4f-ac74-6732bdc95686/d822a9c1-664b-49b7-8c0b-79889c98350d/Untitled.png)

**Download the modules required for execution.**

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/71004678-6d47-4f4f-ac74-6732bdc95686/9b11f9ca-3ffd-4271-96cc-37f2ad9ba179/Untitled.png)

**OpenPCDet is a clear and simple standalone open source project for LiDAR-based 3D object detection.**

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/71004678-6d47-4f4f-ac74-6732bdc95686/46dd28f1-8dfe-4263-9702-b5a524a70013/Untitled.png)

**Clone OpenPCdet through git.**

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/71004678-6d47-4f4f-ac74-6732bdc95686/d44d7cfe-2b6e-40a4-878d-78ce92f03ebd/Untitled.png)

**Install spconv for your cuda version**

```jsx
!python3 setup.py develop
```

**Run OpenPCDet setup.py**

```jsx
!python demo.py --cfg_file cfgs/nuscenes_models/cbgs_voxel0075_res3d_centerpoint.yaml --ckpt cfgs/nuscenes_models/cbgs_voxel0075_centerpoint_nds_6648.pth --data_path ../data/openData/training/file_name_000000.bin
```

**Run nuscenes_models cbgs_voxel0075_res3d_centerpoint** 

**This is an issue that cannot be visualized in colab, so it is visualized locally.**

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

**Visualization using pickles saved in colab**
