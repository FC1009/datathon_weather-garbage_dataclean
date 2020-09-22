import pandas as pd
import os
from app.app import alert_cout

for file_name in os.listdir("./data"):
    
    country_name = file_name.split("0")[0]

    df1 = pd.read_csv("./data{}".format(file_name),sep=",")
    # filter = df1['時間'].apply(str) >= "2020-01-01-01" && <= "2020-06-30-24"
    # df
    df2 = df1[["時間","縣市","鄉鎮市區","降雨量"]]
    df2[["日期","時間"]] = df2["時間"].str.split(' ',expand=True)
    '''
    df2 = df2[df2["降雨量"] != "T"]
    df2 = df2[df2["降雨量"] != "X"]
    df2 = df2[df2["降雨量"] != "..."]
    df2 = df2[df2["降雨量"] != "\\"]
    '''
    df3 = df2.groupby(["時間"])["降雨量"].max()
    df4 = pd.DataFrame({'時間':df3.index, '降雨量':df3.values})
    df4 = alert_cout(df4)

    df3 = df2.groupby(["時間"])["降雨量"].rolling(24).max()
    df4 = pd.DataFrame({'時間':df3.index, '降雨量':df3.values})
    df4 = alert_cout(df4)

    df3 = df2.groupby(["時間"])["降雨量"].rolling(6).max()