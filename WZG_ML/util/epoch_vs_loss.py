import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
csv_file = "../run/history.csv"
history_df = pd.read_csv(csv_file)

history_df[['loss', 'val_loss']].plot()
plt.grid()
plt.show()


plt.close()
history_df[['acc', 'val_acc']].plot()
plt.grid()
plt.show()
