import pandas as pd

df1 = pd.read_csv('CommonInfos.csv', delimiter = ';', index_col = 0)
df1 = df1['Forming (4): Temperature (°C)']
#print(df1)


df2 = pd.read_csv('TemperatureLeft.csv', delimiter = ';', index_col = 0)
df2 = df2.drop(['Unit'], axis=1)
df2 = df2.T
#print(df2.head(10))
run1 = df2[8557]

val = []
for values in run1:
    if values >= 138:
        val.append(values)
#print(val)

df4 = val

df3 = pd.concat([df1, df2, df4], axis=1, join='inner')
df3.to_csv('data_concat.csv')
#df3 = df3.T
#df3.to_csv('data_concat.transposed.csv')

#formtemp = df3['Forming (4): Temperature (Â°C)']

#print(df3)

#print(df3['Cycle'])
#print(formtemp)




