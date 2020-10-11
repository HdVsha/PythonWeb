import csv
import pandas as pd

newarr = pd.read_csv('table.csv', header=0)
newarr['my_col'] = [True for i in range(len(newarr))]
newarr.to_csv('new_col.csv', index=False)
