import numpy as np
import pandas as pd
#from IPython.display import display
import awkward as ak
import seaborn as sns
import matplotlib.pyplot as plt

# Data load
eee_infile='/x4/cms/dylee/Delphes/analysis/ntuple/ntuple/eee_channel.npy'
eem_infile='/x4/cms/dylee/Delphes/analysis/ntuple/ntuple/eem_channel.npy'
emm_infile='/x4/cms/dylee/Delphes/analysis/ntuple/ntuple/emm_channel.npy'
mmm_infile='/x4/cms/dylee/Delphes/analysis/ntuple/ntuple/mmm_channel.npy'

eee_data = np.load(eee_infile,allow_pickle=True)[()]
eem_data = np.load(eem_infile,allow_pickle=True)[()]
emm_data = np.load(emm_infile,allow_pickle=True)[()]
mmm_data = np.load(mmm_infile,allow_pickle=True)[()]

# Arrange data by channel 
eee = {
	'WZG' : eee_data['WZG'],
	'WG' : eee_data['WG'],
	'ZG' : eee_data['ZG'],
	'WW' : eee_data['WW'],
	'WZ' : eee_data['WZ'],
	'ZZ' : eee_data['ZZ'],
	'WWW' : eee_data['WWW'],
	'WWZ' : eee_data['WWZ'],
	'WZZ' : eee_data['WZZ'],
	'ZZZ' : eee_data['ZZZ'],
	'ttbarG' : eee_data['ttbarG'],
}

eem = {
	'WZG' : eem_data['WZG'],
	'WG' : eem_data['WG'],
	'ZG' : eem_data['ZG'],
	'WW' : eem_data['WW'],
	'WZ' : eem_data['WZ'],
	'ZZ' : eem_data['ZZ'],
	'WWW' : eem_data['WWW'],
	'WWZ' : eem_data['WWZ'],
	'WZZ' : eem_data['WZZ'],
	'ZZZ' : eem_data['ZZZ'],
	'ttbarG' : eem_data['ttbarG'],
}

emm = {
	'WZG' : emm_data['WZG'],
	'WG' : emm_data['WG'],
	'ZG' : emm_data['ZG'],
	'WW' : emm_data['WW'],
	'WZ' : emm_data['WZ'],
	'ZZ' : emm_data['ZZ'],
	'WWW' : emm_data['WWW'],
	'WWZ' : emm_data['WWZ'],
	'WZZ' : emm_data['WZZ'],
	'ZZZ' : emm_data['ZZZ'],
	'ttbarG' : emm_data['ttbarG'],
}

mmm = {
	'WZG' : mmm_data['WZG'],
	'WG' : mmm_data['WG'],
	'ZG' : mmm_data['ZG'],
	'WW' : mmm_data['WW'],
	'WZ' : mmm_data['WZ'],
	'ZZ' : mmm_data['ZZ'],
	'WWW' : mmm_data['WWW'],
	'WWZ' : mmm_data['WWZ'],
	'WZZ' : mmm_data['WZZ'],
	'ZZZ' : mmm_data['ZZZ'],
	'ttbarG' : mmm_data['ttbarG'],
}

# Plotting
lumi = 3000000

EventDict = {
"WZG" : 899604,
"WG" : 1010000,
"ZG" : 1010000,
"WW" : 1010000,
"WZ" : 1010000,
"ZZ" : 1010000,
"WWW" : 1003323,
"WWZ" : 995610,
"WZZ" : 1010000,
"ZZZ" : 1010000,
"ttbarG" : 1010000
}

xsecDict = {
"WZG" : 0.00173,
"WG" : 23.08,
"ZG" : 4.977,
"WW" : 3.356,
"WZ" : 0.3983,
"ZZ" : 0.04642,
"WWW" : 0.001335,
"WWZ" : 0.0003067,
"WZZ" : 0.00002989,
"ZZZ" : 0.000003157,
"ttbarG" : 2.445
}

pick_cols = []

for i in eee['WZG'].fields:
        if 'lep1' in i:
                pick_cols.append(i)
        if 'lep2' in i:
                pick_cols.append(i)
        if 'lep3' in i:
                pick_cols.append(i)
        if 'Pho' in i:
                pick_cols.append(i)
        if 'MET' in i:
                pick_cols.append(i)

print(pick_cols)

print(eee['WZG'][pick_cols].fields)


def df_make(channel,sum_list):
	for process in channel:
#		process_columns = channel['{0}'.format(process)].fields
		process_columns = channel['{0}'.format(process)][pick_cols].fields
				
		if process == 'WZG':
			y = np.ones(len(channel['{0}'.format(process)])) * 0
			evt = EventDict['WZG']
			xsec = xsecDict['WZG']			
		elif process == 'WG':
			y = np.ones(len(channel['{0}'.format(process)])) * 1
			evt = EventDict['WG']
			xsec = xsecDict['WG']
		elif process == 'ZG':
			y = np.ones(len(channel['{0}'.format(process)])) * 1
			evt = EventDict['ZG']
			xsec = xsecDict['ZG']
		elif process == 'WW':
			y = np.ones(len(channel['{0}'.format(process)])) * 1
			evt = EventDict['WW']
			xsec = xsecDict['WW']
		elif process == 'WZ':
			y = np.ones(len(channel['{0}'.format(process)])) * 1
			evt = EventDict['WZ']
			xsec = xsecDict['WZ']
		elif process == 'ZZ':
			y = np.ones(len(channel['{0}'.format(process)])) * 1
			evt = EventDict['ZZ']
			xsec = xsecDict['ZZ']
		elif process == 'WWW':
			y = np.ones(len(channel['{0}'.format(process)])) * 1
			evt = EventDict['WWW']
			xsec = xsecDict['WWW']
		elif process == 'WWZ':
			y = np.ones(len(channel['{0}'.format(process)])) * 1
			evt = EventDict['WWZ']
			xsec = xsecDict['WWZ']
		elif process == 'WZZ':
			y = np.ones(len(channel['{0}'.format(process)])) * 1
			evt = EventDict['WZZ']
			xsec = xsecDict['WZZ']
		elif process == 'ZZZ':
			y = np.ones(len(channel['{0}'.format(process)])) * 1
			evt = EventDict['ZZZ']
			xsec = xsecDict['ZZZ']
		else:
			y = np.ones(len(channel['{0}'.format(process)])) * 1
			evt = EventDict['ttbarG']
			xsec = xsecDict['ttbarG']

		data = {'y':y, 'Event':evt, 'xsec':xsec}	
		df = pd.DataFrame(data)	
#		df['y']		= y	
#		df['Event']	= evt	
#		df['xsec']	= xsec	

		for column in process_columns:		
			df[column] = ak.to_pandas(channel['{0}'.format(process)][column])

		lista = df.values.tolist()
		sum_list += lista
		
	return sum_list

sum_list=[]
sum_list = df_make(eee,sum_list)
sum_list = df_make(eem,sum_list)
sum_list = df_make(emm,sum_list)
sum_list = df_make(mmm,sum_list)

col = ['y', 'Event', 'xsec']

cols = col + eee['WZG'][pick_cols].fields

df = pd.DataFrame(sum_list, columns=cols)

pd.set_option("display.max_colwidth", 200)

print(df)

df.to_hdf('binary.h5', key='df', mode='w')
'''
corr = df.corr()
f, ax = plt.subplots(figsize=(11,9))

cmap = sns.diverging_palette(230, 20, as_cmap=True)

sns.heatmap()
'''



