dataset_info = dict(
    dataset_name='hand_images_single',
    paper_info=dict(
        author='Wei Qian, Yongqing Bao, MMPose Contributors',
        title='Automated hand landmark detection using MMlab Pose Estimation toolbox',
        container='Shanghai Institute for Nutrition and Health, Chinese Academy of Sciences',
        year='2025',
        homepage='https://www.sinh.cas.cn',
    ),
    keypoint_info={
        0:
        dict(name='pinky_fingerR1', id=0, color=[255, 255, 255], type='', swap=''),
        1:
        dict(name='pinky_fingerR2', id=1, color=[255, 128, 0], type='', swap=''),
        2:
        dict(name='pinky_fingerR3', id=2, color=[255, 128, 0], type='', swap=''),
        3:
        dict(name='pinky_fingerR4', id=3, color=[255, 128, 0], type='', swap=''),
        4:
        dict(name='pinky_fingerR5', id=4, color=[255, 128, 0], type='', swap=''),
        5:
        dict(
            name='pinky_fingerR6', id=5, color=[255, 153, 255], type='', swap=''),
        6:
        dict(
            name='pinky_fingerR7', id=6, color=[255, 153, 255], type='', swap=''),
        7:
        dict(
            name='pinky_fingerR8', id=7, color=[255, 153, 255], type='', swap=''),
        8:
        dict(
            name='ring_fingerR1', id=8, color=[255, 153, 255], type='', swap=''),
        9:
        dict(
            name='ring_fingerR2',
            id=9,
            color=[102, 178, 255],
            type='',
            swap=''),
        10:
        dict(
            name='ring_fingerR3',
            id=10,
            color=[102, 178, 255],
            type='',
            swap=''),
        11:
        dict(
            name='ring_fingerR4',
            id=11,
            color=[102, 178, 255],
            type='',
            swap=''),
        12:
        dict(
            name='ring_fingerR5',
            id=12,
            color=[102, 178, 255],
            type='',
            swap=''),
        13:
        dict(
            name='ring_fingerR6', id=13, color=[255, 51, 51], type='', swap=''),
        14:
        dict(
            name='ring_fingerR7', id=14, color=[255, 51, 51], type='', swap=''),
        15:
        dict(
            name='ring_fingerR8', id=15, color=[255, 51, 51], type='', swap=''),
	16:
        dict(
            name='middle_fingerR1',
	    id=16,
	    color=[255, 153, 255], type='', swap=''),
        17:
        dict(
            name='middle_fingerR2',
            id=17,
            color=[102, 178, 255],
            type='',
            swap=''),
        18:
        dict(
            name='middle_fingerR3',
            id=18,
            color=[102, 178, 255],
            type='',
            swap=''),
        19:
        dict(
            name='middle_fingerR4',
            id=19,
            color=[102, 178, 255],
            type='',
            swap=''),
        20:
        dict(
            name='middle_fingerR5',
            id=20,
            color=[102, 178, 255],
            type='',
            swap=''),
        21:
        dict(
            name='middle_fingerR6', id=21, color=[255, 51, 51], type='', swap=''),
        22:
        dict(
            name='middle_fingerR7', id=22, color=[255, 51, 51], type='', swap=''),
        23:
        dict(
            name='middle_fingerR8', id=23, color=[255, 51, 51], type='', swap=''),
        24:
        dict(
            name='forefingerR1', id=24, color=[255, 51, 51], type='', swap=''),
        25:
        dict(
            name='forefingerR2', id=25, color=[255, 51, 51], type='', swap=''),
        26:
        dict(
            name='forefingerR3', id=26, color=[255, 51, 51], type='', swap=''),
        27:
        dict(
            name='forefingerR4', id=27, color=[255, 51, 51], type='', swap=''),
        28:
        dict(
            name='forefingerR5', id=28, color=[255, 51, 51], type='', swap=''),
        29:
        dict(
            name='forefingerR6', id=29, color=[255, 51, 51], type='', swap=''),
        30:
        dict(
            name='forefingerR7', id=30, color=[255, 51, 51], type='', swap=''),
        31:
        dict(
            name='forefingerR8', id=31, color=[255, 51, 51], type='', swap=''),
        32:
        dict(name='thumb_fingerR1', id=32, color=[0, 255, 0], type='', swap=''),
        33:
        dict(name='thumb_fingerR2', id=33, color=[0, 255, 0], type='', swap=''),
        34:
        dict(name='thumb_fingerR3', id=34, color=[0, 255, 0], type='', swap=''),
        35:
        dict(name='palmR1', id=35, color=[0, 255, 0], type='', swap=''),
        36:
        dict(name='palmR2', id=36, color=[0, 255, 0], type='', swap=''),
        37:
        dict(name='palmR3', id=37, color=[0, 255, 0], type='', swap=''),
       	},
    skeleton_info={
        0:
        dict(link=('pinky_fingerR1', 'pinky_fingerR3'), id=0, color=[255, 128, 0]),
        1:
        dict(link=('pinky_fingerR2', 'pinky_fingerR3'), id=1, color=[255, 128, 0]),
        2:
        dict(link=('pinky_fingerR3', 'pinky_fingerR4'), id=2, color=[255, 128, 0]),
        3:
        dict(link=('pinky_fingerR3', 'pinky_fingerR6'), id=3, color=[255, 128, 0]),
        4:
        dict(link=('pinky_fingerR5', 'pinky_fingerR6'), id=4, color=[255, 153, 255]),
        5:
        dict(link=('pinky_fingerR6', 'pinky_fingerR7'), id=5, color=[255, 153, 255]),
        6:
        dict(link=('pinky_fingerR6', 'pinky_fingerR8'), id=6, color=[255, 153, 255]),
        7:
        dict(link=('ring_fingerR1', 'ring_fingerR3'), id=7, color=[255, 153, 255]),
        8:
        dict(link=('ring_fingerR2', 'ring_fingerR3'), id=8, color=[102, 178, 255]),
        9:
        dict(
            link=('ring_fingerR3', 'ring_fingerR4'),
            id=9,
            color=[102, 178, 255]),
        10:
        dict(
            link=('ring_fingerR3', 'ring_fingerR6'),
            id=10,
            color=[102, 178, 255]),
        11:
        dict(
            link=('ring_fingerR5', 'ring_fingerR6'),
            id=11,
            color=[102, 178, 255]),
        12:
        dict(link=('ring_fingerR6', 'ring_fingerR7'), id=12, color=[255, 51, 51]),
        13:
        dict(
            link=('ring_fingerR6', 'ring_fingerR8'), id=13, color=[255, 51, 51]),
        14:
        dict(
            link=('middle_fingerR1', 'middle_fingerR3'), id=14, color=[255, 51, 51]),
        15:
        dict(
            link=('middle_fingerR2', 'middle_fingerR3'), id=15, color=[255, 51, 51]),
        16:
        dict(
            link=('middle_fingerR3', 'middle_fingerR4'), id=16, color=[0, 255, 0]),
        17:
        dict(
            link=('middle_fingerR3', 'middle_fingerR6'), id=17, color=[0, 255, 0]),
        18:
        dict(
            link=('middle_fingerR5', 'middle_fingerR6'), id=18, color=[0, 255, 0]),
        19:
        dict(
            link=('middle_fingerR6', 'middle_fingerR7'), id=19, color=[0, 255, 0]),
	20:
        dict(
            link=('middle_fingerR6', 'middle_fingerR8'), id=5, color=[255, 153, 255]),
        21:
        dict(
            link=('forefingerR1', 'forefingerR3'), id=21, color=[255, 51, 51]),
        22:
        dict(
            link=('forefingerR2', 'forefingerR3'), id=22, color=[255, 51, 51]),
        23:
        dict(
            link=('forefingerR3', 'forefingerR4'), id=23, color=[0, 255, 0]),
        24:
        dict(
            link=('forefingerR3', 'forefingerR6'), id=24, color=[0, 255, 0]),
        25:
        dict(
            link=('forefingerR5', 'forefingerR6'), id=25, color=[0, 255, 0]),
        26:
        dict(
            link=('forefingerR6', 'forefingerR7'), id=26, color=[0, 255, 0]),
	27:
        dict(
            link=('forefingerR6', 'forefingerR8'), id=27, color=[255, 153, 255]),
	28:
	dict(link=('thumb_fingerR1', 'thumb_fingerR2'), id=28, color=[255, 153, 255]),
	29:
        dict(link=('thumb_fingerR2', 'thumb_fingerR3'), id=29, color=[255, 153, 255]),
	30:
        dict(link=('thumb_fingerR3', 'palmR3'), id=30, color=[255, 153, 255]),
	31:
        dict(link=('palmR1', 'palmR2'), id=31, color=[255, 153, 255]),
	32:
        dict(link=('palmR1', 'palmR3'), id=32, color=[255, 153, 255]),
	33:
        dict(link=('palmR2', 'palmR3'), id=33, color=[255, 153, 255]),
    },
    joint_weights=[1.] * 38,
    sigmas=[])
