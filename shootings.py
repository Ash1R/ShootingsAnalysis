import numpy as np
import pandas as pd
import collections

# To do
# What days have most shootings
# Average casualties per day
# Which states are most affected
# Totals
# Are there cities affected?
# A look at the "big-news" mass shootings

shootings_data = pd.read_csv(
    "/export-55f18053-21f5-4dd8-8ac0-d3bf6608d62b.csv")

shootings_data.groupby("Incident ID").describe()
