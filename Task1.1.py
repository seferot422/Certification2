import pandas as pd
import numpy as np
import random

# Создаем DataFrame
lst = ['robot'] * 10 + ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
print(data)

# Создаем one-hot 
one_hot = pd.get_dummies(data['whoAmI'])
data = pd.concat([data, one_hot], axis=1).drop(columns=['whoAmI'])
print(data)