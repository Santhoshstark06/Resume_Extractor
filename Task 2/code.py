from datasets import load dataset

import itertools

dataset = load_dataset('csv', data files='/content/training data.csv') 
for row in itertools.islice(dataset ['train'], 10): 
  print(row)
