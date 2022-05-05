import numpy as np
import pandas as pd


def transfer(csv):  # raw 轉置
    data = pd.read_csv(csv, encoding="utf-8")

    # FIXME: what is the different between current implement and below?
    data.columns = data.iloc[2, :]
    data.index = data.iloc[:, 0]
    # c = []
    # column = data.iloc[2, :]  # Column list 項目

    # for x in column:  # 取出作為column list
    #     c.append(x)
    # data.columns = c

    # r = []
    # row = data.iloc[:, 0]  # row list 項目
    # for y in row:  # 取出作為row list
    #     r.append(y)
    # data.index = r
    #########################################

    # FIXME: magic number 3 and 7, replace with some meaningful variable
    SOME_MEANINGFUL_NAME1 = 3
    SOME_MEANINGFUL_NAME2 = 7
    data = data.drop(index=data.index[0:SOME_MEANINGFUL_NAME1], columns=data.columns[0:SOME_MEANINGFUL_NAME2])  # 刪除不需要data
    # data = data.drop(index=data.index[0:3], columns=data.columns[0:7])  # 刪除不需要data
    #########################################

    data = data.T
    return data


def drop_unnecessary_data(data):
    # explain why and how this works
    data = data.drop(index=data.index[0:3], columns=data.columns[0:4])
    data = data.drop(columns=data.columns[2:])  # 刪除不需要data
    return data


def spectransfer(csv):  # 只留spec 轉置

    data = pd.read_csv(csv, encoding="utf-8")

    # FIXME: what is the different between current implement and below?
    data.columns = data.iloc[2, :]
    data.index = data.iloc[:, 0]
    # c = []
    # column = data.iloc[2, :]  # Column list 項目

    # for x in column:  # 取出作為column list
    #     c.append(x)
    # data.columns = c

    # r = []
    # row = data.iloc[:, 0]  # row list 項目
    # for y in row:  # 取出作為row list
    #     r.append(y)
    # data.index = r
    #########################################

    # FIXME: magic number 3 and 4 and 2, extract to a self-expressed function
    data = drop_unnecessary_data(data)
    # data = data.drop(index=data.index[0:3], columns=data.columns[0:4])
    # data = data.drop(columns=data.columns[2:])  # 刪除不需要data
    #########################################

    data = data.T
    return data


files = ["try2.csv", "try3.csv", "try4.csv"]  # csv data list
data = spectransfer("try5.csv")  # spec 掛載

for file in files:  # 合併 spec & data
    data = pd.concat([data, transfer(file)])

# finalitem=[]
Avg = []
Std = []
# Cpk = []
Col = []

# FIXME: what is this part doing? give it a function name
# why there is some code I can remove without impact the output?
for n in range(len(data.columns)):  # 取出每一個data 計算?
    name = data.columns[n]
    # FIXME: not using spechigh, spechlow
    # spechigh = pd.to_numeric(data["NPN"][0])  # Spec high
    # speclow = pd.to_numeric(data["NPN"][1])  # Spec low
    #########################################

    item = pd.to_numeric(data[name][2:].dropna())  # STR to float

    # FIXME: Cpk and Cpk_value is not using, I can get same output even remove those code
    # if (spechigh - item.mean()) >= (item.mean() - speclow):  # Cpk判斷
    #     Cpk_value = (item.mean() - speclow) / (3 * item.std())

    # else:
    #     Cpk_value = (spechigh - item.mean()) / (3 * item.std())
    #########################################

    Avg.append(item.std())
    Std.append(item.std())
    # Cpk = np.append(Cpk, Cpk_value)
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
