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

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--epoch', type=int,default=100,
            help="--epoch EPOCH")
parser.add_argument('--batch', type=int,default=512,
            help="--batch BATCH_SIZE")
parser.add_argument('--lr', type=float,default=0.01,
            help="--lr LEARNING_RATE")
args = parser.parse_args()

## Hyperparameter
batch_size = args.batch
LR = args.lr
EPOCH = args.epoch


sys.path.append("../python")
from DataLoader import WZGDataset

dataset = WZGDataset()

lengths = [int(0.6*len(dataset)), int(0.2*len(dataset))]
lengths.append(len(dataset) - sum(lengths))

torch.manual_seed(123456)
train_dataset, val_dataset, test_dataset = torch.utils.data.random_split(dataset, lengths)
torch.manual_seed(torch.initial_seed())

test_loader = DataLoader(dataset=dataset,batch_size=batch_size,shuffle=False,num_workers=2)

## Device set and Optimizer set
from Model import Model

device = 'cpu'
if torch.cuda.is_available() & use_gpu:
        model = Model()
        model = model.to('cuda')
        device = 'cuda'

model.load_state_dict(torch.load('weightFile.pth'))

optm = optim.Adam(model.parameters(), lr=LR)


# Evaluation
from tqdm.auto import tqdm
from sklearn.metrics import roc_curve, roc_auc_score, confusion_matrix

labels, preds = [], []
weights, scaleWeights = [], []
predFile = 'prediction.csv'

#for i, (data, label, weight, scalefactor) in enumerate(tqdm(test_loader)): # Use SF
for i, (data, label, weight) in enumerate(tqdm(test_loader)): # Not use SF
	data = data.float().to(device)
	weight = weight.float()
	pred = model(data).detach().to('cpu').float()

	labels.extend([x.item() for x in label])
	preds.extend([x.item() for x in pred.view(-1)])
	weights.extend([x.item() for x in weight.view(-1)]) 
	#scaleWeights.extend([x.item() for x in (weight*scalefactor).view(-1)]) # Use SF

#df = pd.DataFrame({'label': labels, 'prediction': preds, 'weight': weights, 'scaleWeight': scaleWeights}) # Use SF
df = pd.DataFrame({'label': labels, 'prediction': preds, 'weight': weights}) # Not use SF
df.to_csv(predFile, index=False)

df = pd.read_csv(predFile)
tpr, fpr, thr = roc_curve(df['label'], df['prediction'], sample_weight=df['weight'], pos_label=0)
auc = roc_auc_score(df['label'], df['prediction'], sample_weight=df['weight'])

df_bkg = df[df.label == 1]
df_sig = df[df.label == 0]
plt.rcParams['figure.figsize'] = (6,6)

hbkg1 = df_bkg['prediction'].plot(kind='hist', histtype='step', weights=df_bkg['weight'], bins=15,linewidth=3, color='crimson', label='BKG')
hsig1 = df_sig['prediction'].plot(kind='hist', histtype='step', weights=df_sig['weight'], bins=15, linewidth=3,color='royalblue', label='SIG')
plt.xlabel('DNN score', fontsize=17)
plt.ylabel('Events', fontsize=17)
plt.legend(fontsize=15)
plt.grid()
plt.savefig("DNN_score.png")
plt.close()

# DNN score with SF
#hbkg2 = df_bkg['prediction'].plot(kind='hist', histtype='step', weights=df_bkg['scaleWeight'], bins=15,linewidth=3, color='crimson', label='BKG')
#hsig2 = df_sig['prediction'].plot(kind='hist', histtype='step', weights=df_sig['scaleWeight'], bins=15, linewidth=3, color='royalblue', label='SIG')
#plt.xlabel('DNN score', fontsize=17)
#plt.ylabel('Events', fontsize=17)
#plt.legend(fontsize=15)
#plt.grid()
#plt.savefig("DNN_score2(SF,512).png")


plt.close()
plt.plot(fpr, tpr, '-',linewidth=2, label='%s %.3f' % ("auc", auc))
plt.xlim(0, 1.000)
plt.ylim(0, 1.000)
plt.xlabel('False Positive Rate', fontsize=17)
plt.ylabel('True Positive Rate', fontsize=17)
plt.legend(fontsize =17)
plt.savefig("ROC.png")




