import torch
from torch.utils.data import Dataset
import numpy as np
import pandas as pd

infile = "/x4/cms/dylee/Delphes/ML/WZG_ML/data/diabetes.csv.gz"

xy = np.loadtxt(infile, delimiter=',', dtype=np.float32)
df = pd.DataFrame(xy)
print(df)
