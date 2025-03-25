import pandas as pd
url = "https://od.cdc.gov.tw/eic/NHI_EnteroviralInfection.csv"
df = pd.read_csv(url)

# df.iloc[4,4]
# df.loc[4,"縣市"]

# df.iloc[2:6,]
# df.loc[2:5,]

# df.iloc[:,1:5]
# df.loc[:,"週":"縣市"]

# df["週"]
# df["週":"縣市"] error

# df[["週","縣市"]]
# df[["週","就診類別","年齡別","縣市"]]

# type(df["週"])
# type(df[["週","縣市"]])
