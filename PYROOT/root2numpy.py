import pandas as pd
from ROOT import *
from root_numpy import root2array, tree2array
from root_numpy import testdata
from IPython.display import display

test_file = TFile.Open('test.root') 
test_tree = test_file.Get('tree')   
test_arr  = tree2array(test_tree)	
test_df   = pd.DataFrame(test_arr)	
test_df.to_csv('out.csv', mode='w')

display(test_df)









