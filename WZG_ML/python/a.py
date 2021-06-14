import pandas as pd
from torch import from_numpy


infile = "/x4/cms/dylee/Delphes/ML/Node06_Machine_Learning/WZG_ML/data/binary.h5"

df = pd.read_hdf(infile)
print(df)


