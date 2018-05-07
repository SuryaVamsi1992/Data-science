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







sio = StringIO()
sio.write(df.to_csv(index=None, header=None))  # Write the Pandas DataFrame as a csv to the buffer
sio.seek(0)  # Be sure to reset the position to the start of the stream

# Copy the string buffer to the database, as if it were an actual file
with conn.cursor() as c:
    c.copy_from(sio, "schema.table", columns=dataframe.columns, sep=',')
    conn.commit()
