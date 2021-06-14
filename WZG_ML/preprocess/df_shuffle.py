import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import sklearn

infile = "/x4/cms/dylee/Delphes/analysis/ntuple/df/h5data/binary.h5"
df = pd.read_hdf(infile)

df['weight'] = (df['xsec'] * 3000000)/df['Event']

# use pandas 
df_shuffled_pd = df.sample(frac=1).reset_index(drop=True)
print(df_shuffled_pd)

# use numpy 
df_shuffled_np = df.iloc[np.random.permutation(df.index)].reset_index(drop=True)
print(df_shuffled_np)

# use sklearn
df_shuffled_sk = sklearn.utils.shuffle(df)
print(df_shuffled_sk)

