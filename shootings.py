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
    "export-55f18053-21f5-4dd8-8ac0-d3bf6608d62b.csv")

shootings_data.groupby("City")

states_data = pd.read_csv("csvData.csv")

states_data.groupby("State")

states_data = states_data.reset_index()

statespop = {}
for index, row in states_data.iterrows():
    statespop[row["State"]] = row["Pop"]

# an analysis of shootings by state
states = shootings_data.State.str.split(",").apply(collections.Counter)
states_g = states.sum().most_common()
# print(states_g[:10])

# population adjusted shootings by state
states_p = []
for i in states_g:
    states_p.append((i[0], (i[1]/statespop[i[0]]) * 1000000))
print(states_p)

# an analysis of shootings by city
county = shootings_data.City.str.split(",").apply(collections.Counter)
county_g = county.sum().most_common()
# print(county_g[:10])


# shootings above 4 deaths (the ones that make headlines)
"""xd = 5
d_shootings = shootings_data[(shootings_data.Killed >= 20).copy()]
d_states = d_shootings.State.str.split(",").apply(collections.Counter)
dg_states = d_states.sum().most_common()
print(dg_states[:10])"""
