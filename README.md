# Data-science
Data science practise

temp = []
for i in range(len(df)):
    value = list(df.loc[i,:])[0]
    value = value.split(",")
    print (len(value))
    value[0] = value[0][1:]
    value[-1] = value[0][:-1]
    for j in range(len(value)):
        value[j] = value[j][2:-1]
        value[j] = value[j].split(":")
        temp.append(value[j][0])
dataframe = pd.DataFrame(temp)
dataframe.columns = ['Name']
print (len(dataframe))
