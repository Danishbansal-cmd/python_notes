import pandas as pd

# pandas version
print(pd.__version__)

df = pd.read_csv("ohoo.csv",encoding='cp1252')
# print(df.to_string())
print(df)
print(pd.options.display.max_rows)