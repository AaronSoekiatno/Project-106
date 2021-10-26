import numpy as np
import plotly.express as px
import pandas as pd

df = pd.read_csv(r"student.csv")
graph = px.scatter(df,x="Roll",y="Days")

roll = df["Roll"].tolist()
days = df["Days"].tolist()

correlation = np.corrcoef(roll, days)
graph.show()
print(correlation)
