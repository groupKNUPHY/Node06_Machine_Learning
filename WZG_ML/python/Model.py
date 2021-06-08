import torch
import torch.nn as nn
import torch.nn.functional as F

class Model(nn.Module):

	def __init__(self):
		super(Model, self).__init__()
		self.l1 = nn.Linear(8, 6)
		self.l2 = nn.Linear(6, 4)
		self.l3 = nn.Linear(4, 1)
		self.sigmoid = nn.Sigmoid()

	def forward(self, x):
		out1 = F.relu(self.l1(x))
		out2 = F.relu(self.l2(out1))
		y_pred = self.sigmoid(self.l3(out2))
		return y_pred
