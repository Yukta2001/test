import pandas as pd
data = pd.read_csv("C:\\Users\\mehulidas\\Downloads\\case_no_ds_dt.csv")
#print(data)

#df = ", ".join(data.astype(str).stack().tolist())
def case_id(df_slice):
    return ",".join(["'{}'".format(value) for value in df_slice.astype(str).stack().tolist()])
# print(df)
# df = ",".join(["'{}'".format(value) for value in data.astype(str).stack().tolist()])
# print(df)
b_size = 1000
for start in range(0,len(data),b_size):
    end = start + b_size
    result = case_id(data.iloc[start:end])
    print(result)