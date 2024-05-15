import pandas as pd

data_frame = pd.read_csv("datos.csv", delimiter=",")

data_frame["Fi"] = data_frame["fi"].cumsum()
data_frame["ri"] = data_frame["fi"] / data_frame["fi"].sum()
data_frame["Ri"] = data_frame["ri"].cumsum()
data_frame["pi%"] = data_frame["ri"] * 100
data_frame["Pi%"] = data_frame["pi%"].cumsum()

data_frame.to_clipboard(
  decimal=','
)



print(data_frame.head())