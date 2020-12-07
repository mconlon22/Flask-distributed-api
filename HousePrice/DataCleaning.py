import pandas as pd

df = pd.DataFrame(columns=['address', 'lon', 'lat'])
for i in range(0, 260000, 10000):
    print("trying"+str(i))
    data = pd.read_csv("./dataoutput/housedata10000.csv", encoding='latin-1')
    df = df.append(data)
    print("found"+str(i))
    print(data.shape)
    print(df.shape)

print(df.shape)

df.to_csv('output.csv')