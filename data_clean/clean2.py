import pandas as pd

df1 = pd.read_csv("./2020_01-06.csv",sep=",",encoding="big5")
df2 = pd.read_csv("./water.csv",sep=",")


df1 = df1[["縣市","鄉鎮市區","觀測日期","日雨量"]]
df1['city_name'] = df1[['縣市', '鄉鎮市區']].apply(lambda x: ''.join(x), axis=1)
df2 = df2[["city","Name","Lv1_24H","Lv2_24H"]]
df2['city_name'] = df2[['city', 'Name']].apply(lambda x: ''.join(x), axis=1)

df2["city_name"] = df2["city_name"].str.replace("台","臺")
df2["city_name"] = df2["city_name"].str.replace("阿里山鄉","阿里山")

df1[["Lv1_24H","Lv2_24H"]] = 0

for i in df1.index:
    for j in df2.index:
        if df1["city_name"][i] == df2["city_name"][j]:
            for l in [1,2]:
                 df1[f"Lv{l}_24H"][i] = df2[f"Lv{l}_24H"][j]

df3 = df1
df3[["Lv1_alert","Lv2_alert"]] = 0

for i in df3.index:
    for lv in [1,2]:
        if df3["日雨量"][i] >= df3[f"Lv{lv}_24H"][i]:
            df3[f"Lv{lv}_alert"][i] = 1

df3 = df3[df3["Lv1_24H"] != 0]
df4 = df3[["縣市","鄉鎮市區","Lv1_alert","Lv2_alert"]]