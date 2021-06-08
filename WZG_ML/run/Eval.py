import numpy as np
import pandas as pd
import sys, os
import matplotlib.pyplot as plt

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

## Device set and Optimizer set
from Model import Model

device = 'cpu'
if torch.cuda.is_available() & use_gpu:
        model = Model()
        model = model.to('cuda')
        device = 'cuda'

model.load_state_dict(torch.load('weightFile.pth'))

optm = optim.Adam(model.parameters(), lr=0.01)


# Evaluation
from tqdm.auto import tqdm
from sklearn.metrics import roc_curve, roc_auc_score, confusion_matrix

labels, preds = [], []
predFile = 'prediction.csv'

for i, (data, label) in enumerate(tqdm(test_loader)):
	data = data.float().to(device)
	pred = model(data).detach().to('cpu').float()

	labels.extend([x.item() for x in label])
	preds.extend([x.item() for x in pred.view(-1)])

df = pd.DataFrame({'label': labels, 'prediction': preds})
df.to_csv(predFile, index=False)

df = pd.read_csv(predFile)
tpr, fpr, thr = roc_curve(df['label'], df['prediction'], pos_label=0)
auc = roc_auc_score(df['label'], df['prediction'])

df_bkg = df[df.label == 0]
df_sig = df[df.label == 1]
plt.rcParams['figure.figsize'] = (6,6)

hbkg1 = df_bkg['prediction'].plot(kind='hist', histtype='step', bins=15,linewidth=3, color='crimson', label='Negative')
hsig1 = df_sig['prediction'].plot(kind='hist', histtype='step',bins=15, linewidth=3,color='royalblue', label='Positive')
plt.xlabel('DNN score', fontsize=17)
plt.ylabel('Events', fontsize=17)
plt.legend(fontsize=15)
plt.grid()
plt.savefig("DNN_score.png")

plt.close()
plt.plot(fpr, tpr, '-',linewidth=2, label='%s %.3f' % ("auc", auc))
plt.xlim(0, 1.000)
plt.ylim(0, 1.000)
plt.xlabel('False Positive Rate', fontsize=17)
plt.ylabel('True Positive Rate', fontsize=17)
plt.legend(fontsize =17)
plt.savefig("ROC.png")




