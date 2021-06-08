import torch
from torch import from_numpy
from torch.utils.data import Dataset
import numpy as np


infile = "/x4/cms/dylee/Delphes/ML/WZG_ML/data/diabetes.csv.gz"

class DiabetesDataset(Dataset):
	""" Diabetes dataset """
	# Initialize your data, download, etc...
	
	def __init__(self):
		xy = np.loadtxt(infile,delimiter = ',', dtype=np.float32)
		self.len = xy.shape[0]
		self.x_data = from_numpy(xy[:, 0:-1])
		self.y_data = from_numpy(xy[:, [-1]])

	def __getitem__(self, index):
		return self.x_data[index], self.y_data[index]

	def __len__(self):
		return self.len
