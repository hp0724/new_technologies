import pickle
import os
from mayavi import mlab
import torch
import utils as V
from tqdm import tqdm

#Apply the desired number in the range
for i in range(0, 1):
    data_dir = 'data_dict/data_dict%06d.pkl' % i
    pred_dir = 'pred_dict/pred_dict%06d.pkl' % i
    # 피클 파일 로드
    with open(data_dir, 'rb') as f:
        data_dict = pickle.load(f)

    with open(pred_dir, 'rb') as f:
        pred_dicts = pickle.load(f)

    print('{0:06d} Open Success'.format(i))
    # 예시: Open3D를 사용한 시각화
    if len(data_dict) > 0:
        mlab.options.offscreen = True
        # Open3D를 사용한 시각화
        V.draw_scenes(
            points=data_dict['points'][:, 1:], ref_boxes=pred_dicts[0]['pred_boxes'],
            ref_scores=pred_dicts[0]['pred_scores'], ref_labels=pred_dicts[0]['pred_labels']
        )
        result_dir = 'image/result%06d.png' % i
        mlab.savefig(result_dir)
        print('{0:06d} Finish'.format(i))
