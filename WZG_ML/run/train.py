import numpy as np
import pandas as pd
import sys, os
import csv

import torch
from torch.utils.data import Dataset, DataLoader
from torch import nn, from_numpy, optim
from torch.utils.data.dataset import random_split
import torch.nn.functional as F

## Check GPU
def GPU_check():
	if torch.cuda.is_available():

		nGPU = torch.cuda.device_count()
		print("Number of GPU : {0}".format(nGPU))
	
		for i,j in enumerate(range(nGPU)):
			print("Device", i, torch.cuda.get_device_name(i))

	else:
		print("No GPU for use")

GPU_check()
use_gpu=True


## Dataset, Hyperparameter
batch_size = 32
LR = [0.01]
EPOCH = [100, 500, 1000]

sys.path.append("/x4/cms/dylee/Delphes/ML/WZG_ML/python")
from DataLoader import DiabetesDataset

dataset = DiabetesDataset()

lengths = [int(0.6*len(dataset)), int(0.2*len(dataset))]
lengths.append(len(dataset) - sum(lengths))

torch.manual_seed(123456)
train_dataset, val_dataset, test_dataset = torch.utils.data.random_split(dataset, lengths)
torch.manual_seed(torch.initial_seed())

train_loader = DataLoader(dataset=dataset,batch_size=batch_size,shuffle=False,num_workers=2)
val_loader = DataLoader(dataset=dataset,batch_size=batch_size*2,shuffle=False,num_workers=2)
test_loader = DataLoader(dataset=dataset,batch_size=batch_size,shuffle=False,num_workers=2)


## Model, Device set and Optimizer set
from Model import Model

device = 'cpu'
if torch.cuda.is_available() & use_gpu:
	model = Model()
	model = model.to('cuda')
	device = 'cuda'

optm = optim.Adam(model.parameters(), lr=0.01)


## Training Step
from tqdm.auto import tqdm
from sklearn.metrics import accuracy_score

bestWeight, bestLoss = {}, 1e9
try:
	history = {'loss': [], 'acc': [], 'val_loss': [], 'val_acc': []}

# Start EPOCH
	for epoch in tqdm(range(1,EPOCH[1]+1)):

		# Training Stage
		model.train()
		optm.zero_grad() # initialize grad data
		train_loss, train_acc = 0., 0.
		
		for i, (x_data, label) in enumerate(train_loader):
			x_data = x_data.float().to(device) # Make tensor on the gpu or cpu
			label = label.float().to(device)

			pred = model(x_data)
			crit = torch.nn.BCELoss(reduction='mean') # binary cross entropy
		
			if device == 'cuda': crit = crit.cuda() # GPU case
			loss = crit(pred,label)
			loss.backward()

			optm.step()

			train_loss += loss.item()
			train_acc += accuracy_score(label.to('cpu'), np.where(pred.to('cpu') > 0.5, 1, 0))
		
		train_loss /= len(train_loader)
		train_acc /= len(train_loader)

		# Validation Stage
		model.eval()
		val_loss, val_acc = 0., 0.
		
		for i, (x_data,label) in enumerate(val_loader):
			x_data = x_data.float().to(device)
			label = label.float().to(device)

			pred = model(x_data)
			crit = torch.nn.BCELoss(reduction='mean')

			loss = crit(pred,label)
			val_loss += loss.item()
			val_acc += accuracy_score(label.to('cpu'), np.where(pred.to('cpu') > 0.5, 1, 0))

		val_loss /= len(val_loader)
		val_acc /= len(val_loader)

		# Update weight of best epoch checking validation loss
		if bestLoss > val_loss:
			bestWeight = model.state_dict()
			bsetLoss = val_loss
			
			torch.save(bestWeight, 'weightFile.pth')		

		history['loss'].append(train_loss)
		history['acc'].append(train_acc)
		history['val_loss'].append(val_loss)
		history['val_acc'].append(val_acc)

		if epoch % 10 == 1:
			print("Epoch: {0}, Train Loss: {1}, Val Loss: {2}, Train Acc: {3}, Val Acc: {4}".format(epoch,train_loss,val_loss,train_acc,val_acc))

		with open('history.csv', 'w') as f:
			writer = csv.writer(f)
			keys = history.keys()
			writer.writerow(keys)
			for row in zip(*[history[key] for key in keys]):
				writer.writerow(row)
		

except KeyboardInterrupt:
	print("Muyaho!")


