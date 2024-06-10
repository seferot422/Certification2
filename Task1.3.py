import pandas as pd
import random

# Создаем DataFrame
lst = ['robot'] * 10 + ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

# Получаем уникальные значения категориального столбца
categories = sorted(data['whoAmI'].unique())

# Создаем DataFrame, заполненный нулями
one_hot = pd.DataFrame(0, columns=categories, index=data.index)

# Заполняем one-hot DataFrame соответствующими значениями
for category in categories:
    one_hot[category] = (data['whoAmI'] == category).astype(int)

# Объединяем исходный DataFrame с one-hot DataFrame
data = pd.concat([data, one_hot], axis=1)

data.head()