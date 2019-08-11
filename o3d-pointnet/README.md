# Open3D-PointNet
Simple wrapper class around PointNet (PyTorch) to easly test inference over a point cloud sample.
The 3d object classifier class is implemented in `object_classifier_3d.py'.

This repository is forked from
['Open3D implementation'](https://github.com/fxia22/pointnet.pytorch).
![seg](misc/o3d_visualize.png)

# PointNet Dataset
The ShapeNetCore dataset is called `shapenetcore_partanno_segmentation_benchmark_v0`.
* 10 classes
* point clouds, labels
* per-point annotation parts (segmentations)

# Tools
* dataset.py: load PointNet datasets 
* download.py: download datasets and pre-trained model
* OGL visualization: open3d_visulized.py


# Setup
Install O3D and PyTorch.

```bash
pip install open3d-python
pip install -r requirements.txt
```

# Inference
Datasets and model will be downloaded by script.
```bash
python test_inference.py
```

# References
[open3d]: https://github.com/IntelVCL/Open3D
