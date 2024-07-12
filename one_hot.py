import random
import pandas as pd
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
data.head()
print(data)


def dum(val):
    lst1 = list()
    for i in range(len(lst)):
        if data[data.columns[0]][i] == val:
            lst1.append(True)
        else:
            lst1.append(False)
    return lst1


values = set(data[data.columns[0]].values)
columns = dict()
for value in values:
    columns[value] = dum(value)
new_data = pd.DataFrame(columns)
new_data.head()
print(new_data)
