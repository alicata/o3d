import os
import random
from random import randrange
import numpy as np
import open3d as o3

from datasets import PartDataset
import download
import object_classifier_3d as oc


# download dataset and pre-trained model
download.download_contents()

class Dataset:
    def __init__(self, num_points):
        DATA_FOLDER = 'shapenetcore_partanno_segmentation_benchmark_v0'
        self.num_points = num_points

        self.test_dataset_seg = PartDataset(
            root=DATA_FOLDER,
            train=False,
            classification=False,
            npoints=num_points)
        self.num_samples = len(self.test_dataset_seg)

        self.classes_dict = {'Airplane': 0, 'Bag': 1, 'Cap': 2, 'Car': 3, 'Chair': 4, 
            'Earphone': 5, 'Guitar': 6, 'Knife': 7, 'Lamp': 8, 'Laptop': 9,
            'Motorbike': 10, 'Mug': 11, 'Pistol': 12, 'Rocket': 13, 
            'Skateboard': 14, 'Table': 15}
        self.num_classes = len(self.classes_dict.items())

    def get_sample(self, sample_ix, max_points):
        point_set, seg = self.test_dataset_seg.__getitem__(sample_ix)
        point_set = point_set[0:max_points]
        seg = seg[0:max_points]
        return point_set, seg

    def get_labels(self):
        return list(self.classes_dict.keys())

ds = Dataset(num_points=10000)
classifier = oc.Classifier(ds.num_classes, ds.num_points)

def read_pointnet_colors(seg_labels):
    map_label_to_rgb = {
        1: [0, 255, 0],
        2: [0, 0, 255],
        3: [255, 0, 0],
        4: [255, 0, 255],  # purple
        5: [0, 255, 255],  # cyan
        6: [255, 255, 0],  # yellow
    }
    colors = np.array([map_label_to_rgb[label] for label in seg_labels])
    return colors

cloud = o3.PointCloud()

# max object examples
MAX_SAMPLES = 10 

for i in range(MAX_SAMPLES):
    sample_ix = i*150 
    print('[Sample {} / {}]'.format(sample_ix, ds.num_samples))

    point_set, seg = ds.get_sample(sample_ix, max_points=1000)

    cloud.points = o3.Vector3dVector(point_set)
    cloud.colors = o3.Vector3dVector(read_pointnet_colors(seg.numpy()))
    o3.visualization.draw_geometries([cloud], width=300, height=300)
    
    pred_class, prob = classifier.test(point_set)
    label = ds.get_labels()[pred_class]

    print('predicted object  [{}]  probability {:0.3}'
          .format(label, prob))

