import numpy as np
import torch
import torch.nn as nn
import torch.nn.parallel
import torch.optim as optim
import torch.utils.data
import torchvision.datasets as dset
import torchvision.transforms as transforms
import torchvision.utils as vutils
from torch.autograd import Variable

if torch.cuda.is_available():
    import torch.backends.cudnn as cudnn

from pointnet import PointNetCls

MODEL_PATH = 'model/cls_model.pth'

class Classifier:
    def __init__(self, num_classes, num_points):
        # Create the classification network from pre-trained model
        classifier = PointNetCls(k=num_classes, num_points=num_points)
        if torch.cuda.is_available():
            classifier.cuda()
            classifier.load_state_dict(torch.load(MODEL_PATH))
        else:
            classifier.load_state_dict(torch.load(MODEL_PATH, map_location='cpu'))
        classifier.eval()
        self.cls = classifier

    def test(self, point_set):
        # perform inference in GPU
        points = Variable(point_set.unsqueeze(0))
        points = points.transpose(2, 1)

        if torch.cuda.is_available():
            points = points.cuda()
        pred_logsoft, _ = self.cls(points)

        # move data back to cpu for visualization
        pred_logsoft_cpu = pred_logsoft.data.cpu().numpy().squeeze()
        pred_soft_cpu = np.exp(pred_logsoft_cpu)
        pred_class = np.argmax(pred_soft_cpu)
        return pred_class, pred_soft_cpu[pred_class]
