import torch
from torch import from_numpy
from torch.utils.data import Dataset
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import pandas as pd

#infile = "../data/diabetes.csv.gz"
infile = "/x4/cms/dylee/Delphes/ML/Node06_Machine_Learning/WZG_ML/data/binary.h5"

class WZGDataset(Dataset):
	""" Diabetes dataset """
	# Initialize your data, download, etc...
	
	def __init__(self):
		df = pd.read_hdf(infile)

		self.len = len(df)
		self.x_data = from_numpy(df.iloc[:, 3:-2].values)
		self.y_data = from_numpy(df.iloc[:, [0]].values)
		self.weight = from_numpy(df.iloc[:, [-2]].values)		
		self.scalefactor = from_numpy(df.iloc[:, [-1]].values)

		# -- MinMax Scaler
		scaler = MinMaxScaler()
		scaler.fit(self.x_data)
		self.x_data = from_numpy(scaler.transform(self.x_data))
		self.y_data[self.y_data > 0] = 1

	def __getitem__(self, index):
		return self.x_data[index], self.y_data[index], self.weight[index], self.scalefactor[index]

	def __len__(self):
		return self.len
