# %%
from fpgrowth_py import fpgrowth
import pandas as pd
import pickle
import os

# %%

playlist_df = pd.read_csv("./data/2023_spotify_ds1.csv", delimiter=",")
print(playlist_df.shape)
playlist_df.head(5)

# %%
grouped_playlist = playlist_df.groupby("pid").agg({"track_name": list})
grouped_playlist.rename(columns={"track_name": "musicas"}, inplace=True)

print(grouped_playlist.shape)
grouped_playlist.head(5)

# %%
playlists = grouped_playlist["musicas"].tolist()
len(playlists)

# %%
freqItemSet, rules = fpgrowth(playlists, minSupRatio=0.1, minConf=0.5)

# %%
rules[0]

# %%
inferencias = {}
for rule in rules:
    musics = tuple(rule[0])
    if musics not in inferencias:
        inferencias[musics] = (list(rule[1]), rule[2])
    elif rule[2] > inferencias[musics][1]:
        inferencias[musics] = (list(rule[1]), rule[2])

# %%
mostFreqMusic = playlist_df["track_name"].value_counts().idxmax()

# %%
versao = str(os.environ["LATEST_TAG"])
print(versao)

# %%
model = {
    "musica_mais_frequente": mostFreqMusic,
    "inferencias": inferencias,
    "versao": versao,
}

# %%
with open("./data/model.pkl", "wb") as file:
    pickle.dump(model, file)
