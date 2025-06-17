# HRNet-based Automated Landmark Detection For Human Hand Phenotyping


## Introduction
This is a tool for automated landmark detection of keypoints on both hands or a single hand. Pretrained model was used based on HRNetV2 (TPAMI'2019) framework with topdown heatmap and Dark (CVPR'2020) trained on Onehand10k datasets. Fine-tuning of the pretrained model was performed using our datasets of hand scanning images. The best model was deposited in the checkpoints folder.


## Citation
If you use our tool - automated landmarking for hand, please cite:

`Qian, W. et al., Hierarchical genetic architectures underlie hand morphology. (2025 submitted)`


## Installation
1. Prerequisites
   
`conda create --name openmmlab python=3.8 -y`

`conda activate openmmlab`

`conda install pytorch torchvision -c pytorch`

`pip install -U openmim`

`mim install mmengine`

`mim install "mmcv>=2.0.1"`

`pip install tensorboard`


2. install MMPose
	
`cd mmpose_hand`

`pip install -r requirements.txt`

`pip install -v -e .`


For more details, please check out the installation part of MMPose Documentation (https://mmpose.readthedocs.io/en/latest/installation.html).


## Datasets
Please prepare 256*256 images and json files (landmark position) for train, validation and test. Examples are deposited in the Toy_Sample folder.


## Demo
This is a demo for a toy test sample and visualization can be found in your work_dir folder.

	python demo/image_demo.py Toy_Sample/test/0081_H.jpg \

 	td-hm_hrnetv2-w18_dark-8xb64-210e_onehand10k-256x256.py \
 
 	checkpoints/best_model.pth --out-file work_dirs/vis_results.jpg --draw-heatmap --radius 2


The visualization result was deposited in work_dirs folder.

## Model training and testing
#### 1. Train on a GPU:

`python tools/train.py td-hm_hrnetv2-w18_dark-8xb64-210e_onehand10k-256x256.py [ARGS]`

e.g. 

	python tools/train.py td-hm_hrnetv2-w18_dark-8xb64-210e_onehand10k-256x256.py --word-dir ./work_dirs


#### 2. Train on multiple GPUs:

`bash ./tools/dist_train.sh td-hm_hrnetv2-w18_dark-8xb64-210e_onehand10k-256x256.py ${GPU_NUM} [ARGS]`



#### 3. Test the model:
Before run the script, add the path of testing files in the configure file.


`python tools/test.py td-hm_hrnetv2-w18_dark-8xb64-210e_onehand10k-256x256.py ${CHECKPOINT_FILE} [ARGS]`


e.g.

	python tools/test.py td-hm_hrnetv2-w18_dark-8xb64-210e_onehand10k-256x256.py \

	checkpoints/best_model.pth \
	
	--show-dir [SHOW_VISUAL_DIR] --dump [file_path.pkl]


## Visualization

`tensorboard --logdir ${WORK_DIR}/${TIMESTAMP}/vis_data`


For more arguments and descriptions, please check out the training and testing part of MMPose Document (https://mmpose.readthedocs.io/en/latest/user_guides/train_and_test.html)


