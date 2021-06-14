import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

infile = "/x4/cms/dylee/Delphes/analysis/ntuple/df/h5data/binary.h5"
df = pd.read_hdf(infile)

df = df.drop(['lep1_mass', 'lep2_mass', 'lep3_mass'], axis=1)

df['weight'] = (df['xsec'] * 3000000)/df['Event']

#df.to_hdf('binary.h5', key = 'df', mode = 'w')


sigY = df[df['y'] == 0]['weight'].sum(axis = 0, skipna = False)

bkgY = df[df['y'] == 1]['weight'].sum(axis = 0, skipna = False)

sf = sigY/bkgY

data = []

for i in df['y']:
	if i == 0:
		data.append(1)
	else:
		data.append(sf)

df['SF'] = data

df.to_hdf('binary.h5', key = 'df', mode = 'w')


#df[df['y'] == 0]['SF'] = 
#df[df['y'] == 1]['SF'] = sf

#df1 = df[df['y'] > 0]

#print(df1['y'].replace(['y'], '1'))

#print(df.loc[df.y > 0, 'y'] = 1)

#print(df[df['y'] > 0].iloc[:, [0]].values)


#df['sf'] = 
