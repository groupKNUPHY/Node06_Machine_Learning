import numpy as np
import pandas as pd
from IPython.display import display
import awkward as ak
import seaborn as sns
import matplotlib.pyplot as plt


infile='/x4/cms/dylee/Delphes/analysis/ntuple/eee_channel.npy'

dat = np.load(infile,allow_pickle=True)[()]


wzg_dat = dat['WZG']

print(wzg_dat)
columns = wzg_dat.fields
print(columns)


print(len(wzg_dat))

y = np.ones(len(wzg_dat)) * 1
#xsec =  np.ones(len(wzg_dat)) * 
#gen  = 




data = {'y':y}
df = pd.DataFrame(data)



for column in columns:
	print(column,len(wzg_dat[column]))
	df[column] = ak.to_pandas(wzg_dat[column])


display(df)



corr = df.corr()
# Set up the matplotlib figure
f, ax = plt.subplots(figsize=(11, 9))


# Generate a custom diverging colormap
cmap = sns.diverging_palette(230, 20, as_cmap=True)

# Draw the heatmap with the mask and correct aspect ratio
sns.heatmap(corr, cmap=cmap, vmax=.3, center=0,
            square=True, linewidths=.5, cbar_kws={"shrink": .5})

plt.show()
