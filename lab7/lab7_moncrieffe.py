"""
janelle moncrieffe
lab 7: apis & data collection
sep 28, 2026
"""

import pandas as pd

# ------
# example 1
# ------

dict_ = {'a': [11,21,31], 'b': [12,22,32]}

df = pd.DataFrame(dict_)
print(df.head())
print(df.mean())


# ------
# example 2: get nba teams
# ------

from static import get_teams

nba_teams = get_teams()

print(f"First 2 teams: {nba_teams[:2]}")

# Convert list to DataFrame
df_teams = pd.DataFrame(nba_teams)
print(df_teams.head())

# Filter the row that contains 'Warriors' nickname
df_warriors = df_teams[df_teams["nickname"].str.lower() == "warriors"]
print(df_warriors)

# Access and save the ID of the Warriors
id_warriors = df_warriors["id"].values[0]
print(f"The ID of the Warriors is: {id_warriors}")


# ------
# example 3: working with external API
# ------

import requests

url = "https://s3-api.us-geo.objectstorage.softlayer.net/cfcourses%20data/CognitiveClass/PY0101EN/Chapter%205/Labs/Golden_State.pkl"
file_name = "Golden_State.pkl"

print("\nDownloading external data...")

response = requests.get(url)

if response.status_code == 200:
    with open(file_name, "wb") as f:
        f.write(response.content)

    print("Download complete.")

    # Load DataFrame from pickle
    games = pd.read_pickle(file_name)

    print("\nGames data from pickle file:")
    print(games.head())

    # Filter GSW vs Raptors
    warriors_vs_raptors = games[games['MATCHUP'].str.contains('TOR')]
    gsw_home_vs_raptors = warriors_vs_raptors[
        warriors_vs_raptors['MATCHUP'].str.contains(' vs. ')
    ]
    gsw_away_vs_raptors = warriors_vs_raptors[
        warriors_vs_raptors['MATCHUP'].str.contains(' @ ')
    ]

    # Calculate averages
    home_avg_plus = gsw_home_vs_raptors['PLUS_MINUS'].mean()
    away_avg_plus = gsw_away_vs_raptors['PLUS_MINUS'].mean()
    home_avg_pts = gsw_home_vs_raptors['PTS'].mean()
    away_avg_pts = gsw_away_vs_raptors['PTS'].mean()

    print(f"Warriors home average {home_avg_plus}")
    print(f"Warriors away average {away_avg_plus}")
    print(f"Warriors home point average {home_avg_pts}")
    print(f"Warriors away point average {away_avg_pts}")

else:
    print("Golden State download failed.")
    print("Status code:", response.status_code)


# ------
# EXERCISE
# ------

print("\nEXERCISE")

# a. Download the CSV file
url = "https://datahub.io/core/english-premier-league/r/season-2324.csv"
file_name = "epl_matches.csv"

print("\nDownloading external data...")

response = requests.get(url)

if response.status_code == 200:
    with open(file_name, "wb") as f:
        f.write(response.content)

    print("Download complete.")
else:
    print("Download failed.")
    print("Status code:", response.status_code)


# b. Load DataFrame from CSV
games = pd.read_csv(file_name)

print("\nGames data from CSV file:")
print(games.head())


# c. Display the columns
print("\nColumns in the dataset:")
print(games.columns)


# d. Calculate home and away goals
home_avg_goals = games["FTHG"].mean()
away_avg_goals = games["FTAG"].mean()

print(f"\nHome average goals: {home_avg_goals}")
print(f"Away average goals: {away_avg_goals}")


# e. Visualize
import matplotlib.pyplot as plt

metrics = ["Home Goals", "Away Goals"]
values = [home_avg_goals, away_avg_goals]

plt.figure(figsize=(8, 5))

plt.bar(metrics, values)

plt.title("Premier League — Home vs Away Goals")
plt.ylabel("Average Goals")

plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.tight_layout()

plt.show()

input("Press Enter to close...")
