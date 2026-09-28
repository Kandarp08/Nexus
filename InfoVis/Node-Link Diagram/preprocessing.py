# Import necessary libraries

import numpy as np
import pandas as pd
import os

subdir = [x[0] for x in os.walk("../twitch/")] # Folders corresponding to different languages

# Iterate through each subdirectory
for dir in subdir:

    if dir == "../twitch/":
        continue

    lang = dir[10:] # Language corresponding to the network

    df = pd.read_json(f"{dir}/musae_{lang}_features.json", lines=True) # Feature list of nodes
    edges = pd.read_csv(f"{dir}/musae_{lang}_edges.csv")               # Edge list

    total = 0 # Sum of number of features of all nodes 
    count = 0 # Number of nodes

    for column_name, features in df.iterrows():
        total += len(features[0])
        count += 1

    avg_features = total // count # Average number of features of each node

    print(f"Language: {lang}, Average Features: {avg_features}")

    # For new edge list
    new_from = [] 
    new_to = []

    for idx, row in edges.iterrows():

        u = row["from"]
        v = row["to"]

        # Only select those nodes for which abs(Number of features - Average features) = 1
        if abs(len(df[u][0]) - avg_features) <= 1 and abs(len(df[v][0]) - avg_features) <= 1:
            new_from.append(u)
            new_to.append(v) 

    new_edges = []
    new_edges.append(new_from)
    new_edges.append(new_to)

    new_edges = np.array(new_edges).T

    # Save new edge list
    new_edges = pd.DataFrame(new_edges)
    new_edges.to_csv(f"./Edges/{lang}_edges.csv", index=False, header=["from", "to"])

