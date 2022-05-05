import numpy as np
import pandas as pd


def transfer(csv):  # raw 轉置
    data = pd.read_csv(csv, encoding="utf-8")

    c = []
    column = data.iloc[2, :]  # Column list 項目

    for x in column:  # 取出作為column list
        c.append(x)
    data.columns = c

    r = []
    row = data.iloc[:, 0]  # row list 項目
    for y in row:  # 取出作為row list
        r.append(y)
    data.index = r

    data = data.drop(index=data.index[0:3], columns=data.columns[0:7])  # 刪除不需要data
    data = data.T
    return data


def spectransfer(csv):  # 只留spec 轉置

    data = pd.read_csv(csv, encoding="utf-8")

    c = []
    column = data.iloc[2, :]  # Column list 項目

    for x in column:  # 取出作為column list
        c.append(x)
    data.columns = c

    r = []
    row = data.iloc[:, 0]  # row list 項目
    for y in row:  # 取出作為row list
        r.append(y)
    data.index = r

    data = data.drop(index=data.index[0:3], columns=data.columns[0:4])
    data = data.drop(columns=data.columns[2:])  # 刪除不需要data
    data = data.T
    return data


files = ["try2.csv", "try3.csv", "try4.csv"]  # csv data list
data = spectransfer("try5.csv")  # spec 掛載

for file in files:  # 合併 spec & data
    data = pd.concat([data, transfer(file)])

# finalitem=[]
Avg = []
Std = []
Cpk = []
Col = []

for n in range(len(data.columns)):  # 取出每一個data 計算?
    name = data.columns[n]
    spechigh = pd.to_numeric(data["NPN"][0])  # Spec high
    speclow = pd.to_numeric(data["NPN"][1])  # Spec low
    item = pd.to_numeric(data[name][2:].dropna())  # STR to float

    if (spechigh - item.mean()) >= (item.mean() - speclow):  # Cpk判斷
        Cpk_value = (item.mean() - speclow) / (3 * item.std())

    else:
        Cpk_value = (spechigh - item.mean()) / (3 * item.std())

    Avg.append(item.std())
    Std.append(item.std())
    Cpk = np.append(Cpk, Cpk_value)
    Col.append(name)

result = pd.DataFrame(
    {
        "Parameter": Col,
        "Average": Avg,
        "Std": Std,
    }
)
print(result)
result.to_csv("MerRecal.csv")  # 輸出csv
