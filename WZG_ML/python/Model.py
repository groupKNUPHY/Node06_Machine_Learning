import torch
import torch.nn as nn
import torch.nn.functional as F

class Model(nn.Module):

	def __init__(self):
		super(Model, self).__init__()

		self.fc = nn.Sequential(

			# 1st layer
			nn.Linear(8, 32),
			nn.ReLU(),
			nn.BatchNorm1d(32),
			
			# 2nd layer
            nn.Linear(32, 32),
			nn.ReLU(),
			nn.BatchNorm1d(32),

			# 5th layer
            nn.Linear(32, 1),
			nn.Sigmoid(),
		)


	def forward(self, x):
		y_pred = self.fc(x)
		return y_pred
