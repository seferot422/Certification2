import pandas as pd
import random

# Генерация данных
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

# Получение уникальных значений из столбца 'whoAmI'
categories = list(set(lst))

# Создание словаря для one-hot представления
one_hot_dict = {}
for category in categories:
    one_hot_dict[category] = []

# Заполнение словаря one-hot представления
for index, row in data.iterrows():
    for category in categories:
        if row['whoAmI'] == category:
            one_hot_dict[category].append(1)
        else:
            one_hot_dict[category].append(0)

# Создание DataFrame из словаря
one_hot_data = pd.DataFrame(one_hot_dict)

# Объединение one-hot представления с исходным DataFrame
data = pd.concat([data, one_hot_data], axis=1)

data.head()